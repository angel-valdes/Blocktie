def recomendador_reclutador(id_oferta):

    nlp = spacy.load('es_core_news_md')

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="blocktiedb")
    mycursor = mydb.cursor()

    #Borrar recomendaciones anteriores
    mycursor.execute("DELETE FROM recomendaciones WHERE id_oferta = {}".format(id_oferta))

    # traer oferta
    mycursor.execute("SELECT oferta.cargo_requerido, oferta.area_de_trabajo, oferta.experiencia_laboral_req FROM empresa, oferta WHERE empresa.id = oferta.id_empresa AND oferta.id = %s", (id_oferta,))
    oferta_mysql = mycursor.fetchall()


    # traer candidatos

    mycursor.execute('SELECT persona.id FROM persona, candidato, certificado WHERE persona.id = candidato.id_persona AND persona.id = certificado.id_persona_candidato')
    id_candidatos = mycursor.fetchall()
    id_candidatos = set(id_candidatos)
    id_candidatos = sorted(id_candidatos)

    aux_candidatos = []
    for can in id_candidatos:
        mycursor.execute('SELECT certificado.titulo, certificado.menciones, candidato.experiencia_laboral FROM persona, candidato, certificado WHERE persona.id = candidato.id_persona AND persona.id = certificado.id_persona_candidato AND persona.id = {}'.format(can[0]))
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
                #myresult.append(edu[3])
                myresult.insert(0, can[0])
                aux_candidatos.append(myresult)


    listaofertas=[]

    def tokenizer(lista):

        string = ' '.join(lista)
        string = nlp(string)
        borrador = [t.orth_ for t in string if not t.is_punct | t.is_stop]
        borrador = ' '.join(borrador)
        return borrador

    def recomendador(of, oferta2):
        lista = []
        experiencia_oferta = oferta2[0]
        oferta2 = nlp(oferta2[1])
        for candidato in lista_candidatos:
            can = candidato[0]
            experiencia_candidato = candidato[1]
            candidato = nlp(candidato[2])
            if oferta2.vector_norm and candidato.vector_norm and float(experiencia_candidato) >= float(experiencia_oferta):
                similaridad = oferta2.similarity(candidato)
                lista2 = [similaridad, can, of]
                lista.append(lista2)
            else:
                similaridad = 0
                lista2 = [similaridad, can, of]
                lista.append(lista2)
        return lista

    lista_candidatos = []
    for c in aux_candidatos:
        aux = []
        id_candidato = c[0]
        experiencia_candidato = c[-1]
        c = c[1:len(c)-1]
        y = tokenizer(c)
        aux.append(id_candidato)
        aux.append(experiencia_candidato)
        aux.append(y)
        lista_candidatos.append(aux)

    oferta = []
    o = oferta_mysql[0][:2]
    features_token= tokenizer(o)
    oferta.append(oferta_mysql[0][-1])
    oferta.append(features_token)

    r = recomendador(id_oferta, oferta)

    for lista in r:
       similarity = float(lista[0])
       id_candidato = lista[1]
       cur = mydb.cursor()
       cur.execute('INSERT INTO recomendaciones (similarity, id_candidato, id_oferta) VALUES (%s, %s, %s)',
                   (similarity, id_candidato, id_oferta))
       mydb.commit()

    mycursor.execute('SELECT recomendaciones.id_candidato FROM recomendaciones WHERE recomendaciones.id_oferta = {} ORDER BY recomendaciones.similarity DESC LIMIT 0,5'.format(int(id_oferta)))
    myresult3 = mycursor.fetchall()
    id_personas_recomendadas = [myresult3[0][0], myresult3[1][0], myresult3[2][0], myresult3[3][0], myresult3[4][0]]
    return id_personas_recomendadas
