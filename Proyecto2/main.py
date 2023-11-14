from Aeronave import Aeronave
from Helicoptero import Helicoptero
from Avion import Avion
from JetPrivado import Jetprivado
from Pasajero import Pasajero
from Tripulacion import Tripulacion
import os

def mostrar_menu():
    print("Menú:")
    print("1. AERONAVES")
    print("2. VUELOS")
    print("3. PASAJEROS")
    print("4. TRIPULACION")
    print("5. Salir")


aeronaves = []
aviones = []
helicopteros = []
jets = []
usuarios = []
tripulacion = []
id_aero_tripulacion = None

def buscar_aeronave_por_id(id_aero):
    global aeronaves
    for aeronave in aeronaves:
        if aeronave.IdAero == id_aero:
            return aeronave
    return None


while True:
    os.system("cls")
    mostrar_menu()
    opcion = input("SELECIONE UNA OPCION: ")
    if opcion == "1":
        print("1.CREAR AERONAVE")
        print("2.MOSTRAR AERONAVE")
        opcion = input("SELECIONE UNA OPCION: ")
        if opcion == "1":
            print("1.AVION")
            print("2.HELICOPTERO")
            print("3. JET PRIVADO")
            TipoAero = input("SELECIONE UNA OPCION: ")
            if TipoAero == "1":
                modelo = input("MODELO: ")
                capacidad = int(input("CAPACIDAD PASAJEROS: "))
                velmax = input("VELOCIDAD MAXIMA: ")
                autonomia = input("AUTONOMIA: ")
                añoFab = input("AÑO FABRICACION: ")
                AltitudMax = input("INGRESE LA ALTITUD MAXIMA: ")
                CantMotores = int(input("INGRESE LA CANTIDAD DE MOTORES: "))
                Categoria = input("INGRESE LA CATEGORIA: ")
                nuevo_avion = Avion(modelo, capacidad, velmax, autonomia, añoFab, AltitudMax, CantMotores, Categoria)
                aviones.append(nuevo_avion)
            elif TipoAero == "2":
                modelo = input("MODELO: ")
                capacidad = int(input("CAPACIDAD PASAJEROS: "))
                velmax = input("VELOCIDAD MAXIMA: ")
                autonomia = input("AUTONOMIA: ")
                añoFab = input("AÑO FABRICACION: ")
                CantRotores = input("CANTIDAD DE ROTORES")
                CapElevacion = input("CAPACIDAD DE ELEVACION")
                TipoUso = input("TIPO DE USO")
                nuevo_helicoptero = Helicoptero(modelo, capacidad, velmax, autonomia, añoFab, CantRotores, CapElevacion, TipoUso)
                helicopteros.append(nuevo_helicoptero)
            elif TipoAero == "3":
                modelo = input("MODELO: ")
                capacidad = int(input("CAPACIDAD PASAJEROS: "))
                velmax = input("VELOCIDAD MAXIMA: ")
                autonomia = input("AUTONOMIA: ")
                añoFab = input("AÑO FABRICACION: ")
                Propietario = input("PROPIETARIO: ")
                servicios = []
                destinos = []
                while True:
                    print("----SI DESEA SALIR ESCRIBA SALIR----")
                    nuevo_servicio = input("INGRESE EL SERVICIO: ")
                    nuevo_destino = input("INGRESE EL DESTINO FRECUENTE: ")
                    if nuevo_servicio.lower() == "salir":
                        break
                    servicios.append(nuevo_servicio)
                    destinos.append(nuevo_destino)
                nuevo_jet = Jetprivado(modelo, capacidad, velmax, autonomia, añoFab, Propietario, servicios, destinos)
                jets.append(nuevo_jet)
        elif opcion == "2":
            if not aviones and not helicopteros and not jets:
                print("No hay datos de aeronaves ingresados.")
            else:
                print("\n---DATOS AERONAVES---:")
                for Avion in aviones:
                    Avion.MostrarAvion()
                for Helicoptero in helicopteros:
                    Helicoptero.MostrarHeli()
                for Jetprivado in jets:
                    Jetprivado.Mostrarjet()
    elif opcion == "3":
        print("--- MENU PASAJEROS ---")
        print("1.INGRESAR PASAJEROS")
        print("2.MOSTRAR PASAJEROS")
        print("3.COMPRAR VUELOS")
        opcion = input("SELECIONE UNA OPCION: ")
        if opcion == "1":
            Nombre = input("INGRESE EL NOMBRE: ")
            Apellido = input("INGRESE EL APELLIDO: ")
            Nacionalidad = input("INGRESE NACIONALIDAD: ")
            CantidadM = int(input("INGRESE LA CANTIDAD DE MALETAS: "))
            EstSalud = input("INGRESE ESTADO DE SALUD: ")
            Cedula = input("INGRESE NUMERO DE CEDULA: ")
            Genero = input("INGRESE SU GENERO: ")
            Direccion = input("INGRESE SU DIRECCION: ")
            NumeroTel = input("INGRESE SU NUMERO TELEFONICO: ")
            Correo = input("INGRESE SU CORREO: ")
            nuevo_user = Pasajero(Nombre, Apellido, Nacionalidad, CantidadM, EstSalud, Cedula, Genero, Direccion, NumeroTel, Correo)
            usuarios.append(nuevo_user)
        elif opcion == "2":
            if not usuarios:
                print("No hay usuarios registrados")
            else:
                print("\n--- DATOS USUARIOS ---")
                for Pasajero in usuarios:
                    Pasajero.MostrarPasajero()
    elif opcion == "4":
        print("--- MENU TRIPULACION ---")
        print("1. INGRESAR TRIPULANTE")
        print("2. MOSTRAR TRIPULACION")
        opcion = input("SELECCIONE UNA OPCION: ")
        if opcion == "1":
            Nombre = input("INGRESE EL NOMBRE: ")
            Apellido = input("INGRESE EL APELLIDO: ")
            Nacionalidad = input("INGRESE NACIONALIDAD: ")
            CantidadM = int(input("INGRESE LA CANTIDAD DE MALETAS: "))
            EstSalud = input("INGRESE ESTADO DE SALUD: ")
            Cedula = input("INGRESE NUMERO DE CEDULA: ")
            Genero = input("INGRESE SU GENERO: ")
            Direccion = input("INGRESE SU DIRECCION: ")
            NumeroTel = input("INGRESE SU NUMERO TELEFONICO: ")
            Correo = input("INGRESE SU CORREO: ")
            cargo = input("INGRESE SU CARGO: ")
            exp = input("INGRESE SU EXPERIENCIA EN AÑOS: ")
            horaslaborales = input("INGRESE CANTIDAD DE HORAS LABORALES: ")
            while True:
                id_aero_tripulacion = int(input("Ingrese el ID de la aeronave a la que se vinculará la tripulación: "))
                aero_existente = buscar_aeronave_por_id(id_aero_tripulacion)
                if aero_existente:
                    break
                else:
                    print("Aeronave no encontrada. Intente nuevamente.")
            nuevo_tripulante = Tripulacion(Nombre, Apellido, Nacionalidad, CantidadM, EstSalud, Cedula, Genero,
                                           Direccion, NumeroTel, Correo, cargo, exp, horaslaborales)
            tripulacion.append(nuevo_tripulante)
        elif opcion == "2":
            if id_aero_tripulacion is not None:
                aero_existente = buscar_aeronave_por_id(id_aero_tripulacion)
                if aero_existente:
                    aero_existente.Mostrardatos()
                    aero_existente.MostrarTripulacion()
                else:
                    print("Aeronave no encontrada.")
            else:
                print("Primero debe ingresar la tripulación vinculada a una aeronave.")
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
