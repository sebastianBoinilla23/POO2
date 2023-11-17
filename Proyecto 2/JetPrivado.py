from Aeronave import Aeronave

class Jetprivado(Aeronave):
    def __init__(self, modelo, capacidad, velmax, autonomia, añoFab, propietario, servicios, destinos):
        super().__init__(modelo, capacidad, velmax, autonomia, añoFab)
        self.propietario = propietario
        self.servicios = []
        self.destinos = []

    def AgregarServicio(self, servicio):
        self.servicios.append(servicio)

    def AgregarDestinos(self, destino):
        self.destinos.append(destino)

    def Agregarjet(self):
        super().Agregardatos()
        self.propietario = input("INGRESE El NOMBRE DEL PROPIETARIO: ")

    def Mostrardatos(self):
        print(super().Mostrardatos())
        return (f"NOMBRE DE PROPIETARIO: {self.propietario}\n"
                f"SERVICIOS A BORDO: {self.servicios}\n"
                f"DESTINOS FRECUENTES: {self.destinos}")

    def __str__(self):
        return self.Mostrardatos()