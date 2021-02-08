import datetime

class Material(object):

    def __init__(self, myid, nombre):
        self.id = int(myid)
        self.nombre = str(nombre)
        self.fechaPedido = None
        self.fechaEntregado = None

    def pedir(self):

        self.fechaPedido = datetime.datetime.now()

        pass

    def entregar(self):
        
        self.fechaEntregado = datetime.datetime.now()
        
        pass

    def asignarPedir(self,date):

        self.fechaPedido = date

        pass

    def asignarEntregar(self,date):

        self.fechaEntregado = date

        pass
