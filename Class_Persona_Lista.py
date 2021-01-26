#La existencia de esta clase se debe a que la clase persona
#o en general cualquier clase de Python no acepta más de dos
#constructores, lo cual es una pena. Aun así se soluciona separando
#dicha clase de persona en dos, el array y el objeto singular

class Persona_Lista:

    #Inicializa los objetos con este constructor
    def __init__(self, Lista:[]):
        self.Lista = Lista

    #Busca a una persona dado su nombre
    #regresa el objeto que coincida con dicha condicion
    def buscarPersona(self, nombre):
        for persona in self.Lista:
            if persona.nombre == nombre:
                return persona
    
    #Añade un objeto de tipo Persona al array
    def añadirPersona(self, persona):
        self.Lista.append(persona)

    #Clona en masa los objetos que se le ingresen
    #Tienen que estar en un solo array
    def agregarMuchos(self, objetos):
        self.Lista = objetos

    #Fuerza desde el inicio registros de pedido en la DB
    def forzarPedir(self, personaInt, materialInt):
        self.Lista[personaInt].materiales[materialInt].pedir()
    #Fuerza desde el inicio registros de devolucion en la DB
    def forzarEnt(self, personaInt, materialInt):
        self.Lista[personaInt].materiales[materialInt].entregar()

    