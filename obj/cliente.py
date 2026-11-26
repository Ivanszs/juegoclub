from obj.persona import Persona

class Cliente(Persona):
    def __init__(self, pNombre="", pApellido="", pDni="", pTelefono="", pIdCliente=0):
        super().__init__(pNombre, pApellido, pDni)
        self.IdCliente = pIdCliente
        self.Telefono = pTelefono

    def mostrarDatos(self):
        print("Id Cliente:", self.IdCliente)
        super().mostrarDatos()
        print("Telefono:", self.Telefono)
