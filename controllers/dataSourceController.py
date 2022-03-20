from tkinter import messagebox
from models.settings import settings


class dataSourceController:

    def __init__(self):  

        self.model = settings()
        self.settingKey = 'CONF_DATASOURCE'
        self.initVal()
       
    def initVal(self):

       self.list = self.getSettingsByKey(self.settingKey)


    def setActiveSource(self, source,state):
       
        id = ''  
        data = self.model.selectByCondition({
    
            'columns' : ['id'] ,
            'condition' : f"key = 'CONF_DATASOURCE' and val1 = '{source}'"

        })

        if len(data) > 0:
            id = data[0]['id'] 
            val =  {
                        "key"  : 'CONF_DATASOURCE',
                        "count" : 1,
                        "val1" : source,
                        "val2" : state,
                        "val3" : '',
                        "val4" : ''
                    }
       
            self.model.update( id , val)
        
    def save(self):

        try:
            # conect to database
            sqlService = SQLConnect({ 'server' : self.val1.get() , 'dbname': 'sldbclnt' , 'user' : self.val2.get(), 'pass' : self.val3.get() })

            isConnect = sqlService.TestConnect()

            if isConnect == True:
                isOk = self.CheckInput()
            
                if isOk == True:
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
                    'condition' : f"key = '{self.settingKey}'",

                    })

                    if len(data) > 0:
                        id = data[0]['id'] 
                
                    if id != "" :
                        res = self.model.update(id,values)
                    else: 
                        res = self.model.insert(values)
                
                    if res == True : 
                        messagebox.showinfo("info","La configuracion de ha guardado correctamente")

            
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

            'columns' : ['val1','val2'] ,
            'condition' : f"key = '{key}'"
        }

        return self.model.selectByCondition(filter)


    def delete(self,id):
         self.model.delete(id)
