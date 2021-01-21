import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
cur = mydb.cursor()

NombreArchivo = "C:/Users/cotec/PycharmProjects/Datos prueba blocktie/Datoscandidatosfinal.xlsx"

datatable = pd.read_excel(NombreArchivo)

datatable.columns = ['link', 'nombre', 'titulo_perfil', 'locacion', 'cargo_exp1', 'empresa_exp1', 'fecha_exp1', 'duracion_exp1', 'duracion_exp1_años', 'cargo_exp2', 'empresa_exp2', 'fecha_exp2', 'duracion_exp2', 'duracion_exp2_años', 'cargo_exp3', 'empresa_exp3', 'fecha_exp3', 'duracion_exp3', 'duracion_exp3_años', 'cargo_exp4', 'empresa_exp4', 'fecha_exp4', 'duracion_exp4', 'duracion_exp4_años', 'experiencia_total', 'entidad_educativa1', 'educacion1', 'especilidad1', 'entidad_educativa2', 'educacion2', 'especilidad2', 'entidad_educativa3', 'educacion3', 'especilidad3']

lista_instituciones = []
for index, row in datatable.iterrows():
    lista_instituciones.append(row.entidad_educativa1)
    lista_instituciones.append(row.entidad_educativa2)
    lista_instituciones.append(row.entidad_educativa3)
lista_instituciones = set(lista_instituciones)

for institucion in lista_instituciones:
    print(institucion)
    cur.execute("""INSERT INTO institucion (nombre) VALUES (%s)""", (institucion,))
mydb.commit()