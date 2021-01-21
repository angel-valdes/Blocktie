from flask import Flask, render_template, url_for, redirect, request, session, g
import mysql.connector
import requests
import json
import pandas
import spacy
from requests.auth import HTTPBasicAuth
from datetime import datetime

nlp = spacy.load('es_core_news_md') #cargar_modelo

app = Flask(__name__)
app.secret_key = '7585515-753951852a-ravioliraviolishowmetheformuoli'

node = 'u0pa9ea7pt'  # nodo
account = '0xce323273d94650803cf40c8654251af40b52455d'  # cuenta
credential = 'u0gclpyeq3'  # usuario
""""contract_instance = '0x135f66683cad7e41ab1ad8b4cde47a1989d1a2ed'  # instancia del contrato"""
key = 'l2hh8JBMo2O_HIrEyarNg2dkTZQ98Zjd-9k5-wrTe24'  # password
base_url = 'https://u0z93so5ob-' + node + '-connect.us0-aws.kaleido.io/instances/'





"""
# Contract creation
@app.route('/make_contract', methods=['GET', 'POST'])
def make_contract():
    if request.method == 'GET':
        make_contract_url = 'https://u0nik2513u-' + node + '-connect.us0-aws.kaleido.io/gateways/egresadov2/'
        parameters = {'kld-from': account, 'kld-sync': 'true'}
        response = requests.post(make_contract_url, params=parameters, auth=HTTPBasicAuth(credential, key))
        resp_as_json = response.json()
        with open('latest_contract_info.json', 'w') as outfile:
            json.dump(resp_as_json, outfile)
        print(resp_as_json)
        return resp_as_json
    else:
        return render_template('index.html')


# Retrieve functions
@app.route('/retrieve_name')
def retrieve_name():
    retrieve_url = base_url + '/retrieve_nombre'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    print(response.text)
    print(response.json())
    return redirect('/')


@app.route('/retrieve_lastname')
def retrieve_lastname():
    retrieve_url = base_url + 'retrieve_apellido'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    print(response.text)
    print(response.json())
    return redirect('/')


@app.route('/retrieve_degree')
def retrieve_degree():
    retrieve_url = base_url + '/retrieve_titulo'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    print(response.text)
    print(response.json())
    return redirect('/')


@app.route('/retrieve_minor')
def retrieve_minor():
    retrieve_url = base_url + '/retrieve_mencion'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    print(response.text)
    print(response.json())
    return redirect('/')


@app.route('/retrieve_school')
def retrieve_school():
    retrieve_url = base_url + '/retrieve_universidad'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    print(response.text)
    print(response.json())
    return redirect('/')


@app.route('/retrieve_graduation')
def retrieve_graduation():
    retrieve_url = base_url + '/retrieve_fecha_de_egreso'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    print(response.text)
    print(response.json())
    return redirect('/')


@app.route('/retrieve_phone')
def retrieve_phone():
    retrieve_url = base_url + '/retrieve_numero_telefonico'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    print(response.text)
    print(response.json())
    return redirect('/')


@app.route('/retrieve_extras')
def retrieve_extras():
    retrieve_url = base_url + 'retrieve_extras'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    print(response.text)
    print(response.json())
    return redirect('/')


# Store functions
@app.route('/store_name', methods=['POST', 'GET'])
def store_name():
    if request.method == 'POST':
        name_content = request.form['content']
        new_name = Todo(content=name_content)
        store_url = base_url + '/store_nombre'
        body = {"nom": name_content}
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(response.json())
        try:
            db.session.add(new_name)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding your name'
    else:
        return render_template('store_name.html')
    #store_url = base_url + '/store_name'
    #body = {"nom": name_content}
    #parameters = {'kld-from': account}
    #response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
    #print(response.json())
    #Name_content = request.form['fname']
    #body = {"nom": Name_content}
    #return render_template('index.html')


@app.route('/store_lastname', methods=['POST', 'GET'])
def store_lastname():
    if request.method == 'POST':
        lastname_content = request.form['content']
        new_lastname = Todo(content=lastname_content)
        store_url = base_url + '/store_apellido'
        body = {"ape": lastname_content}
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(response.json())
        try:
            db.session.add(new_lastname)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding your lastname'
    else:
        return render_template('store_lastname.html')
    #store_url = base_url + '/store_apellido'
    #body = {"ape": lastname_content}
    #parameters = {'kld-from': account}
    #response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
    #print(response.json())
    #return redirect('/')


@app.route('/store_degree', methods=['POST', 'GET'])
def store_degree():
    #store_url = base_url + '/store_titulo'
    #body = {"tit": 'Artista'}
    #parameters = {'kld-from': account}
    #response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
    #print(response.json())
    #return redirect('/')
    if request.method == 'POST':
        degree_content = request.form['content']
        new_degree = Todo(content=degree_content)
        store_url = base_url + '/store_titulo'
        body = {"tit": degree_content}
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(response.json())
        try:
            db.session.add(new_degree)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding your degree'
    else:
        return render_template('store_degree.html')



@app.route('/store_minor')
def store_minor():
    # store_url = base_url + '/store_mencion'
    # body = {"men": 'N/A'}
    # parameters = {'kld-from': account}
    # response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
    # print(response.json())
    # return redirect('/')
    if request.method == 'POST':
        minor_content = request.form['content']
        new_minor = Todo(content=minor_content)
        print(minor_content)
        store_url = base_url + '/store_mencion'
        body = {"men": minor_content}
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(response.json())
        try:
            db.session.add(new_minor)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding your minor'
    else:
        return render_template('store_minor.html')



@app.route('/store_school')
def store_school():
    if request.method == 'POST':
        school_content = request.form['content']
        new_school = Todo(content=school_content)
        store_url = base_url + '/store_universidad'
        body = {"uni": school_content}
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(response.json())
        try:
            db.session.add(new_school)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding your degree'
    else:
        return render_template('store_school.html')
    #store_url = base_url + '/store_universidad'
    #body = {"uni": 'N/A'}
    #parameters = {'kld-from': account}
    #response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
    #print(response.json())
    #return redirect('/')


@app.route('/store_graduation')
def store_graduation():
    if request.method == 'POST':
        graduation_content = request.form['content']
        new_graduation = Todo(content=graduation_content)
        store_url = base_url + '/store_fecha_de_egreso'
        body = {"fec": graduation_content}
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(response.json())
        try:
            db.session.add(new_graduation)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding your name'
    else:
        return render_template('store_graduation.html')
    #store_url = base_url + '/store_fecha_de_egreso'
    #body = {"fec": 'N/A'}
    #parameters = {'kld-from': account}
    #response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
    #print(response.json())
    #return redirect('/')


@app.route('/store_phone')
def store_phone():
    if request.method == 'POST':
        phone_content = request.form['content']
        new_phone = Todo(content=phone_content)
        store_url = base_url + '/store_numero_telefonico'
        body = {"num": phone_content}
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(response.json())
        try:
            db.session.add(new_phone)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding your phone'
    else:
        return render_template('store_phone.html')
    #store_url = base_url + '/store_numero_telefonico'
    #body = {"num": '11111111'}
    #parameters = {'kld-from': account}
    #response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
    #print(response.json())
    #return redirect('/')


@app.route('/store_extras')
def store_extras():
    if request.method == 'POST':
        extra_content = request.form['content']
        new_extra = Todo(content=extra_content)
        store_url = base_url + '/store_extras'
        body = {"ext": extra_content}
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(response.json())
        try:
            db.session.add(new_extra)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem adding your phone'
    else:
        return render_template('store_extras.html')
    #store_url = base_url + '/store_extras'
    #body = {"ext": 'EXTRA INFO'}
    #parameters = {'kld-from': account}
    #response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
    #print(response.json())
    #return redirect('/')
"""  # Old Single-target Routes
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


