from tkinter import StringVar
from tkinter import messagebox
from controllers.sitelinkController import sitelinkController
from models.customer import customers
from models.products import products
from models.settings import settings
from models.documentHdr import documentHdr
from models.documentDtls import documentDtls
from controllers.sitelinkController import sitelinkController as siteLink
import datetime

class invoicesController:

    def __init__(self):

        self.settings = settings()
        self.docHdr = documentHdr()
        self.docDtls= documentDtls()


        self.dateFrom = StringVar()
        self.dateTo  = StringVar()

                
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


        self.invoiceList = self.getInvoiceList()

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

    def getInvoiceList(self):

        fake_list = []
        fake_list.append( ( '01','Apcon consulting', 'Factura', '01-03-2022','3000.00', '0.00', 'NO EMITIDO' ) )
        fake_list.append( ('02','Apcon consulting', 'Factura', '01-03-2022','300.00',  '0.00', 'NO EMITIDO'  )  )

        # print(fake_list)
                    #   ('02','Apcon consulting', 'Factura', '01-03-2022','300.00',  '0.00', 'NO EMITIDO'  )  ]

        return fake_list 

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

    def extractInvoices(self):

        try:

            result = self.settings.selectByCondition({

                'columns' : ['val1','val2'] ,
                'condition' : f"key = 'CONF_DATASOURCE' and val2 = 'X'"
            })

            if len(result) > 0 :

                for item in result:
                   if item['val1'] == 'CONF_SITELINK_DB' : 
                       self.getDataFromSitelink()
                   if item['val1'] == 'CONF_QUICKBOOKS_API' : 
                        self.getDataFromQuickbooks()

            self.refreshTable()

          

        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")


    def getDataFromSitelink(self):
        # perform logic to get data from db
        controller = siteLink()
        result = controller.doQueryExtraction()
       
        if result != "" :
            i = 0

            dTotNeto = 0
            dTotITBMS = 0
            oldledger = 0

            for item in result :

                newledger = item['LedgerID']

                dValITBMS = item['Itbms']

                self.docDtls.dSecItem    = i
                self.docDtls.dCodProd    = item['ItemID']
                self.docDtls.dDescProd   = item['ItemDescription'] 
                self.docDtls.dCantCodInt = str(item['Qty'])
                self.docDtls.dPrUnit     = str(item['SubTotalPrice'])
                self.docDtls.dPrItem     = str(item['SubTotalPrice'] * item['Qty'])
                self.docDtls.dValTotItem = str(item['SubTotalPrice'] + dValITBMS)

                # itbm 00: 0% (excento) / 01:7% / 02:10% / 03:15%.
                self.docDtls.dTasaITBMS  = '01' 
                self.docDtls.dValITBMS   =  str(dValITBMS)


                values = self.docDtls.__dict__.copy()
                print(values )
                self.docDtls.insert( values  )


                # calculo de totales
                dTotNeto  = dTotNeto + item['SubTotalPrice']
                dTotITBMS = dTotITBMS + dValITBMS

                if oldledger != newledger :
                   
                   self.docHdr.iDoc = 1 
                   self.docHdr.dNroDF    = item['iInvoiceNum']
                   self.docHdr.dPtoFacDF = item['LocationCode']
                   self.docHdr.dFechaEm  = item['Date']
                   self.docHdr.iNatOp    = 1
                   self.docHdr.iTipoOp   = 1
                   self.docHdr.iDest   = 1
                   self.docHdr.iTipoTranVenta = 1
                   self.docHdr.dInfEmFE = item['sUnitName']
                   self.docHdr.customer_id = item['TenantID']

                    # completar parte de totales

                   valuesHdr = self.docHdr.__dict__.copy()
                   self.docHdr.insert( valuesHdr  )
                   
                   oldledger = newledger 
                
                i += 1
                
                return

              
        # messagebox.showinfo( message= 'getting from sitelink' , title="Info" )
        

    def getDataFromQuickbooks(self):
        return

    def refreshTable(self):
        return

    