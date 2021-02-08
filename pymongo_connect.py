import pymongo

class Mymongo():

    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb+srv://israel:2409@centrodeportivo.6fuhl.mongodb.net/<dbname>?retryWrites=true&w=majority")
        self.mydb = self.myclient['centrodeportivo']

    def select(self, collection="", query={}):        
        mycol = mydb[collection]
        x = mycol.find({})
        return x
        
    def insert(self, collection="", data={}):

        mycollection = self.mydb[collection]
        
        x = mycollection.insert_one(data)

    def update(self, collection="", query="",newValues=""):
        mycollection = self.mydb[collection]
        mycollection.update_one(query,newValues)

    def delete(self, collection="",query={}):
        mycollection = self.mydb[collection]

        mycollection.delete_one(query)


if __name__ == "__main__":
    
    db = Mymongo()
    
    print(db.myclient.list_database_names())

    db.insert('personas',{
                "nombre":"Cesar",
                "edad":21,
                "puesto":"estudiante",
                "materiales":[{
                    "id": 1,
                    "nombre": "Balon-basket",
                    "fechaPedido": "2020-12-24",
                    "fechaEntregado": "2020-12-29",
                    }]
                }
            )

