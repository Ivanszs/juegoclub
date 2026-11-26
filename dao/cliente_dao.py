from dao.db_config import conectar
from obj.cliente import Cliente

def guardarCliente(pCliente):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "insert into cliente (nombre, apellido, dni, telefono) values (%s, %s, %s, %s)"
    datos = (pCliente.Nombre, pCliente.Apellido, pCliente.getDni(), pCliente.Telefono)
    cursor.execute(sql, datos)
    clienteId = cursor.lastrowid
    conexion.commit()
    cursor.close()
    conexion.close()
    return clienteId

def traerClientes():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("select id_cliente, nombre, apellido, dni, telefono from cliente")
    filas = cursor.fetchall()
    lista = []
    for fila in filas:
        cli = Cliente(fila[1], fila[2], fila[3], fila[4], fila[0])
        lista.append(cli)
    cursor.close()
    conexion.close()
    return lista

def traerCliente(pId):
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("select id_cliente, nombre, apellido, dni, telefono from cliente where id_cliente = %s", (pId,))
    fila = cursor.fetchone()
    if fila != None:
        cli = Cliente(fila[1], fila[2], fila[3], fila[4], fila[0])
    else:
        cli = None
    cursor.close()
    conexion.close()
    return cli

def modificarCliente(pCliente):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "update cliente set nombre = %s, apellido = %s, dni = %s, telefono = %s where id_cliente = %s"
    datos = (pCliente.Nombre, pCliente.Apellido, pCliente.getDni(), pCliente.Telefono, pCliente.IdCliente)
    cursor.execute(sql, datos)
    conexion.commit()
    cursor.close()
    conexion.close()

def borrarCliente(pId):
    conexion = conectar()
    cursor = conexion.cursor()
    try:
        cursor.execute("delete from cliente where id_cliente = %s", (pId,))
        conexion.commit()
        borrado = True
    except Exception:
        borrado = False
    cursor.close()
    conexion.close()
    return borrado
