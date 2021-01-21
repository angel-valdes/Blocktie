import pandas as pd
import mysql.connector

NombreArchivo = "C:/Users/cotec/PycharmProjects/Datos prueba blocktie/ofertas_de_trabajo_limpio.xlsx"
datatable = pd.read_excel(NombreArchivo)
datatable.columns = ['link', 'nombre_comp', 'titulo_profesional', 'locacion', 'industria', 'funcion_laboral', 'años_de_experiencia']


mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
cur = mydb.cursor()

def del_nan(req):
    nada = ''
    if req != 'nan':
        return req
    else:
        return nada

for index, row in datatable.iterrows():
    print(row.nombre_comp)
    nombre_empresa = '-' if str(row.nombre_comp) == 'nan' else row.nombre_comp
    cur.execute('INSERT INTO empresa (nombre, industria, direccion, sitio_web) VALUES (%s, %s, %s, %s)', (str(nombre_empresa), str(row.industria), str(row.locacion), str(row.link)))
    id_empresa = cur.lastrowid
    cur.execute('INSERT INTO oferta (id_empresa, area_de_trabajo, cargo_requerido, experiencia_laboral_req) VALUES (%s, %s, %s, %s)', (id_empresa, str(row.funcion_laboral), str(row.titulo_profesional), str(row.años_de_experiencia)))
    mydb.commit()

cur.close()
mydb.close()