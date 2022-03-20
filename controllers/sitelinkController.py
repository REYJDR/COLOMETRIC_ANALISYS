from tkinter import BooleanVar, StringVar
from tkinter import messagebox
from models.settings import settings
from services.SQL.SQLConnect import SQLConnect
from helpers import helper
from io import open
import json

class sitelinkController:


    def __init__(self):  

        self.model = settings()
        self.settingKey = 'CONF_SITELINK_DB'
        self.dbName = 'sldbclnt'
        self.initVal()
       

    def initVal(self):

        initvaues = self.getSettingsByKey(self.settingKey)
        # print(  initvaues )
        self.key  =  StringVar()
        self.count  =  StringVar()
        self.val1 = StringVar()
        self.val2 = StringVar()
        self.val3  = StringVar()
        self.val4  = StringVar()

        self.connString = ""
      
        if len(initvaues) > 0:

            self.val1.set( initvaues[0]['val1'] ) 
            self.val2.set( initvaues[0]['val2'] ) 
            self.val3.set( initvaues[0]['val3'] ) 
            self.val4.set( initvaues[0]['val4'] ) 

            self.connString = { 'server' : initvaues[0]['val1'], 
                                'dbname': f"{self.dbName}" , 
                                'user' : initvaues[0]['val3'], 
                                'pass' : initvaues[0]['val4'] }
            

    def clearData(self):
  
        self.key.set('')
        self.count.set('')
        self.val1.set('')
        self.val2.set('')
        self.val3.set('')
        self.val4.set('')
        # self.default.set(False)
        
        
    def save(self):

        try:
            # conect to database
            sqlService = SQLConnect({ 'server' : self.val1.get() , 'dbname': f"{self.dbName}" , 'user' : self.val2.get(), 'pass' : self.val3.get() })

            isConnect = sqlService.TestConnect()

            if isConnect == True:
                isOk = self.CheckInput()
            
                if isOk == True:
                    self.saveInDb()
            else:
                 self.deleteSource() 
                   
                    
            
        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")

    def CheckInput(self):

        errorStr = "Valide que todos los campos han sido capturados"

        if self.val1.get() == '' :
            messagebox.showerror(message=errorStr , title="Error")
            return False

        if self.val2.get() == '' :

            messagebox.showerror(message=errorStr , title="Error")
            return False

        if self.val3.get() == '' :
                messagebox.showerror(message=errorStr , title="Error")
                return False


        return True

    def getSettingsByKey(self,key):
       
        filter = {

            'columns' : '*' ,
            'condition' : f"key = '{key}'"
        }

        return self.model.selectByCondition(filter)

    def setSettingsInfoValues(self, values):

        values = values[0]
        
        self.key.get(values[1]),
        self.count.get(values[2]),
        self.val1.get(values[3]),
        self.val2.get(values[4]),
        self.val3.get(values[5]),
        self.val4.get(values[6]),

    def delete(self,id):
         self.model.delete(id)

    def doQueryExtraction(self):
        
        LocationsCodes =  self.val4.get() 

        ruta = helper.find_data_file('SITELINK_ALMACENAJE.sql')
        script = open(ruta,"r")
        query = script.read()

        if  LocationsCodes != "" :
            addCondition = f" and  S.sLocationCode in ({LocationsCodes}) ;"
            query = f"{query} {addCondition}"

   
        try:
            # conect to database
            sqlService = SQLConnect({ 'server' : self.val1.get() , 'dbname': f"{self.dbName}" , 'user' : self.val2.get(), 'pass' : self.val3.get() })

            isresult = sqlService.execute( query )

            if isresult != None :

              return isresult
             
            else:
                
              return "" 
                   
                    
        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")
  
    # def doQuery(self,input):

    #     try:
    #         query = input.get("1.0", "end-1c")

    #         sqlService = SQLConnect(self.connString)
           

    #         return sqlService.execute( query )

            
    #     except Exception as e :
    #         messagebox.showerror(message=str(e) , title="Error")

    def saveInDb(self):

        values =  {
                "key"  : f"{self.settingKey}",
                "count" : 1,
                "val1" : self.val1.get(),
                "val2" : self.val2.get(),
                "val3" : self.val3.get(),
                "val4" : self.val4.get(),
            } 

        id = ''  

        data = self.model.selectByCondition({
    
            'columns' : ['id'] ,
            'condition' : f"key = '{self.settingKey}'"

        })

        if len(data) > 0:
            id = data[0]['id'] 
    
        if id != "" :
            res = self.model.update(id,values)
        else: 
            res = self.model.insert(values)

        if res == True : 
            self.saveSource() 
            messagebox.showinfo("info","La configuracion de ha guardado correctamente")
        else:
            self.deleteSource() 
            

    def saveSource(self):

        id = ''  

        data = self.model.selectByCondition({
    
            'columns' : ['id'] ,
            'condition' : f"key = 'CONF_DATASOURCE' and val1 = '{self.settingKey}'"

        })

        if len(data) > 0:
            id = data[0]['id'] 
    
        if id == "" :
           
            self.model.insert({
                                "key"  : 'CONF_DATASOURCE',
                                "count" : 1,
                                "val1" : self.settingKey,
                                "val2" : 'X',
                                "val3" : '',
                                "val4" : ''
                            } )

    def deleteSource(self):

        id = ''  
        data = self.model.selectByCondition({
            'columns' : ['id'] ,
            'condition' : f"key = 'CONF_DATASOURCE' and val1 = '{self.settingKey}'"
        })

        if len(data) > 0:
            id = data[0]['id'] 
    
        if id != "" :            
            self.model.delete( id)
        
        