def store_full(nom, ape, uni, tit, men, eda, tel, fec, ext, ci,nodo):
        base_url = 'https://u0z93so5ob-' + nodo + '-connect.us0-aws.kaleido.io/instances/'
        store_url = base_url + ci + '/store_full'
        body = {
  "ape": ape,
  "eda": eda,
  "ext": ext,
  "fec": fec,
  "men": men,
  "nom": nom,
  "tel": tel,
  "tit": tit,
  "uni": uni
        }
        parameters = {'kld-from': account}
        response = requests.post(store_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        return (response.json())
    


def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def make_contract(nodo):  
        make_contract_url = 'https://u0z93so5ob-' + nodo + '-connect.us0-aws.kaleido.io/gateways/egresadov3/'
        parameters = {'kld-from': account, 'kld-sync': 'true'}
        response = requests.post(make_contract_url, params=parameters, auth=HTTPBasicAuth(credential, key))
        resp_as_text = response.text
        contract_id = find_between(resp_as_text, 'contractAddress": "', '"')
        return (contract_id)

def retrieve_name(ci):
    retrieve_url = base_url + ci + '/retrieve_nombre'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    return response.text



def retrieve_lastname(ci):
    retrieve_url = base_url + ci + 'retrieve_apellido'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    return response.text



def retrieve_degree(ci):
    retrieve_url = base_url + ci + '/retrieve_titulo'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    x = response.text
    y = x.split("\"")[3]
    return y



def retrieve_minor(ci):
    retrieve_url = base_url + ci + '/retrieve_mencion'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    x = response.text
    y = x.split("\"")[3]
    return y



def retrieve_school(ci):
    retrieve_url = base_url + ci + '/retrieve_universidad'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    x = response.text
    y = x.split("\"")[3]
    return y



def retrieve_graduation(ci):
    retrieve_url = base_url + ci + '/retrieve_fecha_de_egreso'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    return response.text



def retrieve_phone(ci):
    retrieve_url = base_url + ci + '/retrieve_numero_telefonico'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    return response.text



def retrieve_extras(ci):
    retrieve_url = base_url + ci + '/retrieve_extras'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    return response.text

def retrieve_fecha_egreso(ci):
    retrieve_url = base_url + ci + '/retrieve_fecha_egreso'
    parameters = {'kld-from': account}
    response = requests.get(retrieve_url, params=parameters, auth=HTTPBasicAuth(credential, key))
    x = response.text
    y = x.split("\"")[3]
    return y


@app.before_request
def before_request():
    if 'user_id' in session:
        g.user = session['user_id']
        
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor(buffered=True)
        # search by author or book
        mycursor.execute("SELECT id FROM persona INNER JOIN candidato ON persona.id = candidato.id_persona WHERE persona.email = '"+username+"' and persona.contraseña = '"+password+"' ")
        data = mycursor.fetchall()
        if (data != 0):
            print(data[0])
            print(data[0][0])
            session['user_id'] = data[0][0]
            return redirect(url_for('home'))
        else:
            return redirect(url_for('index'))
    else:
        return render_template('index2.html')
    
@app.route('/login_reclutador', methods=['POST', 'GET'])
def login_reclutador():
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor(buffered=True)
        # search by author or book
        mycursor.execute("SELECT id FROM persona INNER JOIN reclutador ON persona.id = reclutador.id_persona WHERE persona.email = '"+username+"' and persona.contraseña = '"+password+"' ")
        data = mycursor.fetchall()
        if (data != 0):
            session['user_id'] = data[0][0]
            return redirect(url_for('home2'))
    else:
        return render_template('index3.html')




@app.route('/home2', methods=['POST', 'GET'])
def home2():
    if request.method == 'GET':
        read_instance = str(g.user)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blocktiedb")
        mycursor = mydb.cursor()
        mycursor.execute('SELECT oferta.id, empresa.nombre, oferta.fecha_publicacion, oferta.area_de_trabajo, oferta.cargo_requerido FROM empresa INNER JOIN oferta ON empresa.id = oferta.id_empresa WHERE id_persona_reclutador = "'+ read_instance +'"')
        data = mycursor.fetchall()
        return render_template('home2_pre_oferta.html', userdata = data)
    if request.method == 'POST':
        id_oferta = request.form['id_oferta']
        datalist = recomendador_reclutador(id_oferta)
        print(datalist)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="blocktiedb")
        mycursor = mydb.cursor()
        lista_limpia = []
        for can in datalist:
            mycursor.execute('SELECT persona.nombre, persona.email, persona.sexo, candidato.aptitudes, candidato.logros, certificado.titulo, certificado.menciones FROM persona, candidato, certificado WHERE persona.id = candidato.id_persona AND persona.id = certificado.id_persona_candidato AND persona.id = {}'.format(can))
            lista_candidato = mycursor.fetchall()
            print(lista_candidato)
            lista_limpia2 = []
            lista_limpia2.append(can)
            lista_limpia2.append(lista_candidato[0][0])
            lista_limpia2.append(lista_candidato[0][1])
            lista_limpia2.append(lista_candidato[0][2])
            lista_limpia2.append(lista_candidato[0][3])
            lista_limpia2.append(lista_candidato[0][4])
            for i in lista_candidato:
                lista_limpia2.append(i[5])
                lista_limpia2.append(i[6])
    
            lista_limpia.append(lista_limpia2)
                
    
        print(lista_limpia)
    
        return render_template('home2.html', userdata=lista_limpia)

