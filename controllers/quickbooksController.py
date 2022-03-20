from tkinter import BooleanVar, StringVar
from tkinter import messagebox
from models.settings import settings
from services.SQL.SQLConnect import SQLConnect

class quickbooksController:

    def __init__(self):  

        self.model = settings()
        self.settingKey = 'CONF_QUICKBOOKS_API'
        self.initVal()
       
    def initVal(self):

        initvaues = self.getSettingsByKey(self.settingKey )

        self.key  =  StringVar()
        self.count  =  StringVar()
        self.val1 = StringVar()
        self.val2 = StringVar()
        self.val3  = StringVar()
        self.val4  = StringVar()

        self.connString = ""
      
        self.default = BooleanVar()

        self.default.set(False)

        if len(initvaues) > 0:

            self.val1.set( initvaues[0][3] ) 
            self.val2.set( initvaues[0][4] ) 
            self.val3.set( initvaues[0][5] ) 
            self.val4.set( initvaues[0][6] ) 

            self.connString = { 'server' : initvaues[0][3], 
                                'dbname': 'sldbclnt' , 
                                'user' : initvaues[0][4], 
                                'pass' : initvaues[0][5] }
            

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
                        id = data[0][0] 
                
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
