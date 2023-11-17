from Pasajero import Pasajero

class Tripulacion(Pasajero):
    def __init__(self, Nombre, Apellido, Nacionalidad, CantidadM, EstSalud, Cedula, Genero, Direccion, NumeroTel,
                 Correo, cargo, exp, horaslaborales, idAero):
        super().__init__(Nombre, Apellido, Nacionalidad, CantidadM, EstSalud, Cedula, Genero, Direccion, NumeroTel,
                         Correo)
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
        print(super().MostrarPasajero())
        print(f"ID AERONAVE: {self.idAero}")
        return(f"ID AERONAVE ASIGNADA: {self.idAero}\n"
            f"CARGO: {self.cargo}\n"
            f"EXPERIENCIA LABORAR: {self.exp}\n"
            f"HORAS LABORALES: {self.horaslaborales}\n")