@app.route('/home', methods=['POST', 'GET'])
def home():
    datalist = recomendador_candidato(str(g.user))
    return render_template('home.html', userdata=datalist)


@app.route('/display_oferta', methods=['POST', 'GET'])
def display_oferta():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor()

        id_tarjeta = request.form['id_tarjeta']
        id_tarjeta = int(id_tarjeta)
        mycursor.execute('SELECT persona.nombre, persona.email, persona.sexo, candidato.aptitudes, candidato.logros, certificado.titulo, certificado.menciones FROM persona, candidato, certificado WHERE persona.id = candidato.id_persona AND persona.id = certificado.id_persona_candidato AND persona.id = {}'.format(id_tarjeta))
        lista_candidato = mycursor.fetchall()
        print(lista_candidato)
        lista_limpia2 = []
        lista_limpia2.append(lista_candidato[0][0])
        lista_limpia2.append(lista_candidato[0][1])
        lista_limpia2.append(lista_candidato[0][2])
        lista_limpia2.append(lista_candidato[0][3])
        lista_limpia2.append(lista_candidato[0][4])
        for i in lista_candidato:
            lista_limpia2.append(i[5])
            lista_limpia2.append(i[6])
        try:
            lista_limpia2.remove('-')
        except:
            print("no guion")
        return render_template('display_oferta.html', userdata=lista_limpia2)

