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
        for tripulacion in self.tripulacion_asignada:
            tripulacion.MostrarTripulante()

    def Mostrardatos(self):
        print("--- DATOS INGRESADOS ---")
        print(f"ID AERONAVE: {self.IdAero}")
        print(f"MODELO: {self.modelo}")
        print(f"CAPACIDAD PASAJEROS: {self.capacidad}")
        print(f"VELOCIDAD MAXIMA: {self.velmax}")
        print(f"AUTONOMIA: {self.autonomia}")
        print(f"AÑO FABRICACION: {self.añoFab}")
        print(f"ESTADO AERONAVE: {self.estado}")
