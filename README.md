PROYECTO 1
PROGRAMACIÓN ORIENTADA A OBJETOS
INTEGRANTES: SEBASTIAN BONILLA

INDICE
1. Presentación general del proyecto
2. Diagrama
3. Código
3.1 ¿Cómo funciona el programa?
3.2 ¿Cómo compilar el programa?
3.3 ¿Cómo ejecutar el programa?
4. Evidencias
5. Referencias

1. Presentación general del proyecto

De acuerdo con el Consejo Internacional de Aeropuertos para Ámerica Latina y el Caribe (ACI -LAC), el tráfico de pasajeros en estas regiones se incrementó un 47.8% en 2022, en comparación con el 2021. (Redaccion Trade News, 2023)
Lo anterior, logra poner en evidencia la importancia de facilitar los procesos claves/críticos  para los aeropuertos y sus aerolineas a través de la sistematización de los mismos. 
Por ello, este proyecto propone una idea de cómo los procesos para compra de vuelos, conocer los estados de aviones, conocer los tipos de aeronaves, realizar el ingreso de datos de pasajeros, etc; podrían ser automatizados mediante un código desarollado en lenguaje c++. Para el desarrollo de esta propuesta, resultó necesario aplicar los conocimientos relacionados con clases, métodos y objetos adquiridos en el curso de Programación Orientada a Objetos.  

2. Diagrama

3. Código

3.1 ¿Cómo funciona?

El programa presentado requiere que el usuario realice una interacción completa, puesto que, debe ser él quien cargue los datos solicitados por el programa y posteriormente, evidenciar su funcionamiento.

Respecto al código es importante mencionar que emplea y considera aspectos como por ejemplo: recursividad para que una función resuelva un problema al llamarse a sí misma, poliformismo para que objetos de diferentes clases puedan emplear la misma interfaz, la correcta identación para estructurar adecuadamente el código y facilitar su legilibilidad, el uso de patrones de diseño y buenas prácticas.

3.2 ¿Cómo compilar el programa?

Con el objetivo de facilitar su uso, se diseñó un código completo que no requiere cambios para ser compilado. 

3.3 ¿Cómo ejecutar el programa?

Para ejecutar el código de manera sencilla, se emplea CLion, un editor de texto que facilita el acceso a una terminal y su utilización. En esta terminal, se muestra todo el proceso de ejecución del código, lo que permite tanto ingresar nuevos datos como visualizar aquellos que han sido previamente cargados.

4. Evidencias
   fragmentos de codigo:
   int main() {
    int menu;
    vector<aeronave> aeronaves;
    vector<avion> aviones;
    vector<helicoptero> helicopteros;
    vector<jetprivado> jetsPrivados;
    vector<vuelo> vuelos;
    vector<Pasajero> pasajeros;
    do {
        system("cls");
        cout << "---------BIENVENIDO--------\n";
        cout << "------MENU AEROPUERTO--------\n";
        cout << "1. Aeronaves\n";
        cout << "2. Vuelos\n";
        cout << "3. Usuarios\n";
        cin >> menu;
        cout << ":::::::::::::::::::::\n";

        if (menu == 1) {
            system("cls");
            crearaeronave(aviones, helicopteros, jetsPrivados);
        } else if (menu == 2) {
            crearvuelo(vuelos, aviones, helicopteros, jetsPrivados);
        } else if (menu == 3) {
            crearusuario(pasajeros, vuelos, aviones, helicopteros, jetsPrivados);
        }


        system("pause");
    } while (menu != 4);

    return 0;
}

5. Referencias
Redaccion Trade News. (2023, August 25). Cuáles fueron los 10 aeropuertos con más movimiento de América latina y el Caribe en 2022 - Trade News. Trade News. https://tradenews.com.ar/cuales-fueron-los-10-aeropuertos-con-mas-movimiento-de-america-latina-y-el-caribe-en-2022/#:~:text=A%20la%20cabeza%20del%20ranking,seguida%20por%20la%20terminal%20colombiana.

‌
