from tkinter import StringVar
from tkinter import messagebox
from models.products import products


class productsController:


    def __init__(self):  

        self.model = products()
        self.initVal()
       
    def initVal(self):

        self.id  =  StringVar()
        self.dCodProd  =  StringVar()
        self.dDescProd  =  StringVar()
        self.cUnidad = StringVar()
        self.dFechaFab = StringVar()
        self.dFechaCad  = StringVar()
        self.dPrUnit = StringVar()
        self.Taxable = StringVar()
  
    def clearData(self):
        
        self.id.set('')
        self.dCodProd.set('')
        self.dDescProd.set('')
        self.cUnidad.set('')
        self.dFechaFab.set('')
        self.dFechaCad.set('')
        self.dPrUnit.set('')
        self.Taxable.set('')

    def save(self):

        try:
        
            values =  {
                        "dCodProd"  : self.dCodProd.get(),
                        "dDescProd" : self.dDescProd.get(),
                        "cUnidad" : self.cUnidad.get(),
                        "dFechaFab"  : self.dFechaFab.get(),
                        "dFechaCad" : self.dFechaCad.get(),
                        "dPrUnit" : self.dPrUnit.get(),
                        "Taxable" : self.Taxable.get()
                    } 
                    
            id = self.id.get() 
            
            if id != "" :
                res = self.model.update(id,values)
            else: 
                res = self.model.insert(values)
          

            if res == True : 
                messagebox.showinfo("info","Se ha guardado el producto correctamente")
        
        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")

    def getProductList(self,columns):
        return self.model.selectAll(columns)
    
    def getProductById(self,id):
       
        filter = {

            'columns' : '*' ,
            'condition' : f"id = '{id}'"
        }

        return self.model.selectByCondition(filter)

    def setProductInfoValues(self, values):

        values = values[0]
        
        self.id.set(values[0])
        self.dCodProd.set(values[1])
        self.dDescProd.set(values[2])
        self.cUnidad.set(values[3])
        self.dFechaFab.set(values[4])
        self.dFechaCad.set(values[5])
        self.dPrUnit.set(values[6])
        self.Taxable.set(values[7])


    def delete(self,id):
         self.model.delete(id)