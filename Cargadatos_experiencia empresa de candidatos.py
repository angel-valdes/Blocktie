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

lista_empresas = []
datatable2 = datatable.copy()

def limpiar(empresa):
    empresa = empresa.replace("\n", "")
    empresa = empresa.replace("Contrato de Prácticas", "")
    empresa = empresa.replace("contrato temporal", "")
    empresa = empresa.replace("Jornada parcial", "")
    empresa = empresa.replace("jornada completa", "")
    empresa = empresa.replace("Contrato: de formación", "")
    empresa = empresa.replace("Independiente profesional", "")
    empresa = empresa.replace("Autónomo", "")
    empresa = empresa.strip()
    return empresa

for index, row in datatable2.iterrows():
    empresa1 = row.empresa_exp1
    empresa1 = limpiar(empresa1)

    empresa2 = row.empresa_exp2
    empresa2 = limpiar(empresa2)

    empresa3 = row.empresa_exp3
    empresa3 = limpiar(empresa3)

    empresa4 = row.empresa_exp4
    empresa4 = limpiar(empresa4)

    lista_empresas.append(empresa1)
    lista_empresas.append(empresa2)
    lista_empresas.append(empresa3)
    lista_empresas.append(empresa4)

lista_empresas = set(lista_empresas)

lista_empresas = [item for item in lista_empresas if len(item)>0]
lista_empresas.remove('Falabella')
lista_empresas.remove('CMPC')
lista_empresas.remove('Consorcio')

for empresa in lista_empresas:
    cur.execute("""INSERT INTO empresa (nombre) VALUES (%s)""", (empresa,))
mydb.commit()


