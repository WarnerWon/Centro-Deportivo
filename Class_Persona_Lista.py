class Persona_Lista:

    def __init__(self, Lista:[]):
        self.Lista = Lista

    def buscarPersona(self, nombre):
        for persona in self.Lista:
            if persona.nombre == nombre:
                return persona
    
    def añadirPersona(self, persona):
        self.Lista.append(persona)

    def agregarMuchos(self, objetos):
        self.Lista = objetos

    def forzarPedir(self, personaInt, materialInt):
        self.Lista[personaInt].materiales[materialInt].pedir()
    def forzarEnt(self, personaInt, materialInt):
        self.Lista[personaInt].materiales[materialInt].entregar()

    