import pyodbc 
from tkinter import messagebox

class SQLConnect:


    def __init__(self,params):  
    
        self.driver = '{SQL Server}'
        self.server = params['server']
        self.dbname = params['dbname']
        self.user = params['user']
        self.pw = params['pass']

        # self.connection = None
      


    def OpenConnection(self):
        stringCon = f"Driver={self.driver}; Server={self.server}; Database={self.dbname}; UID={self.user}; PWD={self.pw};"
        self.connection = pyodbc.connect(stringCon)



    def  CloseConnection(self):
        self.connection.close()


    def execute(self,query):

        self.OpenConnection()
        cursor =  self.connection.cursor()
       
        cursor.execute(query)
        query_result = [ dict(line) for line in [zip([ column[0] for column in cursor.description], row) for row in cursor.fetchall()] ]
        # row  = cursor.fetchall()
        cursor.close()

        return query_result 


    def TestConnect(self):
        
        try:

            self.OpenConnection()

            row = self.execute('SELECT @@VERSION as version')

            while 1: 
                if not row:
                    return False
                    break
                self.CloseConnection()
                return True

            
        except Exception as e: 

            messagebox.showerror(title="Error", message= str(e))
            return False
      
