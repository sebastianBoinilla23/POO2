from Pasajero import Pasajero

class Tripulacion:
    def __init__(self, Nombre, Apellido, Nacionalidad, CantidadM, EstSalud, Cedula, Genero, Direccion, NumeroTel, Correo, cargo, exp, horaslaborales, idAero):
        super().__init__(Nombre, Apellido, Nacionalidad, CantidadM, EstSalud, Cedula, Genero, Direccion, NumeroTel, Correo)
        self.cargo = cargo
        self.exp = exp
        self.horaslaborales = horaslaborales
        self.idAero = idAero


    def AgregarTripulante(self):
        super().AgregarPasajero()
        self.cargo = input("INGRESE SU CARGO: ")
        self.exp = input("INGRESE SU EXPERIENCIA EN AÑOS: ")
        self.horaslaborales = input("INGRESE CANTIDAD DE HORAS LABORALES: ")

    def MostrarTripulante(self):
        super().MostrarPasajero()
        print(f"ID AERONAVE ASIGNADA: {self.idAero}")
        print(f"CARGO: {self.cargo}")
        print(f"EXPERIENCIA LABORAR: {self.exp}")
        print(f"HORAS LABORALES: {self.horaslaborales}")