class Persona(object):

  def __init__(self, nombre:str, edad:int, puesto:str, materiales:[]):
    self.nombre = nombre
    self.edad = edad
    self.puesto = puesto
    self.materiales = materiales

  def añadirMat(self, matObject):
    material = matObject
    material.fechaEntregado = None
    material.fechaPedido = None
    self.materiales.append(matObject)
    self.materiales[-1].pedir()
