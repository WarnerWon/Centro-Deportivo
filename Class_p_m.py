#El nombre del archivo significa Clase de Persona y Material
#Haciendo referencia a una relacion de 1 a Muchos en modelo entidad relacion

#Se importan las clases a usar
from Class_Persona_Lista import Persona_Lista
from Class_persona import Persona
from Class_Material import Material
from test import FileManager
#Se inicializa la BD

#Tabal de Personas
lPerson = Persona_Lista([])

#Tabla de Materiales
mLista = FileManager.readFile('materials',[])

#Serializacion--------

#Se insertan datos a la tabla de personas
#En este caso al array se le insertan objetos tipo Persona
#El array de Materiales de la clase Persona es llenado
    #en base a la tabla de Materiales.

lPerson.agregarMuchos(FileManager.readFile('persons',mLista))



#Se fuerzan devoluciones y pedidos a los usuarios se pre crearon en DB

