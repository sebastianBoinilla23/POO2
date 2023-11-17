from Vuelo import Vuelo

class TorreDeControl:
    def __init__(self):
        self.puertaEmbarque = list(range(1, 11))

    def asignarembarque(self, vuelo):
        if self.puertaEmbarque:
            vuelo.puertaEmbarque = self.puertaEmbarque.pop(0)
        else:
            print("No hay puertas de embarque disponibles en este momento.")

    def actualizarestadovuelo(self, vuelo, estado):
        vuelo.estado = estado
        print(f"El vuelo {vuelo.Vueloid} está ahora {estado}.")
        if estado == "Programado":
            estado = "En el aire"
            vuelo.estado = estado
            if estado == "En el aire":
                estado = "En tierra"
                vuelo.estado = estado