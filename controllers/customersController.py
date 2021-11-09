from tkinter import StringVar
from tkinter import messagebox
from models.customer import customers


class customersController:


    def __init__(self):  

        self.model = customers()
        self.initVal()
    
    def initVal(self):

        self.id  =  StringVar()
        self.iTipoRec  =  StringVar()
        self.dTipoRuc = StringVar()
        self.dRuc = StringVar()
        self.dDV  = StringVar()
        self.dNombRec = StringVar()
        self.dTfnRec = StringVar()
        self.dCorElectRec = StringVar()  
        self.dDirecRec = StringVar()  
  
    def clearData(self):
        
        self.id.set('')
        self.dNombRec.set('')
        self.dTipoRuc.set('')
        self.iTipoRec.set('')
        self.dRuc.set('')
        self.dDV.set('')
        self.dDirecRec.set('')
        self.dTfnRec.set('')
        self.dCorElectRec.set('')

    def tipoContribuyentes(self):

        return {
            "1" :  "Natural",
            "2" :  "Juridico"
        }

    def tipoReceptor(self):

        return {
            "1": "Contribuyente",
            "2": "Consumidor final",
            "3": "Gobierno",
            "4" : "Extranjero"
        }

    def saveCustomer(self):
        try:
        
            customerInfo = {
                        "iTipoRec"  : self.iTipoRec.get(),
                        "dTipoRuc" : self.dTipoRuc.get(),
                        "dRuc" : self.dRuc.get(),
                        "dDV"  : self.dDV.get(),
                        "dNombRec" : self.dNombRec.get(),
                        "dTfnRec" : self.dTfnRec.get(),
                        "dCorElectRec" : self.dCorElectRec.get(),
                        "dDirecRec" : self.dDirecRec.get()
                    } 
           
            id = self.id.get() 
            
            if id != "" :
                res = self.model.update(id,customerInfo)
            else: 
                res = self.model.insert(customerInfo)

            if res == True : 
                 messagebox.showinfo("info","Se ha guardado el cliente correctamente")
                
            
        
        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")
    
    def getCustomerList(self,columns):
        return self.model.selectAll(columns)
    
    def getCustomerById(self,id):
       
        filter = {

            'columns' : '*' ,
            'condition' : f"id = '{id}'"
        }

        return self.model.selectByCondition(filter)

    def setCustInfoValues(self, values):

        values = values[0]
        
        self.id.set(values[0])
        self.dNombRec.set(values[1])
        self.dTipoRuc.set(values[2])
        self.iTipoRec.set(values[3])
        self.dRuc.set(values[4])
        self.dDV.set(values[5])
        self.dDirecRec.set(values[6])
        self.dTfnRec.set(values[11])
        self.dCorElectRec.set(values[12])
    
    def deleteCustomer(self,id):

        self.model.delete(id)