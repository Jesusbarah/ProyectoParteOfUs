from medidas import Medidas
from databaseX import DatabaseX

eleccion = 0


eleccion = int(input("Ingrese el número de la opción que desea: "))


while True:

    if eleccion == 0:
        break
    elif eleccion == 1:
        resumen = Resumen()
        resumen.imprimeResumen()
    elif eleccion == 2:
        medidas = Medidas()
        peso = 0
        cintura = 0
        cuello = 0
        while True:
            print("(1) Ingresar peso del día")
            print("(2) Ingresar registro de cintura")
            print("(3) Ingresar registro de cuello")
            print("(4) Enviar mi registro")
            print("(0) Regresar al menú principal")
            opcion = int(input("Ingrese el número de la opción que desea: "))
            if opcion == 0:
                break
            elif opcion == 1:
                peso = float(input("Ingrese su peso en kilogramos: "))
                medidas.ingresarPeso(peso)
            elif opcion == 2:
                cintura = float(input("Ingrese su medida de cintura en centímetros: "))
                medidas.ingresarCintura(cintura)
            elif opcion == 3:
                cuello = float(input("Ingrese su medida de cuello en centímetros: "))
                medidas.ingresarCuello(cuello)
            elif opcion == 4:
                medidas.enviarRegistro()