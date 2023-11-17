from Aeronave import Aeronave

class Vuelo:
    contador_id = 1
    def __init__(self, Origenvuelo, Destinovuelo, aeronave):
        self.Vueloid = Vuelo.contador_id
        Vuelo.contador_id += 1
        self.Origenvuelo = Origenvuelo
        self.Destinovuelo = Destinovuelo
        self.aeronave = aeronave
        self.estado = "Programado"
        self.puertaEmbarque = None


    def Crearvuelo(self, Origenvuelo, Destinovuelo):
        self.Origenvuelo = Origenvuelo
        self.Destinovuelo = Destinovuelo


    def Mostrarvuelo(self):
        print(f"ID AERONAVE: {self.idAero}")
        return(f"ID vuelo:, {self.Vueloid}\n"
               f"Origen De vuelo:, {self.Origenvuelo}\n"
               f"Destino De vuelo:, {self.Destinovuelo}\n")

    def MostrarVueloA(self):
        return (f"ID vuelo:, {self.Vueloid}\n"
               f"ORIGEN VUELO:, {self.Origenvuelo}\n"
               f"DESTINO VUELO:, {self.Destinovuelo}\n"
               f"ESTADO VUELO:, {self.estado}\n"
               f"PUERTA DE EMBARQUE:, {self.puertaEmbarque}\n"
               f"DATOS TIPO AERONAVE: \n{self.aeronave}")

    def __str__(self):
        return self.MostrarVueloA()