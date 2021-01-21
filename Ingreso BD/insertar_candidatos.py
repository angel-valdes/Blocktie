import pandas as pd
import mysql.connector

mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="blocktiedb")
cur = mydb.cursor()

NombreArchivo = "Datoscandidatos_excel.xlsx"

datatable = pd.read_excel(NombreArchivo)

datatable.columns = ['link', 'nombre', 'titulo_perfil', 'locacion', 'cargo_exp1', 'empresa_exp1', 'fecha_exp1', 'duracion_exp1', 'duracion_exp1_años', 'cargo_exp2', 'empresa_exp2', 'fecha_exp2', 'duracion_exp2', 'duracion_exp2_años', 'cargo_exp3', 'empresa_exp3', 'fecha_exp3', 'duracion_exp3', 'duracion_exp3_años', 'cargo_exp4', 'empresa_exp4', 'fecha_exp4', 'duracion_exp4', 'duracion_exp4_años', 'experiencia_total', 'entidad_educativa1', 'educacion1', 'especialidad1', 'entidad_educativa2', 'educacion2', 'especialidad2', 'entidad_educativa3', 'educacion3', 'especialidad3']
datatable = datatable.fillna('-')
def insertar_exp_lab(id_per, id_emp, cargo, periodo, duracion, duracion_años):
    cur.execute('INSERT INTO experiencia_laboral (id_persona, id_empresa, cargo, periodo, duracion, duracion_años) VALUES (%s, %s, %s, %s, %s, %s)',
                (id_per, id_emp, cargo, periodo, duracion, duracion_años))

def insertar_certificado(id_per, id_inst, edu, especialidad):
    cur.execute('INSERT INTO certificado (id_persona_candidato, id_institucion, titulo, menciones) VALUES (%s, %s, %s, %s)',
                (id_per, id_inst, edu, especialidad))

def limpiar(empresa):
    empresa = empresa.replace("\n", "")
    empresa = empresa.replace("Contrato de Prácticas", "")
    empresa = empresa.replace("contrato temporal", "")
    empresa = empresa.replace("Jornada parcial", "")
    empresa = empresa.replace("jornada completa", "")
    empresa = empresa.replace("Contrato: de formación", "")
    empresa = empresa.replace("Independiente profesional", "")
    empresa = empresa.replace("Autónomo", "")
    empresa = empresa.replace("Nombre de la Empresa", "")
    empresa = empresa.strip()
    return empresa
cont = 0
for index, row in datatable.iterrows():
    cur.execute('INSERT INTO persona (nombre, dirección) VALUES (%s, %s)', (row.nombre, row.locacion))
    id_persona = cur.lastrowid
    mydb.commit()

    cur.execute('INSERT INTO candidato (id_persona, titulo_perfil, experiencia_laboral) VALUES (%s, %s, %s)',
                (id_persona, row.titulo_perfil, row.experiencia_total))
    mydb.commit()
    # 4 experiencias laborales y 3 educativas

    # experiencia laboral
    lista_exp_lab = [(limpiar(row.empresa_exp1), limpiar(row.cargo_exp1), row.fecha_exp1, row.duracion_exp1, row.duracion_exp1_años),
                     (limpiar(row.empresa_exp2), limpiar(row.cargo_exp2), row.fecha_exp2, row.duracion_exp2, row.duracion_exp2_años),
                     (limpiar(row.empresa_exp3), limpiar(row.cargo_exp3), row.fecha_exp3, row.duracion_exp3, row.duracion_exp3_años),
                     (limpiar(row.empresa_exp4), limpiar(row.cargo_exp4), row.fecha_exp4, row.duracion_exp4, row.duracion_exp4_años)]
    for i in lista_exp_lab:
        if i[0] == '-' and i[1] == '-':
            break
        cur.execute('SELECT id FROM empresa WHERE nombre = %s', (i[0],))
        id_empresa = cur.fetchall()
        if i[0] == '':
            id_empresa = [(386,)]
        cur.execute('INSERT INTO experiencia_laboral (id_persona, id_empresa, cargo, periodo, duracion, duracion_años) VALUES (%s, %s, %s, %s, %s, %s)',
                    (id_persona, id_empresa[0][0], i[1], i[2], i[3], i[4]))
        mydb.commit()
    # certificados
    lista_certificados = [(row.entidad_educativa1, row.educacion1, row.especialidad1),
                          (row.entidad_educativa2, row.educacion2, row.especialidad2),
                          (row.entidad_educativa3, row.educacion3, row.especialidad3)]
    for i in lista_certificados:
        if i[0] == '-' and i[1] == '-' and i[2] == '-':
            break
        cur.execute('SELECT id FROM institucion WHERE nombre = %s', (i[0],))
        id_institucion = cur.fetchall()
        cur.execute('INSERT INTO certificado (id_persona_candidato, id_institucion, titulo, menciones) VALUES (%s, %s, %s, %s)',
                    (id_persona, id_institucion[0][0], i[1], i[2]))
        mydb.commit()
    cont += 1

