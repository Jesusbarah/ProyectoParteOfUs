from login import Login
from signUp import SignUp
from resumenDiario import Resumen
from medidas import Medidas
from objetivos import Objetivos
from alimentacion import Alimentacion
from ejercicio import Ejercicio
from evolucion import Evolucion

eleccion = 0
idUsuario = 0


while True:
    print("Aplicación fit")
    print("(1) Iniciar sesión")
    print("(2) Crear una cuenta")
    print("(0) Salir")
    eleccion = int(input("Ingrese el número de la opción que desea: "))

    if eleccion == 0:
        break
    elif eleccion == 1:
        login = Login()
        usuario = input("Ingrese su nombre de usuario: ")
        contra = input("Ingrese su contraseña: ")
        comprobacion = login.comprobacion(usuario, contra)
        if comprobacion:
            print("Iniciando sesión")
            idUsuario = login.idUsuario()
            break
        else:
            print("Usuario o contraseña incorrectos")
    elif eleccion == 2:
        signUp = SignUp()
        usuario = input("Ingrese un nombre de usuario: ")
        compUsuario = signUp.comprobacionUsuario(usuario)
        if compUsuario:
            correo = input("Ingrese su correo electronico: ")
            compCorreo = signUp.comprobacionCorreo
            if compCorreo:
                contra = input("Ingrese su contraseña: ")
                compContra = signUp.comprobacionContra()
                if compContra:
                    signUp.guardaDatos()
                else:
                    print("Contraseña no válida")
            else:
                print("Ya existe una cuenta vinculada a ese correo electrónico")
        else:
            print("El usuario que ha ingresado ya existe")

while True:

    if eleccion == 0:
        break

    print("Menú principal")
    print("(1) Mostrar resumen diario")
    print("(2) Ingresar medidas")
    print("(3) Objetivos")
    print("(4) Registrar alimento")
    print("(5) Registrar ejercicio")
    print("(6) Evolución de mi progreso")
    print("(0) Salir")
    eleccion = int(input("Ingrese el número de la opción que desea: "))

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
    elif eleccion == 3:
        objetivos = Objetivos()
        while True:
            print("(1) Mostrar objetivos")
            print("(2) Agregar objetivos")
            print("(3) Modificar objetivos")
            print("(4) Eliminar objetivos")
            print("(0) Regresar al menú principal")
            opcion = int(input("Ingrese el número de la opción que desea: "))
            if opcion == 0:
                break
            elif opcion == 1:
                objetivos.mostrarObjetivos()
            elif opcion == 2:
                objetivos.agregarObjetivos()
            elif opcion == 3:
                objetivos.modificarObjetivos()
            elif opcion == 4:
                objetivos.eliminarObjetivos()
    elif eleccion == 4:
        alimentacion = Alimentacion()
        while True:
            print("(1) Agregar alimento")
            print("(2) Buscar alimento")
            print("(3) Crear receta")
            print("(0) Regresar al menú principal")
            opcion = int(input("Ingrese el número de la opción que desea: "))
            if opcion == 0:
                break
            elif opcion == 1:
                idAlimento = int(
                    input(
                        "Ingrese el ID de su alimento, si desconoce el ID ingrese 0 para ir al buscador: "
                    )
                )
                if idAlimento == 0:
                    alimentacion.buscarAlimento()
                else:
                    alimentacion.agregarAlimento(idAlimento)
            elif opcion == 2:
                alimentacion.buscarAlimento()
            elif opcion == 3:
                alimentacion.crearReceta()
    elif eleccion == 5:
        ejercicio = Ejercicio()
        while True:
            print("(1) Agregar ejercicio de cardio")
            print("(2) Buscar ejercicio de cardio")
            print("(3) Crear ejercicio de cardio")
            print("(4) Agregar ejercicio de peso")
            print("(5) Buscar ejercicio de peso")
            print("(6) Crear ejercicio de peso")
            print("(0) Regresar al menú principal")
            opcion = int(input("Ingrese el número de la opción que desea: "))
            if opcion == 0:
                break
            elif opcion == 1:
                idEjercicio = int(
                    input(
                        "Ingrese el ID de su alimento, si desconoce el ID ingrese 0 para ir al buscador: "
                    )
                )
                if idEjercicio == 0:
                    ejercicio.buscarCardio()
                else:
                    ejercicio.agregarCardio(idEjercicio)
            elif opcion == 2:
                ejercicio.buscarCardio()
            elif opcion == 3:
                ejercicio.crearCardio()
            elif opcion == 4:
                idEjercicio = int(
                    input(
                        "Ingrese el ID de su alimento, si desconoce el ID ingrese 0 para ir al buscador: "
                    )
                )
                if idEjercicio == 0:
                    ejercicio.buscarPeso()
                else:
                    ejercicio.agregarPeso(idEjercicio)
            elif opcion == 5:
                ejercicio.buscarPeso()
            elif opcion == 6:
                ejercicio.crearPeso()
    elif eleccion == 6:
        evolucion = Evolucion()
        while True:
            print("(1) Evolución de mi peso")
            print("(2) Evolución de cintura")
            print("(3) Evolución de cuello")
            print("(4) Calorías consumidas")
            print("(5) Calorías quemadas")
            print("(6) Parámetro para peso")
            print("(0) Regresar al menú principal")
            opcion = int(input("Ingrese el número de la opción que desea: "))
            if opcion == 0:
                break
            elif opcion == 1:
                evolucion.evoPeso()
            elif opcion == 2:
                evolucion.evoCintura()
            elif opcion == 3:
                evolucion.evoCuello()
            elif opcion == 4:
                evolucion.evoCalConsumidas()
            elif opcion == 5:
                evolucion.evoCalQuemadas()
            elif opcion == 6:
                evolucion.evoEjPeso()
            elif opcion == 7:
                evolucion.evoTiempo()


print("Finalizando app")
