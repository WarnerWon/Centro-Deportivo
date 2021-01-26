#Se importa el controlador Codigo_Consola
#Este archivo se podria decir que es el menu
from Codigo_Consola import *

#variables inicializadas para poder entrar al while 1 vez
respuesta = "1"
session = True

while respuesta != "8":

    print("\n::::Bienvenido al centro deportivo de UTT")
    print("::::Ingrese su nombre")

    #Se crea o recupera un usuario guardado en la BD
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

        #Lee la consola
        respuesta = input()

        #En base a la respuesta elige las funciones
        if respuesta == "1":
            #Asigna 1 material a 1 persona
            # se puede hacer varias veces 
            p = pedirMats(p)
        elif respuesta == "2":
            #Muestra los materiales pedidos y devueltos del usuario en sesion
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