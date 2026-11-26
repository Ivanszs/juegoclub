class Juego:
    def __init__(self, pNombre="", pCategoria="", pPrecioDia=0.0, pIdJuego=0):
        self.IdJuego = pIdJuego
        self.Nombre = pNombre
        self.Categoria = pCategoria
        self.PrecioDia = pPrecioDia

    def mostrarDatos(self):
        print("Id Juego:", self.IdJuego)
        print("Juego:", self.Nombre)
        print("Categoria:", self.Categoria)
        print("Precio por dia: $", self.PrecioDia)
