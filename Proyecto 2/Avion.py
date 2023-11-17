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

    def Mostrardatos(self):
        print(super().Mostrardatos())
        return (
            f"ALTITUD MAXIMA: {self.AltitudMax}\n"
            f"CANTIDAD DE MOTORES: {self.CantMotores}\n"
            f"CATEGORIA: {self.Categoria}\n")

    def __str__(self):
        return self.Mostrardatos()
