from Aeronave import Aeronave

class Avion(Aeronave):
    def __init__(self, modelo, capacidad, velmax, autonomia, añoFab,AltitudMax, CantMotores, Categoria ):
        super().__init__(modelo, capacidad, velmax, autonomia, añoFab)
        self.AltitudMax = AltitudMax
        self.CantMotores = CantMotores
        self.Categoria = Categoria

    def AgregarAvion(self):
        super().Agregardatos()
        self.AltitudMax = input("INGRESE LA ALTITUD MAXIMA: ")
        self.CantMotores = int(input("INGRESE LA CANTIDAD DE MOTORES: "))
        self.Categoria = input("INGRESE LA CATEGORIA: ")

    def MostrarAvion(self):
        super().Mostrardatos()
        print(f"ALTITUD MAXIMA: {self.AltitudMax}")
        print(f"CANTIDAD DE MOTORES: {self.CantMotores}")
        print(f"CATEGORIA: {self.Categoria}")
