from pymongo_connect import Mymongo
from mysql_connect import Mysql
class BD():

  def __init__(self,db_name=''):
    self.mydb = db_name
    if (mydb=="mysql"):
      self.m1sql = Mysql()
    else:
      self.m1mongo = Mymongo()
  
  def insert(self,table_collection="",data={}):
    if (self.mydb=="mysql"):
      self.m1sql.insert(table=table_collection,data=values)
    else:
      self.m1mongo.insert(collection=table_collection,data=values)
  
  def select(self,table_collection="",data={}):
    if (self.mydb=="mysql"):
      if 'whereField' in data:
        self.m1sql.select(table=table_collection,
          selection=data.get('selection'),
          whereField=data.get('where'),
          operator=data.get('operator'),
          value=data.get('value')
          )
      else:
        self.m1sql.select(table=table_collection,
          selection=data.get('selection'),
          whereField=None,
          operator=None,
          value=None
          )
    else:
      self.m1mongo.select(collection=table_collection,query=data)

  def update(self, table_collection="",query={},newValue={}):
    if (self.mydb == "mysql"):
      self.m1sql.update(table=table_collection,
        field=newValue.get('field'),
        value=newValue.get('value'),
        whereField=query.get('field'),
        operator=query.get('operator'),
        whereValue=query.get('value'))
    else:
      self.m1mongo.update(collection=table_collection,query=query,newValue=newValue)
    
  #def delete(self,table_collection="",):
      