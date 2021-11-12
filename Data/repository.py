import json
from io import open
import sqlite3
import mysql.connector
from helpers import helper

from tkinter import messagebox

class repository : 
    
    db_conexion = None

    def __init__(self):
  
        try:
           

            ruta = helper.find_data_file('config.json')
            config = open(ruta,"r")
            
            data = json.load(config)

            type    = data['database']['db_type']
            db_name = data['database']['db_name'] 
            db_mysql_host = data['database']['db_mysql_host'] 
            db_mysql_user = data['database']['db_mysql_user'] 
            db_mysql_pass = data['database']['db_mysql_pass'] 


            if type == "sqlite" : 

                self.db_conexion = sqlite3.connect(db_name)
                self.cursor = self.db_conexion.cursor()

                has_tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

                if len(has_tables.fetchall()) == 0 : 
                    self.createTables()
               

            elif type == "mysql" :

                self.db_conexion = mysql.connector.connect(

                    host = db_mysql_host,
                    user = db_mysql_user,
                    passw = db_mysql_pass,
                    database = db_name,

                )
                self.cursor = self.db_conexion.cursor()
            else: 
                messagebox.showerror(title="Error", message= "No existe conexion a DB establecida") 


        except Exception as e: 
            messagebox.showerror(title="Error", message= str(e))
        finally:
            config.close()

    def createTables(self):

        try :     

            ruta = helper.find_data_file("db_script.sql")
            script = open(ruta,"r")
            self.db_conexion.executescript(script.read())
            has_tables = self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            print(has_tables.fetchall())
        except Exception as e: 
            messagebox.showerror(title="Error", message= str(e))

    def insert(self,dataValue):

        try :     
            table = self.__class__.__name__

            # Get all "keys" inside "values" key of dictionary (column names)
            columns = ', '.join(dataValue.keys())  

            # Get all "values" inside "values" key of dictionary (insert values)
            data =   ', '.join(['?' for s in dataValue])

            listValues = list(dataValue.values())
            query = f"INSERT INTO {table} ({columns}) VALUES ({data})"
            self.cursor.execute( query , tuple(listValues))

            self.db_conexion.commit()
           
            return True

        except Exception as e: 
            messagebox.showerror(title="Error", message= str(e))

    def select(self,dataValue):

        try :     
            table = dataValue["table"]  # Get name of the table

            # # Get all "keys" inside "values" key of dictionary (column names)
            # columns = ', '.join(dataValue["values"].keys())  

            # # Get all "values" inside "values" key of dictionary (insert values)
            # data =   ', '.join(['?' for s in dataValue["values"]])

            # listValues = list(dataValue["values"].values())

            query = f"select * from {table}"
            self.cursor.execute( query )

            self.db_conexion.commit()

           
            return self.cursor.fetchall()

        except Exception as e: 
            messagebox.showerror(title="Error", message= str(e))
    
    def selectAll(self, columns = None):
        
        try :   
            table = self.__class__.__name__

            # # Get all "keys" inside "values" key of dictionary (column names)
            if len(columns) > 0:
                columns = ', '.join(columns)  
            else: 
                columns = "*"

            query = f"select {columns} from {table}"
            self.cursor.execute( query )

            self.db_conexion.commit()

           
            return self.cursor.fetchall()

        except Exception as e: 
            messagebox.showerror(title="Error", message= str(e))
       
    def selectByCondition(self, filter): 
   
        try :   
            table = self.__class__.__name__

            columns = filter['columns']
            condition = filter['condition']
        
            if len(columns) > 0:
                columns = ', '.join(columns)  
            else: 
                columns = "*"

            clause = f" where {condition}"

            query = f"select {columns} from {table} {clause}"
            self.cursor.execute( query )
            self.db_conexion.commit()
           
            return self.cursor.fetchall()

        except Exception as e: 
            messagebox.showerror(title="Error", message= str(e))

    def update(self,id,dataValue):

        try :     
            table = self.__class__.__name__

            # Get all "values" inside "values" key of dictionary (insert values)
            data =   ",".join([f"'{k}' = ?" for k in dataValue.keys()])
           
            valuesList = list(dataValue.values())
            valuesList.append(id)
            query = f"UPDATE {table} set {data} WHERE id = ?"
            self.cursor.execute( query , tuple(valuesList) )

            self.db_conexion.commit()
           
            return True

        except Exception as e: 
            messagebox.showerror(title="Error", message= str(e))

    def delete(self,id): 

        try :     
            table = self.__class__.__name__

            query = f"DELETE FROM {table} WHERE id = ?"
            self.cursor.execute( query , [id])
            self.db_conexion.commit()
           
            return True

        except Exception as e: 
            messagebox.showerror(title="Error", message= str(e))

