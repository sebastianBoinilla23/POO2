class Aeronave:
    contador_id = 1

    def __init__(self, modelo, capacidad, velmax, autonomia, añoFab):
        self.IdAero = Aeronave.contador_id
        Aeronave.contador_id += 1
        self.modelo = modelo
        self.capacidad = capacidad
        self.velmax = velmax
        self.autonomia = autonomia
        self.añoFab = añoFab
        self.estado = "Disponible"
        self.tripulacion_asignada = []

    def Agregardatos(self):
        self.modelo = input("MODELO: ")
        self.capacidad = int(input("CAPACIDAD PASAJEROS: "))
        self.velmax = input("VELOCIDAD MAXIMA: ")
        self.autonomia = input("AUTONOMIA: ")
        self.añoFab = input("AÑO FABRICACION: ")

    def AsignarTripulacion(self, tripulacion):
        self.tripulacion_asignada.append(tripulacion)

    def MostrarTripulacion(self):
        print("--- TRIPULACIÓN ASIGNADA ---")
        i = 1
        for tripulacion in self.tripulacion_asignada:
            print("--------TRIPULANTE {}---------".format(i))
            tripulacion.MostrarTripulante()
            i += 1

    def Mostrardatos(self):
        return (f"ID AERONAVE: {self.IdAero}\n"
                f"MODELO: {self.modelo}\n"
                f"CAPACIDAD PASAJEROS: {self.capacidad}\n"
                f"VELOCIDAD MAXIMA: {self.velmax}\n"
                f"AUTONOMIA: {self.autonomia}\n"
                f"AÑO FABRICACION: {self.añoFab}\n"
                f"ESTADO AERONAVE: {self.estado}")

    def __str__(self):
        return self.Mostrardatos()
