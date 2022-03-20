from tkinter import BooleanVar, StringVar
from tkinter import messagebox
from models.company import company
from services.SQL.SQLConnect import SQLConnect

class companyController:

    def __init__(self):  

        self.model = company()

        self.dNombEm = StringVar()
        self.dSucEm    = StringVar()
        self.dCoordEm    = StringVar()
        self.dDirecEm    = StringVar()
        self.dTfnEm    = StringVar()
        self.dCorElectEmi   = StringVar()
        self.dRuc   = StringVar()
        self.dTipoRuc   = StringVar()
        self.dDV   = StringVar() 
        self.gUbiEm   = StringVar() 
        self.dCodUbi   = StringVar() 
        self.dCorreg   = StringVar() 
        self.dDistr   = StringVar() 
        self.dProv   = StringVar() 

        self.tpContList = ['Natural', 'Juridico']
    
        self.tpSelected = StringVar()
       

        self.initVal()
       
    def initVal(self):
        
        data =self.model.selectByCondition({
    
            'columns' : '*' ,
            'condition' : f"id = '1'",

        })

        data = data[0]
        if len(data) > 0:
            if  data['dTipoRuc'] != '':
                if  data['dTipoRuc'] == 1: 
                    self.tpSelected.set( self.tpContList[0] )
                else:
                    self.tpSelected.set( self.tpContList[1] )  

            self.dNombEm.set( data['dNombEm'])
            self.dSucEm.set( data['dSucEm'])
            self.dCoordEm.set( data['dCoordEm'])
            self.dDirecEm.set( data['dDirecEm'])
            self.dTfnEm.set( data['dTfnEm'])
            self.dCorElectEmi.set( data['dCorElectEmi'])
            self.dRuc.set( data['dRuc'])
         
            self.dDV.set( data['dDV'])
            self.dCodUbi.set( data['dCodUbi'])
            self.dCorreg.set( data['dCorreg'])
            self.dDistr.set( data['dDistr'])
            self.dProv.set( data['dProv'])

        return

        
    def save(self):

        try:
            dTipoRuc = 0
            
            if self.tpSelected.get() == "Natural":
                dTipoRuc = 1
            elif self.tpSelected.get() == "Juridico": 
                dTipoRuc = 2

          
            self.model.dNombEm  = self.dNombEm.get()
            self.model.dSucEm  = self.dSucEm.get()
            self.model.dCoordEm  = self.dCoordEm.get()
            self.model.dDirecEm  = self.dDirecEm.get()
            self.model.dTfnEm  = self.dTfnEm.get()
            self.model.dCorElectEmi  = self.dCorElectEmi.get()
            self.model.dRuc  = self.dRuc.get()
            self.model.dTipoRuc  = dTipoRuc
            self.model.dDV  = self.dDV.get()
            self.model.dCodUbi  = self.dCodUbi.get()
            self.model.dCorreg  = self.dCorreg.get()
            self.model.dDistr  = self.dDistr.get()
            self.model.dProv  = self.dProv.get()

            data =self.model.selectByCondition({
        
                'columns' : ['id'] ,
                'condition' : f"id = '1'",

            })

            values = self.model.__dict__.copy()

            if len(data) > 0:
                id = data[0]['id'] 
        
            if id != "" :
                res =self.model.update(id,values)
            else: 
                res =self.model.insert(values)
            if res :
                messagebox.showinfo("info", "Se han actualizado los datos correctamente")
            
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

        returnself.selectByCondition(filter)

    def setSettingsInfoValues(self, values):

        values = values[0]
        
        self.key.get(values[1]),
        self.count.get(values[2]),
        self.val1.get(values[3]),
        self.val2.get(values[4]),
        self.val3.get(values[5]),
        self.val4.get(values[6]),

       

    def delete(self,id):
        self.delete(id)
