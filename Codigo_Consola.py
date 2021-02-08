from Class_p_m import *
import os
clear = lambda: os.system('cls')

def primeraVezUsuario():
    
    tempNombre = input()
    clear()

    p = lPerson.buscarPersona(tempNombre)
    
    if bool(p) == False:
        print("Ingrese su edad")
        tempEdad = int(input())
        print("Ingrese su puesto")
        tempPuesto = input()
        p = Persona(tempNombre,tempEdad,tempPuesto,[])
        lPerson.añadirPersona(p)
    
    return p

def pedirMats(p):
    clear()
    print("Elige el material que te vas a llevar")
    
    for material in mLista:
        print(str(material.id) + ".- " + material.nombre)
    
    respMaterial = int(input())
    
    p.añadirMat(mLista[respMaterial -1])
    clear()
    print("Se ha añadido " + p.materiales[-1].nombre + " a tu lista")
    print("--------------------------------------------------------\n")

    return p

def mostrarMats(p):
    clear()
    
    if bool(p.materiales) == True:
        print("Esto es el estatus de los materiales que has pedido:")
        print("ID....Nombre.........Fecha pedido.....................Fecha Entregado")
        i = 1
        for material in p.materiales:
            if material.fechaEntregado == None:
                print(str(i) + ".-  " + material.nombre + "......" + str(material.fechaPedido) + "... " + "Aun no entregado")
            else:
                print(str(i) + ".-  " + material.nombre + "......" + str(material.fechaPedido) + "... " + str(material.fechaEntregado))
            i += 1
        print("\n")
        print("\n")
    else:
        print("No debes ningun material")
        print("\n")
        print("\n")

def devolverMats(p):
    clear()
    print("Indica (con el ID) el material que vas a devolver")
    print("ID....Nombre.........Fecha pedido")
    i = 1
    for material in p.materiales:
        if material.fechaEntregado == None:
            print(str(i) + ".- " + material.nombre + "......" + str(material.fechaPedido))
        i += 1
    
    respMaterial = int(input())

    p.materiales[respMaterial -1].entregar()
    clear()
    print("Se ha regresado " + p.materiales[respMaterial - 1].nombre + " a la unidad deportiva")
    print("--------------------------------------------------------\n")
    return p

def mostrarPersonas():
    clear()
    print("Estas son las personas registradas en la base")
    print("ID...Nombre....Edad....Puesto")
    i = 1
    for persona in lPerson.Lista:
        print(str(i) + ".- " + persona.nombre + "......." + str(persona.edad) + "....." + persona.puesto)
        i += 1
    print("--------------------------------------------------------\n")

def eliminarPersona(p):
    clear()
    print("Indica (con el ID) la persona que será eliminada")
    print("ID...Nombre....Edad....Puesto")
    i = 1
    for persona in lPerson.Lista:
        print(str(i) + ".- " + persona.nombre + "......." + str(persona.edad) + "....." + persona.puesto)
        i += 1
    respPersona = int(input())
    clear()
    if p.nombre != lPerson.Lista[respPersona -1].nombre:
        print("El usuario " + lPerson.Lista[respPersona -1].nombre + " se ha eliminado del sistema")
        lPerson.Lista.pop(respPersona - 1)
    else:
        print("No se puede eliminar el usuario que esta usando ahora mismo")
    print("--------------------------------------------------------\n")

def guardarInfo(lPerson, p):
    clear()
    print("Esta a punto de sobre escribir los datos. ¿Esta seguro?")
    print("y/n")
    confirm = input()
    if confirm == "y":
        return None