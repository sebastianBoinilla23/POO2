
class Pasajero:
    def __init__(self, Nombre, Apellido, Nacionalidad, CantidadM, EstSalud, Cedula, Genero, Direccion, NumeroTel, Correo):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Nacionalidad = Nacionalidad
        self.CantidadM = CantidadM
        self.EstSalud = EstSalud
        self.Cedula = Cedula
        self.Genero = Genero
        self.Direccion = Direccion
        self.NumeroTel = NumeroTel
        self.Correo = Correo

    def AgregarPasajero(self, Nombre, Apellido, Nacionalidad, CantidadM, EstSalud, Cedula, Genero, Direccion, NumeroTel, Correo):
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.Nacionalidad = Nacionalidad
        self.CantidadM = CantidadM
        self.EstSalud = EstSalud
        self.Cedula = Cedula
        self.Genero = Genero
        self.Direccion = Direccion
        self.NumeroTel = NumeroTel
        self.Correo = Correo

    def MostrarPasajero(self):
        print("Nombre:", self.Nombre)
        print("Apellido:", self.Apellido)
        print("Nacionalidad:", self.Nacionalidad)
        print("Cantidad maletas:", self.CantidadM)
        print("Estado de salud:", self.EstSalud)
        print("Cedula:", self.Cedula)
        print("Genero:", self.Genero)
        print("Direccion de vivienda:", self.Direccion)
        print("Numero telefonico:", self.NumeroTel)
        print("Correo:", self.Correo)