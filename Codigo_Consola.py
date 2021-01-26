#Se podría decir que este es el controlador de nuesto programa
#Se importa la clase P_M la cual ya contiene las clases de persona, persona lista, material y registros de estas mismas
from Class_p_m import *
#Este import es para limpiar la consola
import os
clear = lambda: os.system('cls')

# Asignador de Sesion
#Si se ingresa un nombre ya ingresado saltará paso 3
def primeraVezUsuario():
    
    #Paso 1 Tomar Valor Nombre 
    tempNombre = input()
    clear()

    #Paso 2 Verifica Si existe nombre en BD
    #Si existe devuelve un objeto tipo Persona de la BD 
    p = lPerson.buscarPersona(tempNombre)
    
    #Paso 3 En caso de que NO exista nombre crear nuevo registro
    #y se añade a la BD 
    if bool(p) == False:
        print("Ingrese su edad")
        tempEdad = int(input())
        print("Ingrese su puesto")
        tempPuesto = input()
        p = Persona(tempNombre,tempEdad,tempPuesto,[])
        lPerson.añadirPersona(p)
    
    #Paso 4 retornar clase Persona modificada
    return p

#Asigna un material al usuarion en Sesion
def pedirMats(p):
    clear()
    print("Elige el material que te vas a llevar")
    
    #Imprime lista de mats
    for material in mLista:
        print(str(material.id) + ".- " + material.nombre)
    
    #Seleccionar mats
    respMaterial = int(input())
    
    #Agregar Material de DB a Persona.Materiales[]
    p.añadirMat(mLista[respMaterial -1])
    clear()
    print("Se ha añadido " + p.materiales[-1].nombre + " a tu lista")
    print("--------------------------------------------------------\n")

    #retorna p posiblemente modificada
    return p

#Muestra materiales entregados y no entregados por el usuario en sesion
def mostrarMats(p):
    clear()
    
    if bool(p.materiales) == True:
        print("Esto es el estatus de los materiales que has pedido:")
        print("ID....Nombre.........Fecha pedido.....................Fecha Entregado")
        #Imprime lista de materiales desde Persona.Materiales[]
        #Distingue entre material entregado y no entregado
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

#Asigna tiempo al material que se va devolver, dando a entender que se devolvió
def devolverMats(p):
    clear()
    print("Indica (con el ID) el material que vas a devolver")
    print("ID....Nombre.........Fecha pedido")
    #Imprime lista de materiales desde Persona.Materiales[]
    #Solo muestra material no entregado
    i = 1
    for material in p.materiales:
        if material.fechaEntregado == None:
            print(str(i) + ".- " + material.nombre + "......" + str(material.fechaPedido))
        i += 1
    
    #Lee la entrada de la consola
    respMaterial = int(input())

    #Selecciona el material y cambia el valor de None a datetime.now
    p.materiales[respMaterial -1].entregar()
    clear()
    print("Se ha regresado " + p.materiales[respMaterial - 1].nombre + " a la unidad deportiva")
    print("--------------------------------------------------------\n")
    return p

#Muestra todas las personas en DB
def mostrarPersonas():
    clear()
    print("Estas son las personas registradas en la base")
    print("ID...Nombre....Edad....Puesto")
    i = 1
    for persona in lPerson.Lista:
        print(str(i) + ".- " + persona.nombre + "......." + str(persona.edad) + "....." + persona.puesto)
        i += 1
    print("--------------------------------------------------------\n")

#Elimina una de las personas de la DB
#No se puede eliminar la persona en sesion
def eliminarPersona(p):
    clear()
    print("Indica (con el ID) la persona que será eliminada")
    print("ID...Nombre....Edad....Puesto")
    i = 1
    #Imprime todos los usuarios
    for persona in lPerson.Lista:
        print(str(i) + ".- " + persona.nombre + "......." + str(persona.edad) + "....." + persona.puesto)
        i += 1
    #Lee la respuesta de la consola
    respPersona = int(input())
    clear()
    #Compara si el usuario a eliminar esta en sesion o no
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