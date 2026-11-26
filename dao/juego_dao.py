from dao.db_config import conectar
from obj.juego import Juego

def guardarJuego(pJuego):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "insert into juego (nombre, categoria, precio_dia) values (%s, %s, %s)"
    datos = (pJuego.Nombre, pJuego.Categoria, pJuego.PrecioDia)
    cursor.execute(sql, datos)
    juegoId = cursor.lastrowid
    conexion.commit()
    cursor.close()
    conexion.close()
    return juegoId

def traerJuegos():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("select id_juego, nombre, categoria, precio_dia from juego")
    filas = cursor.fetchall()
    lista = []
    for fila in filas:
        jue = Juego(fila[1], fila[2], fila[3], fila[0])
        lista.append(jue)
    cursor.close()
    conexion.close()
    return lista

def traerJuego(pId):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("select id_juego, nombre, categoria, precio_dia from juego where id_juego = %s", (pId,))
    fila = cursor.fetchone()
    if fila != None:
        jue = Juego(fila[1], fila[2], fila[3], fila[0])
    else:
        jue = None
    cursor.close()
    conexion.close()
    return jue

def modificarJuego(pJuego):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "update juego set nombre = %s, categoria = %s, precio_dia = %s where id_juego = %s"
    datos = (pJuego.Nombre, pJuego.Categoria, pJuego.PrecioDia, pJuego.IdJuego)
    cursor.execute(sql, datos)
    conexion.commit()
    cursor.close()
    conexion.close()

def borrarJuego(pId):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("delete from juego where id_juego = %s", (pId,))
        conexion.commit()
        borrado = True
    except Exception:
        borrado = False
    cursor.close()
    conexion.close()
    return borrado
