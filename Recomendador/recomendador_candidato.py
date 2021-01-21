def recomendador_candidato(x):
    

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="blocktiedb")
    mycursor = mydb.cursor()
    
    # traer candidato
    
    id_candidato = x #parametro_funcion
    mycursor.execute("DELETE FROM recomendaciones WHERE id_candidato = {}".format(id_candidato))
    mycursor.execute('SELECT certificado.titulo, certificado.menciones, candidato.experiencia_laboral FROM persona, candidato, certificado WHERE persona.id = candidato.id_persona AND persona.id = certificado.id_persona_candidato AND persona.id = {}'.format(id_candidato))
    lista_candidato = mycursor.fetchall()
    largo_lista = len(lista_candidato)
    contador = 0
    myresult = []
    for edu in lista_candidato:
        contador += 1
        if contador < largo_lista:
            myresult.append(edu[0])
            myresult.append(edu[1])
        else:
            myresult.append(edu[0])
            myresult.append(edu[1])
            myresult.append(edu[2])
    
    # traer oferta
    mycursor.execute("SELECT empresa.nombre, oferta.cargo_requerido, empresa.industria, oferta.area_de_trabajo, oferta.experiencia_laboral_req FROM empresa, oferta WHERE empresa.id = oferta.id_empresa")
    myresult2 = mycursor.fetchall()
    
    df2 = pandas.DataFrame(myresult2, columns=['Nombrecomp', 'títuloprofesional', 'Industria', 'Funciónlaboral', 'experiencia'])
    
    auxofertas = []
    for index, rows in df2.iterrows():
        # Create list for the current row
        my_list2 = [rows.títuloprofesional, rows.Industria, rows.Funciónlaboral]
    
        # append the list to the final list
        auxofertas.append(my_list2)
    
    listaofertas = []
    
    
    def tokenizer(lista):
        string = ' '.join(lista)
        string = nlp(string)
        borrador = [t.orth_ for t in string if not t.is_punct | t.is_stop]
        borrador = ' '.join(borrador)
        return borrador
    
    
    def recomendador(can, candidato):
        lista = []
        candidato = nlp(candidato)
        for of in range(len(listaofertas)):
            oferta = nlp(listaofertas[of])
            if candidato.vector_norm and oferta.vector_norm and float(experiencia) >= float(df2['experiencia'].iloc[of]):
                similaridad = candidato.similarity(oferta)
                lista2 = [similaridad, can, of]
                lista.append(lista2)
            else:
                similaridad = 0
                lista2 = [similaridad, can, of]
                lista.append(lista2)
        return lista
    
    
    experiencia = myresult.pop(-1)
    token_candidato = tokenizer(myresult)
    
    for o in auxofertas:
        y = tokenizer(o)
        listaofertas.append(y)
    
    recomendacion = recomendador(id_candidato, token_candidato)
    
    # ingresar recomendacion a DB
    for lista in recomendacion:
        similarity = float(lista[0])
        id_candidato = int(lista[1])
        id_oferta = lista[2] + 1
        cur = mydb.cursor()
        cur.execute('INSERT INTO recomendaciones (similarity, id_candidato, id_oferta) VALUES (%s, %s, %s)',
                    (similarity, id_candidato, id_oferta))
        mydb.commit()
    
    # obtener oferta
    mycursor.execute('SELECT empresa.nombre, oferta.cargo_requerido, empresa.industria, oferta.area_de_trabajo, oferta.experiencia_laboral_req, oferta.id FROM empresa, oferta, recomendaciones WHERE empresa.id = oferta.id_empresa AND oferta.id = recomendaciones.id_oferta AND recomendaciones.id_candidato = {} ORDER BY recomendaciones.similarity DESC LIMIT 0,5'.format(int(id_candidato)))
    myresult3 = mycursor.fetchall()
    print(myresult3)
    return(myresult3)