class Alquiler:
    def __init__(self, pCliente=None, pJuego=None, pDias=0, pIdAlquiler=0):
        self.IdAlquiler = pIdAlquiler
        self.Cliente = pCliente
        self.Juego = pJuego
        self.Dias = pDias

    def calcularTotal(self, pDescuento=0):
        total = self.Juego.PrecioDia * self.Dias
        if pDescuento > 0:
            total = total - pDescuento
        return total

    def mostrarDatos(self):
        print("Id Alquiler:", self.IdAlquiler)
        print("Cliente:", self.Cliente.Nombre, self.Cliente.Apellido)
        print("Juego:", self.Juego.Nombre)
        print("Dias:", self.Dias)
        print("Total: $", self.calcularTotal())
