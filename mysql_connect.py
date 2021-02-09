import mysql.connector as BD

class Mysql():

  def __init__(self):
    self.mydb = BD.connect(
      host="127.0.0.1",
      user="root",
      password="",
      database="centrodeportivo",
      port=3307
    )
    self.mycursor= self.mydb.cursor()

  def insert(self,table="",data={}):

    sql = self.sentenceGenerator("INSERT",table,data.keys())
    
    myInput = self.valuesGenerator(data.values())

    self.mycursor.execute(sql,myInput)

    self.mydb.commit()

  def select(self,table="",selection="*",whereField="",operator="",value=""):
    sql = "SELECT " + selection + " FROM " + table
    if (whereField!=None):
      sql =+ " WHERE " + whereField + " " + operator + " " + value
  
  def update(self,table="",field="", value="", wherefield="", operator="=", whereValue=""):

    sql = "UPDATE %s SET %s = %s WHERE %s %s %s"
    
    val = (table, field, value, wherefield, operator, whereValue)
    
    self.mycursor.execute(sql, val)

    self.mydb.commit()

  def delete(self, table="",whereField="",whereValue=""):
    mycursor = mydb.cursor()
    sql = "DELETE FROM %s WHERE %s = %s"
    values = (table,whereField,whereValue)
    mycursor.execute(sql,values)
    mydb.commit()

  def sentenceGenerator(self, action="", table="", keys=[]):
    parentesis = "( "
    val_count = "("

    for key in keys:
      parentesis += key
      parentesis += ", " 
      val_count += "%s,"

    parentesis = parentesis[:-2]
    val_count = val_count[:-1]
    parentesis += ")"
    val_count +=")"

    sql = action + " INTO " + table + " " + parentesis + " VALUES " + val_count

    return sql
    
  def valuesGenerator(self, values):
    
    newValues = []
    for val in values:
      newValues.append(val)
    myInput = tuple(newValues)

    return myInput

if __name__ == "__main__":

  centroDep = Mysql()
  centroDep.insert("materiales",{"nombre":"Bolsa"})

  
  

