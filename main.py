from Codigo_Consola import *

respuesta = "1"
session = True

while respuesta != "8":

    print("\n::::Bienvenido al centro deportivo de UTT")
    print("::::Ingrese su nombre")

    p = primeraVezUsuario()

    clear()

    print("\nBienvenido " + p.nombre )

    session = True

    while session == True:
        print("Que desea hacer?\n" + 
            "1. Pedir un material\n" +
            "2. Ver registro de tus materiales pedidos\n" +
            "3. Devolver Material")
        print("4. Ver personas en el sistema")
        print("5. Borrar personas en el sistema")
        print("6. iniciar sesion otra persona")
        print("7. Guardar Datos")
        print("8. Salir del programa")

        respuesta = input()

        if respuesta == "1":
            p = pedirMats(p)
        elif respuesta == "2":
            mostrarMats(p)
        elif respuesta == "3":
            p = devolverMats(p)
        elif respuesta == "4":
            mostrarPersonas()
        elif respuesta == "5":
            eliminarPersona(p)
        elif respuesta == "6":
            session = False
            clear()
            print("Volviendo a iniciar sesion...")
            print("--------------------------------------------------------\n")
        elif respuesta == "7":
            saved = FileManager.writeFile("persons",lPerson)
            if saved == True:
                clear()
                print("Se ha guardado con exito")
                print("--------------------------------------------------------\n")
            else:
                print("ALGO SALIO MAL D:")
        elif respuesta == "8":
            session = False
            print("Saliendo...")