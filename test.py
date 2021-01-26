from Class_persona import Persona
from Class_Material import Material
import jsonpickle

class FileManager:

    @staticmethod
    def readFile(ns, mLista):

        route = ns+'test.json'

        with open(route, 'r') as inputLista:
            
            data = inputLista.read()
            outputLista = []

            jsonobject = jsonpickle.decode(data)
        
            if (ns=='persons'):
                lista = jsonobject
                for objeto in lista:
                    outputLista.append(objeto)
            if (ns=='materials'):
                lista = jsonobject["materiales"]
                for objeto in lista:
                    outputLista.append(objeto)
            return outputLista

    @staticmethod
    def writeFile(ns, saveData):

        route = ns+'.json'
        with open(route, 'w') as inputLista:

            frozen = jsonpickle.encode(saveData,indent=4)
            inputLista.write(frozen)

            return True


if __name__ == "__main__":

    newLista = FileManager.readFile("persons",[])

    print(newLista)

    saved = FileManager.writeFile("persons",newLista)
    
    #newLista = FileManager.readFile("persons",[])

    #print(newLista)
    #for persona in newLista:
    #    print(persona.nombre)
    #    print(persona.edad)
    #    print(persona.puesto)
    #    for material in persona.materiales:
    #        print(material.id)
    #        print(material.nombre)
    #        print(material.fechaPedido)
    #        print(material.fechaEntregado)
