import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from obj.cliente import Cliente
from obj.juego import Juego
from obj.alquiler import Alquiler
from dao.cliente_dao import guardarCliente, traerClientes, traerCliente, modificarCliente, borrarCliente
from dao.juego_dao import guardarJuego, traerJuegos, traerJuego, modificarJuego, borrarJuego
from dao.alquiler_dao import guardarAlquiler, traerAlquileres, traerAlquiler, modificarAlquiler, borrarAlquiler

def menuClientes():
    while True:
        print("\n--- Menu de Clientes ---")
        print("1. Crear Cliente")
        print("2. Listar Clientes")
        print("3. Ver Datos de un Cliente")
        print("4. Modificar Cliente")
        print("5. Borrar Cliente")
        print("6. Volver")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                print("\nNuevo Cliente")
                nombre = input("Ingrese nombre: ")
                apellido = input("Ingrese apellido: ")
                dni = input("Ingrese DNI: ")
                telefono = input("Ingrese telefono: ")

                if nombre == "" or apellido == "" or dni == "":
                    print("Error: nombre, apellido y DNI no pueden estar vacios")
                else:
                    cli = Cliente(nombre, apellido, dni, telefono)
                    nuevoId = guardarCliente(cli)
                    print("Cliente guardado con Id:", nuevoId)

            elif opcion == 2:
                clientes = traerClientes()
                print("\nLista de Clientes:")
                if len(clientes) == 0:
                    print("No hay clientes cargados")
                else:
                    for c in clientes:
                        c.mostrarDatos()
                        print("----------------")

            elif opcion == 3:
                idCli = int(input("Ingrese Id de cliente: "))
                cli = traerCliente(idCli)
                if cli == None:
                    print("No existe un cliente con ese Id")
                else:
                    print("")
                    cli.mostrarDatos()

            elif opcion == 4:
                idCli = int(input("Ingrese Id de cliente a modificar: "))
                cli = traerCliente(idCli)
                if cli == None:
                    print("No existe un cliente con ese Id")
                else:
                    print("\nDatos actuales:")
                    cli.mostrarDatos()
                    nombre = input("Ingrese nuevo nombre: ")
                    apellido = input("Ingrese nuevo apellido: ")
                    dni = input("Ingrese nuevo DNI: ")
                    telefono = input("Ingrese nuevo telefono: ")

                    if nombre == "" or apellido == "" or dni == "":
                        print("Error: nombre, apellido y DNI no pueden estar vacios")
                    else:
                        cliMod = Cliente(nombre, apellido, dni, telefono, idCli)
                        modificarCliente(cliMod)
                        print("Datos del cliente modificados")

            elif opcion == 5:
                clientes = traerClientes()
                print("\nId - Nombre - Apellido")
                for c in clientes:
                    print(c.IdCliente, "-", c.Nombre, "-", c.Apellido)

                idCli = int(input("Ingrese Id de cliente a borrar: "))
                cli = traerCliente(idCli)
                if cli == None:
                    print("No existe un cliente con ese Id")
                else:
                    borrado = borrarCliente(idCli)
                    if borrado == True:
                        print("Cliente borrado")
                    else:
                        print("No se puede borrar el cliente porque tiene alquileres registrados")

            elif opcion == 6:
                break
            else:
                print("Opcion no valida")

        except ValueError:
            print("Error: debe ingresar un numero valido")

def menuJuegos():
    while True:
        print("\n--- Menu de Juegos ---")
        print("1. Crear Juego")
        print("2. Listar Juegos")
        print("3. Ver Datos de un Juego")
        print("4. Modificar Juego")
        print("5. Borrar Juego")
        print("6. Volver")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                print("\nNuevo Juego")
                nombre = input("Ingrese nombre del juego: ")
                categoria = input("Ingrese categoria: ")
                precio = float(input("Ingrese precio por dia: "))

                if nombre == "" or categoria == "" or precio <= 0:
                    print("Error: complete los datos y un precio mayor a 0")
                else:
                    jue = Juego(nombre, categoria, precio)
                    nuevoId = guardarJuego(jue)
                    print("Juego guardado con Id:", nuevoId)

            elif opcion == 2:
                juegos = traerJuegos()
                print("\nLista de Juegos:")
                if len(juegos) == 0:
                    print("No hay juegos cargados")
                else:
                    for j in juegos:
                        j.mostrarDatos()
                        print("----------------")

            elif opcion == 3:
                idJue = int(input("Ingrese Id del juego: "))
                jue = traerJuego(idJue)
                if jue == None:
                    print("No existe un juego con ese Id")
                else:
                    print("")
                    jue.mostrarDatos()

            elif opcion == 4:
                idJue = int(input("Ingrese Id del juego a modificar: "))
                jue = traerJuego(idJue)
                if jue == None:
                    print("No existe un juego con ese Id")
                else:
                    print("\nDatos actuales:")
                    jue.mostrarDatos()
                    nombre = input("Ingrese nuevo nombre: ")
                    categoria = input("Ingrese nueva categoria: ")
                    precio = float(input("Ingrese nuevo precio por dia: "))

                    if nombre == "" or categoria == "" or precio <= 0:
                        print("Error: complete los datos y un precio mayor a 0")
                    else:
                        jueMod = Juego(nombre, categoria, precio, idJue)
                        modificarJuego(jueMod)
                        print("Datos del juego modificados")

            elif opcion == 5:
                juegos = traerJuegos()
                print("\nId - Juego - Precio")
                for j in juegos:
                    print(j.IdJuego, "-", j.Nombre, "- $", j.PrecioDia)

                idJue = int(input("Ingrese Id del juego a borrar: "))
                jue = traerJuego(idJue)
                if jue == None:
                    print("No existe un juego con ese Id")
                else:
                    borrado = borrarJuego(idJue)
                    if borrado == True:
                        print("Juego borrado")
                    else:
                        print("No se puede borrar el juego porque tiene alquileres registrados")

            elif opcion == 6:
                break
            else:
                print("Opcion no valida")

        except ValueError:
            print("Error: debe ingresar un numero valido")

