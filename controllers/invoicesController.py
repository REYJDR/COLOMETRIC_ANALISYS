from tkinter import StringVar
from tkinter import messagebox

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

    def getTaxList(self):
        return { "0" : "Excento",
                 "7" : "Itbms 7%",
                 "15" : "Itbms 15%" }
  
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
