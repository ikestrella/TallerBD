#archivo para conectar a base de datos
import pymysql

conn = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database = 'universidad',
    port = 3306
)

def consultar_modalidad():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM modalidad;')
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila[1])

def insertar_carrera():
    cursor = conn.cursor()
    cursor.execute("INSERT INTO carrera(codigo, nombre, modalidad_id) values('COMP_01', 'COMPUTACION', 1);")
    conn.commit()

def consultar_carreras():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM carrera;')
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila[0], ' - ', fila[1], ' - ', fila[2])
    

insertar_carrera()
consultar_carreras()
#consultar_modalidad()
conn.close() #cerramos conexion a base de datos