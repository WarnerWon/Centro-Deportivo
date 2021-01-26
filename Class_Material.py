#Toda la funcionalidad de Material es en base al tiempo
#por eso inclui la libreria datetime para ello
import datetime

class Material(object):

    def __init__(self, myid, nombre):
        self.id = int(myid)
        self.nombre = str(nombre)
        self.fechaPedido = None
        self.fechaEntregado = None

    #Asigna la fecha actual, dando a entender 
    #que se pidio en esa fecha
    def pedir(self):

        self.fechaPedido = datetime.datetime.now()

        pass
    #Asigna la fecha actual, dando a entender 
    #que se devolvio en esa fecha

    def entregar(self):
        
        self.fechaEntregado = datetime.datetime.now()
        
        pass

    def asignarPedir(self,date):

        self.fechaPedido = date

        pass

    def asignarEntregar(self,date):

        self.fechaEntregado = date

        pass
