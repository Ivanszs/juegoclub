from dao.db_config import conectar
from dao.cliente_dao import traerCliente
from dao.juego_dao import traerJuego
from obj.alquiler import Alquiler

def guardarAlquiler(pAlquiler):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "insert into alquiler (id_cliente, id_juego, dias) values (%s, %s, %s)"
    datos = (pAlquiler.Cliente.IdCliente, pAlquiler.Juego.IdJuego, pAlquiler.Dias)
    cursor.execute(sql, datos)
    alquilerId = cursor.lastrowid
    conexion.commit()
    cursor.close()
    conexion.close()
    return alquilerId

def traerAlquileres():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("select id_alquiler, id_cliente, id_juego, dias from alquiler")
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()
    lista = []
    for fila in filas:
        cli = traerCliente(fila[1])
        jue = traerJuego(fila[2])
        alq = Alquiler(cli, jue, fila[3], fila[0])
        lista.append(alq)
    return lista

def traerAlquiler(pId):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("select id_alquiler, id_cliente, id_juego, dias from alquiler where id_alquiler = %s", (pId,))
    fila = cursor.fetchone()
    cursor.close()
    conexion.close()
    if fila != None:
        cli = traerCliente(fila[1])
        jue = traerJuego(fila[2])
        alq = Alquiler(cli, jue, fila[3], fila[0])
    else:
        alq = None
    return alq

def modificarAlquiler(pAlquiler):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "update alquiler set id_cliente = %s, id_juego = %s, dias = %s where id_alquiler = %s"
    datos = (pAlquiler.Cliente.IdCliente, pAlquiler.Juego.IdJuego, pAlquiler.Dias, pAlquiler.IdAlquiler)
    cursor.execute(sql, datos)
    conexion.commit()
    cursor.close()
    conexion.close()

def borrarAlquiler(pId):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("delete from alquiler where id_alquiler = %s", (pId,))
    conexion.commit()
    cursor.close()
    conexion.close()