@app.route('/display_candidato', methods=['POST', 'GET'])
def display_candidato():
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor()

        id_tarjeta = request.form['id_tarjeta']
        id_tarjeta = int(id_tarjeta)
        mycursor.execute(" SELECT empresa.nombre, oferta.cargo_requerido, empresa.industria, oferta.fecha_publicacion, oferta.descripcion, oferta.area_de_trabajo, oferta.jornada, oferta.sueldo, oferta.beneficios, oferta.carrera_requerida, oferta.experiencia_laboral_req, oferta.idiomas_req, oferta.otros_req FROM empresa, oferta WHERE empresa.id = oferta.id_empresa AND oferta.id = %s", (id_tarjeta,))
        myresult = mycursor.fetchall()
        return render_template('display_candidato.html', userdata=myresult)


@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        firstname = request.form['firstname']  # nombre
        lastname = request.form['lastname']  # apellido
        degree = request.form['degree']  # título
        minor = request.form['minor']  # minor
        phone = request.form['phone']  # teléfono
        school = request.form['school']  # universidad
        extras = request.form['extras']  # extras (info adicional)
        age = request.form['age']  # edad
        graduation = request.form['graduation']

        make_contract_url = 'https://u0z93so5ob-' + node + '-connect.us0-aws.kaleido.io/gateways/u0f6ugp9l8/'
        parameters = {'kld-from': account, 'kld-sync': 'true'}
        creation_response = requests.post(make_contract_url, params=parameters, auth=HTTPBasicAuth(credential, key))
        creation_json = creation_response.json()
        contract_addr = creation_json['contractAddress']  # unsure if this is how we should parse the data here

        # To do: send data to kaleido with the received new contract address
        update_url = 'https://u0z93so5ob-' + node + '-connect.us0-aws.kaleido.io/instances/' + contract_addr + '/store_full'
        body = {"nom": firstname,
                "ape": lastname,
                "tit": degree,
                "men": minor,
                "uni": school,
                "fec": graduation,
                "eda": age,
                "tel": phone,
                "ext": extras}
        parameters = {'kld-from': account}
        update_response = requests.post(update_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(f"Kaleido Response: {update_response}")

        return render_template('home.html')
    else:
        return render_template('create.html')


@app.route('/favorite_ofertas', methods=['POST', 'GET'])
def read():
    if request.method == 'GET':
        read_instance = str(g.user)
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT empresa.nombre as nombre_empresa, persona.nombre as nombre_reclutador, oferta.cargo_requerido as cargo_requerido, oferta.fecha_publicacion as fecha_publicacion, oferta.descripcion as descripcion, oferta.area_de_trabajo as area_de_trabajo, oferta.jornada as jornada, oferta.sueldo as sueldo, oferta.beneficios as beneficios, oferta.carrera_requerida as carrera_requerida, oferta.experiencia_laboral_req as experiencia_laboral_req, oferta.idiomas_req as idiomas_req, oferta.otros_req as otros_req, oferta.id as id_oferta FROM oferta INNER JOIN empresa ON oferta.id_empresa = empresa.id INNER JOIN persona ON persona.id = oferta.id_persona_reclutador INNER JOIN candidato_interesado_en_oferta x ON x.id_oferta = oferta.id WHERE x.id_candidato_persona = '"+ read_instance +"'")  
        myresult = mycursor.fetchall()
        print(myresult)
        return render_template('candidato_ver_ofertas.html', userdata=myresult)


@app.route('/edit', methods=['POST', 'GET'])
def edit():
    if request.method == 'POST':
        read_instance = request.form['contractInstance']
        read_url = 'https://u0z93so5ob-' + node + '-connect.us0-aws.kaleido.io/instances/' + read_instance + '/retrieve_full'
        parameters = {'kld-from': account}
        read_response = requests.get(read_url, params=parameters, auth=HTTPBasicAuth(credential, key))
        prepload = json.loads(read_response.text)
        aux = prepload['output']
        some_list = aux.split(", ")
        comma_separated = ','.join(some_list)
        print(comma_separated)
        return redirect(url_for('show_edit', some_list=comma_separated))
    else:
        return render_template('edit.html')
@app.route('/Edit_contract', methods=['POST', 'GET'])
def show_edit():
    if request.method == 'POST':
        print('entre')
        contact_instance = request.form['contract_instance']
        firstname = request.form['firstname']  # nombre
        lastname = request.form['lastname']  # apellido
        degree = request.form['degree']  # título
        minor = request.form['minor']  # minor
        phone = request.form['phone']  # teléfono
        school = request.form['school']  # universidad
        extras = request.form['extras']  # extras (info adicional)
        age = request.form['age']  # edad
        graduation = request.form['graduation']
        update_url = 'https://u0z93so5ob-' + node + '-connect.us0-aws.kaleido.io/instances/' + contact_instance + '/store_full'
        body = {"nom": firstname,
                "ape": lastname,
                "tit": degree,
                "men": minor,
                "uni": school,
                "fec": graduation,
                "eda": age,
                "tel": phone,
                "ext": extras}
        parameters = {'kld-from': account}
        update_response = requests.post(update_url, data=body, params=parameters, auth=HTTPBasicAuth(credential, key))
        print(f"Kaleido Response: {update_response}")
        return render_template('home.html')
    else:
        return render_template('Edit_contract.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        oferta = request.form['oferta']
        print(oferta)
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor(buffered=True)
        
        mycursor.execute("SELECT empresa.nombre as nombre_empresa, persona.nombre as nombre_reclutador, persona.apellido as apellido_reclutador, oferta.cargo_requerido as cargo_requerido, oferta.fecha_publicacion as fecha_publicacion, oferta.descripcion as descripcion, oferta.area_de_trabajo as area_de_trabajo, oferta.jornada as jornada, oferta.sueldo as sueldo, oferta.beneficios as beneficios, oferta.carrera_requerida as carrera_requerida, oferta.experiencia_laboral_req as experiencia_laboral_req, oferta.idiomas_req as idiomas_req, oferta.otros_req as otros_req, oferta.id as id_oferta FROM oferta INNER JOIN empresa ON oferta.id_empresa = empresa.id INNER JOIN persona ON persona.id = oferta.id_persona_reclutador WHERE empresa.nombre LIKE '%"+ oferta + "%' OR oferta.descripcion LIKE '%"+ oferta +"%'")
        mydb.commit()
        data = mycursor.fetchall()
        print(data)
        
        if len(data) == 0 and oferta == 'all': 
            mycursor.execute("SELECT empresa.nombre as nombre_empresa, persona.nombre as nombre_reclutador, persona.apellido as apellido_reclutador, oferta.cargo_requerido as cargo_requerido, oferta.fecha_publicacion as fecha_publicacion, oferta.descripcion as descripcion, oferta.area_de_trabajo as area_de_trabajo, oferta.jornada as jornada, oferta.sueldo as sueldo, oferta.beneficios as beneficios, oferta.carrera_requerida as carrera_requerida, oferta.experiencia_laboral_req as experiencia_laboral_req, oferta.idiomas_req as idiomas_req, oferta.otros_req as otros_req FROM oferta INNER JOIN empresa ON oferta.id_empresa = empresa.id INNER JOIN persona ON persona.id = oferta.id_persona_reclutador")
            mydb.commit()
            data = mycursor.fetchall()
            print(data)
        return render_template('search_mysql.html', data=data)
    return render_template('search_mysql.html')

@app.route('/add_oferta', methods=['GET', 'POST'])
def add_oferta():
    if request.method == "GET":
        id = request.args.get('id')
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor(buffered=True)
       
        mycursor.execute("SELECT id_candidato_persona, id_oferta FROM candidato_interesado_en_oferta WHERE id_candidato_persona = '"+str(g.user)+"' AND id_oferta = '"+id+"'")
        data = mycursor.fetchall()
        print(data)
        if len(data) == 0 :
            mycursor.execute("INSERT INTO candidato_interesado_en_oferta (id_candidato_persona, id_oferta, permitir_visibilidad) VALUES ('"+str(g.user)+"','"+id+"',1)")
            mydb.commit()
        return redirect(url_for('search'))
@app.route('/delete_oferta', methods=['GET', 'POST'])
def delete_oferta():
    if request.method == "GET":
        id = request.args.get('id')
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor(buffered=True)
        
        mycursor.execute("SELECT id_candidato_persona, id_oferta FROM candidato_interesado_en_oferta WHERE id_candidato_persona = '"+str(g.user)+"' AND id_oferta = '"+id+"'")
        data = mycursor.fetchall()
        print(data)
        if len(data) != 0 :
            mycursor.execute("DELETE FROM candidato_interesado_en_oferta WHERE id_candidato_persona = '"+str(g.user)+"' AND id_oferta = '"+id+"'")
            mydb.commit()
        return redirect(url_for('read'))
    
@app.route('/profile_candidato', methods=['POST', 'GET'])
def profile_candidato():
    if request.method == 'GET':

        read_instance = g.user

        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        cur = mydb.cursor(buffered=True)
        cur.execute('SELECT persona.nombre, persona.apellido, persona.contraseña, persona.telefono, persona.nacimiento, persona.email, persona.dirección, persona.sexo, candidato.universidad, candidato.aptitudes, candidato.logros, candidato.experiencia_laboral, candidato.extra, certificado.titulo, certificado.menciones FROM persona INNER JOIN candidato ON persona.id = candidato.id_persona INNER JOIN certificado ON persona.id = certificado.id_persona_candidato WHERE persona.id = %s', (read_instance,))
        myresult_id = cur.fetchall()
        print(myresult_id)
        aux = []
        for x in myresult_id:
            aux.append(x)


        datalist = aux

        return render_template('profile_candidato.html', data=datalist[0])
    if request.method == 'POST':
        read_instance = g.user
        
        firstname = request.form['firstname']  # nombre
        lastname = request.form['lastname']  # apellido
        password = request.form['pass']
        university = request.form['university']  
        apt = request.form['apt']  
        achievements = request.form['ach']  
        exp = request.form['exp']  
        extra = request.form['extra']
        degree = request.form['degree']  # título
        minor = request.form['minor']  # minor
        phone = request.form['phone']  # teléfono
        birth = request.form['birth']  # edad
        adress = request.form['adress']
        sex = request.form['sex']
        mail = request.form['email']
        
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        cur = mydb.cursor(buffered=True)
        cur.execute("UPDATE persona INNER JOIN candidato ON persona.id = candidato.id_persona INNER JOIN certificado ON persona.id = certificado.id_persona_candidato SET persona.nombre = %s, persona.apellido = %s, persona.contraseña = %s, candidato.universidad = %s, candidato.aptitudes = %s, candidato.logros = %s, candidato.experiencia_laboral = %s, candidato.extra = %s, certificado.titulo = %s, certificado.menciones = %s, persona.telefono = %s, persona.nacimiento = %s, persona.dirección = %s, persona.sexo = %s, persona.email = %s WHERE persona.id = %s", (firstname, lastname, password, university, apt, achievements, exp, extra, degree, minor, phone, birth, adress, sex, mail, read_instance))
        mydb.commit()
        return redirect(url_for('home'))
@app.route('/sign_up_candidato', methods=['POST', 'GET'])
def sign_up_candidato():
    if request.method == 'POST':
        firstname = request.form['firstname']  # nombre
        lastname = request.form['lastname']  # apellido
        password = request.form['pass']
        university = request.form['university']  
        apt = request.form['apt']  
        achievements = request.form['ach']  
        exp = request.form['exp']  
        extra = request.form['extra']
        degree = request.form['degree']  # título
        minor = request.form['minor']  # minor
        phone = request.form['phone']  # teléfono
        birth = request.form['birth']  # edad
        adress = request.form['adress']
        sex = request.form['sex']
        mail = request.form['email']
        
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        cur = mydb.cursor(buffered=True)
        
        results = cur.execute("INSERT INTO persona (nombre, apellido, contraseña, telefono, nacimiento, email, dirección, sexo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); SET @aux = LAST_INSERT_ID(); INSERT INTO candidato (id_persona, universidad, aptitudes, logros, experiencia_laboral, extra) VALUES (@aux, %s, %s, %s, %s, %s); INSERT INTO certificado (id_persona_candidato, titulo, menciones) VALUES (@aux, %s, %s)", (firstname, lastname, password, phone, birth, mail, adress, sex, university, apt, achievements, exp, extra, degree, minor), multi=True)
        for i in results:
            pass
        mydb.commit()
        
        return render_template('index.html')
    else:
        return render_template('sign_up_candidato.html')
    
    
@app.route('/sign_up_reclutador', methods=['POST', 'GET'])
def sign_up_reclutador():
    if request.method == 'POST':
        firstname = request.form['firstname']  # nombre
        lastname = request.form['lastname']  # apellido
        password = request.form['pass']
        emp = request.form['emp']  
        ind = request.form['ind']
        cargo = request.form['cargo']
        adr = request.form['adr']  
        web = request.form['web']  
        desc = request.form['desc']  
        phone = request.form['phone']  # teléfono
        birth = request.form['birth']  # edad
        adress = request.form['adress']
        sex = request.form['sex']
        mail = request.form['email']
        
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        cur = mydb.cursor(buffered=True)
        
        results = cur.execute("INSERT INTO persona (nombre, apellido, contraseña, telefono, nacimiento, email, dirección, sexo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s); SET @aux = LAST_INSERT_ID(); INSERT INTO empresa (nombre, industria, direccion, sitio_web, telefono, descripción) VALUES (%s, %s, %s, %s, %s, %s); INSERT INTO reclutador VALUES (@aux, LAST_INSERT_ID(), %s)", (firstname, lastname, password, phone, birth, mail, adress, sex, emp, ind, adr, web, phone, desc, cargo), multi=True)
        for i in results:
            pass
        mydb.commit()
        
        return render_template('index.html')
    else:
        return render_template('sign_up_reclutador.html')
    
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
        return render_template('sign_up.html')

@app.route('/create_oferta', methods=['POST', 'GET'])
def create_oferta():
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        desc = request.form['desc']
        area = request.form['area']
        cargo = request.form['cargo']
        jornada = request.form['jornada']
        sueldo = request.form['sueldo']
        beneficios = request.form['beneficios']
        carrera = request.form['carrera']
        exp = request.form['exp']
        idiomas = request.form['idiomas']
        otros = request.form['otros']
        
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("INSERT INTO oferta (id_persona_reclutador, id_empresa, fecha_publicacion, descripcion, area_de_trabajo, cargo_requerido, jornada, sueldo, beneficios, carrera_requerida, experiencia_laboral_req, idiomas_req, otros_req, disponible) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, 1)", (str(g.user), emp_id, datetime.today().strftime('%Y-%m-%d'), desc, area, cargo, jornada, sueldo, beneficios, carrera, exp, idiomas, otros))
        mydb.commit()
        return redirect(url_for('home2'))
    if request.method == 'GET':
        
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("SELECT empresa.id, empresa.nombre FROM empresa INNER JOIN reclutador ON reclutador.id_empresa = empresa.id WHERE reclutador.id_persona ="+str(g.user)+"")
        mydb.commit()
        data = mycursor.fetchall()
        return render_template('create_oferta.html', data=data)

@app.route('/get_certificado', methods=['POST', 'GET'])
def get_certificado():
    if request.method == 'POST':
        instance = request.form['contract_instance']
        
        titulo = retrieve_degree(instance)
        menciones = retrieve_minor(instance)
        fecha_titulacion = retrieve_fecha_egreso(instance)
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
        mycursor = mydb.cursor(buffered=True)
        mycursor.execute("INSERT INTO certificado VALUES (%s, %s, %s, %s, %s, %s)", (str(g.user), "12", titulo, menciones, fecha_titulacion, instance))
        mydb.commit()
        return redirect(url_for('home'))
    else:
        return render_template('get_certificado.html')
    
@app.route('/upload_certificados', methods=['POST', 'GET'])
def upload_certificados():
    if request.method == 'POST':
        print("debug1")
        file = request.files['file']
        password = request.form['password']
        print("debug2")
        data_xls = pandas.read_excel(file)
        print("debug3")
        contract_list = []
        for index, row in data_xls.iterrows():
            contract_id = make_contract(password)
            contract_list.append([contract_id, row.nombre, row.apellido])
            print(store_full(row.nombre, row.apellido, row.universidad, row.titulo, row.mencion, row.nacimiento, row.telefono, row.fecha, row.extra, contract_id, password))
        return redirect(url_for('index'))
    else:
        return render_template('upload_certificados.html')
            