def menuAlquileres():
    while True:
        print("\n--- Menu de Alquileres ---")
        print("1. Registrar Alquiler")
        print("2. Listar Alquileres")
        print("3. Ver Datos de un Alquiler")
        print("4. Modificar Alquiler")
        print("5. Borrar Alquiler")
        print("6. Volver")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                print("\nClientes disponibles:")
                for c in traerClientes():
                    print(c.IdCliente, "-", c.Nombre, c.Apellido)
                idCli = int(input("Ingrese Id del cliente: "))
                cli = traerCliente(idCli)

                print("\nJuegos disponibles:")
                for j in traerJuegos():
                    print(j.IdJuego, "-", j.Nombre, "($", j.PrecioDia, "por dia)")
                idJue = int(input("Ingrese Id del juego: "))
                jue = traerJuego(idJue)

                if cli == None or jue == None:
                    print("Error: el cliente o el juego indicado no existe")
                else:
                    dias = int(input("Ingrese cantidad de dias: "))
                    if dias <= 0:
                        print("Error: la cantidad de dias debe ser mayor a 0")
                    else:
                        alq = Alquiler(cli, jue, dias)
                        nuevoId = guardarAlquiler(alq)
                        print("Alquiler guardado con Id:", nuevoId)

                        descuento = float(input("Ingrese descuento si corresponde (0 para ninguno): "))
                        if descuento > 0:
                            print("Total a cobrar con descuento: $", alq.calcularTotal(descuento))
                        else:
                            print("Total a cobrar: $", alq.calcularTotal())

            elif opcion == 2:
                alquileres = traerAlquileres()
                print("\nLista de Alquileres:")
                if len(alquileres) == 0:
                    print("No hay alquileres cargados")
                else:
                    for a in alquileres:
                        a.mostrarDatos()
                        print("----------------")

            elif opcion == 3:
                idAlq = int(input("Ingrese Id del alquiler: "))
                alq = traerAlquiler(idAlq)
                if alq == None:
                    print("No existe un alquiler con ese Id")
                else:
                    print("")
                    alq.mostrarDatos()

            elif opcion == 4:
                idAlq = int(input("Ingrese Id del alquiler a modificar: "))
                alq = traerAlquiler(idAlq)
                if alq == None:
                    print("No existe un alquiler con ese Id")
                else:
                    print("\nDatos actuales:")
                    alq.mostrarDatos()

                    idCli = int(input("Ingrese nuevo Id de cliente: "))
                    cli = traerCliente(idCli)
                    idJue = int(input("Ingrese nuevo Id de juego: "))
                    jue = traerJuego(idJue)
                    dias = int(input("Ingrese nueva cantidad de dias: "))

                    if cli == None or jue == None or dias <= 0:
                        print("Error: verifique que cliente y juego existan y los dias sean mayores a 0")
                    else:
                        alqMod = Alquiler(cli, jue, dias, idAlq)
                        modificarAlquiler(alqMod)
                        print("Alquiler modificado")

            elif opcion == 5:
                alquileres = traerAlquileres()
                print("\nId - Cliente - Juego")
                for a in alquileres:
                    print(a.IdAlquiler, "-", a.Cliente.Nombre, a.Cliente.Apellido, "-", a.Juego.Nombre)

                idAlq = int(input("Ingrese Id del alquiler a borrar: "))
                alq = traerAlquiler(idAlq)
                if alq == None:
                    print("No existe un alquiler con ese Id")
                else:
                    borrarAlquiler(idAlq)
                    print("Alquiler borrado")

            elif opcion == 6:
                break
            else:
                print("Opcion no valida")

        except ValueError:
            print("Error: debe ingresar un numero valido")

def menuPrincipal():
    while True:
        print("\nMenú principal - JuegoClub:")
        print("1. Clientes")
        print("2. Juegos")
        print("3. Alquileres")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                menuClientes()
            elif opcion == 2:
                menuJuegos()
            elif opcion == 3:
                menuAlquileres()
            elif opcion == 4:
                print("Saliendo de la aplicacion")
                break
            else:
                print("Opcion no valida")
        except ValueError:
            print("Error: debe ingresar un numero valido")
        except Exception as e:
            print("Ocurrio un error:", e)

menuPrincipal()
