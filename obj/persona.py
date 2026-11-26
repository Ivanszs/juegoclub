class Persona:
    def __init__(self, pNombre="", pApellido="", pDni=""):
        self.Nombre = pNombre
        self.Apellido = pApellido
        self.__Dni = pDni

    def getDni(self):
        return self.__Dni

    def setDni(self, pDni):
        self.__Dni = pDni

    def mostrarDatos(self):
        print("Nombre Completo:", self.Nombre, self.Apellido)
        print("N° Documento:", self.__Dni)
