from Aeronave import Aeronave

class Helicoptero(Aeronave):
    def __init__(self, modelo, capacidad, velmax, autonomia, añoFab, CantRotores, CapElevacion, TipoUso ):
        super().__init__(modelo, capacidad, velmax, autonomia, añoFab)
        self.CantRotores = CantRotores
        self.CapElevacion = CapElevacion
        self.TipoUso = TipoUso

    def AgregarHeli(self):
        super().Agregardatos()
        self.CantRotores = input("INGRESE LA CANTIDAD DE ROTORES: ")
        self.CapElevacion = input("INGRESE LA CAPACIDAD DE ELEVACION: ")
        self.TipoUso = input("INGRESE EL TIPO DE USO: ")

    def Mostrardatos(self):
        super().Mostrardatos()
        return(f"CANTIDAD DE ROTORES: {self.CantRotores}\n"
               f"CAPACIDAD DE ELEVACION: {self.CapElevacion}n"
               f"TIPO DE USO: {self.TipoUso}\n")

    def __str__(self):
        return self.Mostrardatos()