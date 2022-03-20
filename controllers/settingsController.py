from tkinter import StringVar
from tkinter import messagebox
from models.settings import settings


class settingsController:


    def __init__(self):  

        self.model = settings()
        self.initVal()
       
    def initVal(self):

        self.id  =  StringVar()
        self.key  =  StringVar()
        self.count  =  StringVar()
        self.val1 = StringVar()
        self.val2 = StringVar()
        self.val3  = StringVar()
        self.val4 = StringVar()
  
    def clearData(self):
        
        self.id.set('')
        self.key.set('')
        self.count.set('')
        self.val1.set('')
        self.val2.set('')
        self.val3.set('')
        self.val4.set('')
        
    def save(self):

        try:
            # conect to database

            
        
            values =  {
                        "key"  : 'CONF_SITELINK_DB',
                        "count" : 1,
                        "val1" : self.val1.get(),
                        "val2"  : self.val2.get(),
                        "val3" : self.val3.get(),
                        "val4" : self.val4.get(),
                    } 
                    

            data = self.model.selectByCondition({

            'columns' : ['id'] ,
            'condition' : "key = 'CONF_SITELINK_DB'"

             })

            id = data[0][0] 
           

            if id != "" :
                res = self.model.update(id,values)
            else: 
                res = self.model.insert(values)
          
            if res == True : 
                messagebox.showinfo("info","La configuracion de ha guardado correctamente")
        
        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")



    def getSettingsByKey(self):
       
        filter = {

            'columns' : '*' ,
            'condition' : "key = 'CONF_SITELINK_DB'"
        }

        return self.model.selectByCondition(filter)

    def setSettingsInfoValues(self, values):

        values = values[0]
        
        self.id.set(values[0])
        self.key.get(values[1]),
        self.count.get(values[2]),
        self.val1.get(values[3]),
        self.val2.get(values[4]),
        self.val3.get(values[5]),
        self.val4.get(values[6]),
       

    def delete(self,id):
         self.model.delete(id)