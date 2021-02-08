from Class_Persona_Lista import Persona_Lista
from Class_persona import Persona
from Class_Material import Material
from test import FileManager
lPerson = Persona_Lista([])

mLista = FileManager.readFile('materials',[])

lPerson.agregarMuchos(FileManager.readFile('persons',mLista))

