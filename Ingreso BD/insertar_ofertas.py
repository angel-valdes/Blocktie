import pandas as pd
import mysql.connector

datatable = pd.read_csv('ofertas.csv')
datatable = datatable[['JobPostUrl', 'CompanyName', 'JobTitle', 'JobLocation', 'Industry', 'JobFunction']]
datatable.columns = ['link', 'nombre_comp', 'titulo_profesional', 'locacion', 'industria', 'funcion_laboral']
datatable = datatable.fillna('-')
mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb4")
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
    cur.execute('INSERT INTO empresa (nombre, industria, direccion) VALUES (%s, %s, %s)', (nombre_empresa, del_nan(row.industria), del_nan(row.locacion)))
    id_empresa = cur.lastrowid
    cur.execute('INSERT INTO oferta (id_empresa, area_de_trabajo, cargo_requerido, experiencia_laboral_req) VALUES (%s, %s, %s, %s)', (id_empresa, del_nan(row.funcion_laboral), del_nan(row.titulo_profesional), 0))
    mydb.commit()

cur.close()
mydb.close()