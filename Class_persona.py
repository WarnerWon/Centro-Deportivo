#Al separar el array de persona de su clase, este deja
#muy vacia la clase, aún así es necesaria.
#La mayoria de los atributos de esta clase son de tipo comunes.
#El unico que destaca es el array de materiales.

class Persona(object):

  def __init__(self, nombre:str, edad:int, puesto:str, materiales:[]):
    self.nombre = nombre
    self.edad = edad
    self.puesto = puesto
    self.materiales = materiales

  #Añade una copia de un registro de la DB y 
  #cambia sus parametros de fechas en None para despues 
  #crear la fecha de pedido a la hora actual.
  #Esto debido a como funciona la memoria en Python, 
  #donde si se clona un objeto y modifica en el original
  #la copia misma tambien se modifica. Esta solucion evita que se 
  #copien materiales con fechas ya incluidas (Problema a largo uso)
  def añadirMat(self, matObject):
    material = matObject
    material.fechaEntregado = None
    material.fechaPedido = None
    self.materiales.append(matObject)
    self.materiales[-1].pedir()
