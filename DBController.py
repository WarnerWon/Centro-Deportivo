from pymongo_connect import Mymongo
from mysql_connect import Mysql
class BD():

  def __init__(self,db_name=''):
    self.mydb = db_name
    if (mydb=="mysql"):
      self.mysql = Mysql()
    else:
      self.mymongo = Mymongo()
  
  #def insert(self,table_collection="",values={}):
  #  if