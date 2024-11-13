#archivo para conectar a base de datos
import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'universidad',
    port = 3306
)


def consultar_carreras():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera;')
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila[1])

def consultar_carreraxcodigo():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera WHERE codigo="COMP_01";')
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila[1])

def actualizar_carreaxcodigo():
    cursor = conn.cursor()
    cursor.execute("UPDATE carrera SET nombre = 'ING. COMPUTACION' WHERE codigo = 'COMP_01';")
    conn.commit()

def insertar_carrera():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO carrera(codigo, nombre, modalidad_id) values('COMP_02', 'ING SOFTWARE', 2);")
    conn.commit()
    

def eliminar_carreraxid():
    cursor = conn.cursor()
    cursor.execute("DELETE FROM carrera WHERE id = 3")
    conn.commit()

def consultar_cantidadregistros():
    cursor = conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM carrera;')
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila[0])

#consultar_carreras()
#consultar_carreraxcodigo()
#actualizar_carreaxcodigo()
#insertar_carrera()
#eliminar_carreraxid()
consultar_cantidadregistros()

conn.close()