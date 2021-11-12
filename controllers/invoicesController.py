from tkinter import StringVar
from tkinter import messagebox
from models.customer import customers
from models.products import products

class invoicesController:

    def __init__(self):
                
        self.RUC = StringVar()
        self.DV = StringVar()
        self.Nombre = StringVar()
        self.Contacto = StringVar()
        self.Term = StringVar()

        self.NoInv = StringVar()
        self.Term = StringVar()
        self.Date = StringVar() 
        self.Tax = StringVar()
        self.NoInv.set('FAC0001')

        self.cantidad = StringVar()
        self.subtotal = StringVar()
        self.tax = StringVar()
        self.total = StringVar()
        self.payment = StringVar()
        self.discount = StringVar()

        #gPedComGl
        self.dNroPed = StringVar()
        self.dNumAcept= StringVar()
        self.dInfEmPedGl= StringVar()

    def getTaxList(self):
        return { "0" : "Excento",
                 "7" : "Itbms 7%",
                 "15" : "Itbms 15%" }
  
    def getProductList(self):
        columns = ( 
                    "id ",
                    "dCodProd" ,
                    "dDescProd" ,
                    "dPrUnit" 
                   )
        model = products()
        res = model.selectAll(columns)
        return res

    def getCustomerList(self):
        columns = ( 
                    "id ",
                    "dNombRec" ,
                    "dRuc"  
                   )
        model = customers()
        res = model.selectAll(columns)
        return res

    def getCustomerInfo(self,id):
        
        filter = {

            'columns' : '*' ,
            'condition' : f"id = '{id}'"
        }

        model = customers()
        return model.selectByCondition(filter)


    def save(self):
        
        try:

            ask = messagebox.askquestion("Crear factura", "¿Desea crear generar la factura?")

            if ask == 'yes':

                invHeader = {
                    "RUC" : self.RUC.get(),
                    "DV" : self.DV.get(),
                    "Name" : self.Nombre.get(),
                    "Contact" : self.Contacto.get(),
                    "Term" : self.Term.get(),
                    "NoInv" : self.NoInv.get(),
                    "Date" : self.Date.get(),
                    "Tax" : self.Tax.get(),
                }
                
                messagebox.showinfo("info",invHeader)

            else: 

               messagebox.showinfo("Creacion cancelada","Se ha cancelado la generación de esta factura")

        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")
