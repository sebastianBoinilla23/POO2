from Aeronave import Aeronave

class Vuelo:
    def __init__(self):
        self.Origenvuelo = ""
        self.Destinovuelo = ""
        self.aeronaveAsignada = 0
        self.ID = 0

    def Crearvuelo(self, id, ori, dest):
        self.ID = id
        self.Origenvuelo = ori
        self.Destinovuelo = dest

    def Setaeronave(self, aero):
        self.aeronaveAsignada = aero

    def Mostrarvuelo(self):
        print("ID vuelo:", self.ID)
        print("Origen De vuelo:", self.Origenvuelo)
        print("Destino De vuelo:", self.Destinovuelo)
        print("Aeronave asignada:")
        print("   ID aeronave:", self.aeronaveAsignada)

    def Mostrarvuelo_2(self):
        print("   ID vuelo:", self.ID)
        print("   Origen De vuelo:", self.Origenvuelo)
        print("   Destino De vuelo:", self.Destinovuelo)