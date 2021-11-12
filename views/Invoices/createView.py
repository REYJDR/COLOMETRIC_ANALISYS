from tkinter import IntVar
from tkinter.constants import N, NE, S, TRUE, W
from controllers.invoicesController import *
from helpers import helper


class view:

    def __init__(self, program):
        self.functions = helper()

        self.program = program
        self.controller = invoicesController()
        self.frame_bgc = "#f5f5f5"

        self.items = []

        self.productList = self.controller.getProductList()
        self.searchProd = StringVar()
        self.searchProd.trace("w", lambda name, index, mode : self.filterList('items') )

        self.customerList = self.controller.getCustomerList()
        self.searchCust = StringVar()
        self.searchCust.trace("w", lambda name, index, mode : self.filterList('customers') )
        
    def index(self):

        try:
            # 6 rows - 
            self.program.header("Crear Factura")

            general_info_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos='NW', Margin = 5, Bg=self.frame_bgc)

            self.program.newLabel(  LabelName = "# Factura :", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newLabel(  LabelName = "FAC0001", Row = 0, Col = 1, into_frame = general_info_frame)

            self.program.newLabel(  LabelName = "Fecha :", Row = 1, Col = 0, Bg=self.frame_bgc ,into_frame = general_info_frame)
            self.program.newEntry(  Row = 1, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.Date, into_frame = general_info_frame)
            self.program.newButton( Name='...',Row = 1, Col = 3, Pos = 'W', Command= lambda : self.dateKeeper(), into_frame = general_info_frame)
            
            self.program.newLabel(  LabelName = "Itbms:",Bg=self.frame_bgc, Row = 2, Col = 0, into_frame = general_info_frame)
            self.program.newOptionMenu( SelectedOption = self.controller.Tax, Row = 2, Col = 1, Pos = 'W', Long = 5, options=self.controller.getTaxList(), into_frame = general_info_frame)
            
            customer_frame =  self.program.newFrame(Row = 0 , Col = 1, Pos='NE', Margin = 5, Bg=self.frame_bgc)
            
            self.program.newLabel(  LabelName = "RUC :", Pos = 'W', Row = 0, Col = 0, Bg=self.frame_bgc ,into_frame = customer_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.RUC, into_frame = customer_frame)
            self.program.newButton( Name='...',Row = 0, Col = 2, Pos = 'W', Command= lambda : self.showCustomerSelectTable(), into_frame = customer_frame)
            
            self.program.newLabel(  LabelName = "DV :", Pos = 'W', Row = 0, Col = 3, Bg=self.frame_bgc ,into_frame = customer_frame)
            self.program.newEntry(  Row = 0, Col = 4, Pos = 'W', Long = 2 , Data = self.controller.DV, into_frame = customer_frame)
            
            self.program.newLabel(  LabelName = "Nombre :", Pos = 'W', Row = 1, Col = 0, Bg=self.frame_bgc ,into_frame = customer_frame)
            self.program.newEntry(  Row = 1, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.Nombre, into_frame = customer_frame)
            
            self.program.newLabel(  LabelName = "Contacto :", Pos = 'W', Row = 2, Col = 0,Bg=self.frame_bgc  ,into_frame = customer_frame)
            self.program.newEntry(  Row = 2, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.Contacto, into_frame = customer_frame)
          
            self.program.newLabel(  LabelName = "Termino de pago :", Pos = 'W', Row = 3, Col = 0, Bg=self.frame_bgc  ,into_frame = customer_frame)
            self.program.newEntry(  Row = 3, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.Term, into_frame = customer_frame)
          

            table_frame =  self.program.newFrame(Row = 2 , ColSpan = 2, Pos='NWE', Margin = 5, Bg=self.frame_bgc)

            buttons2_frame =  self.program.newFrame(Row = 1 , Col = 0, Pos="NW", Margin = 5, Bg=self.frame_bgc)

            self.program.newButton( Name='Agregar producto',Row = 0, Col = 0, Pos = 'NW', Command= lambda: self.showProductSelectTable(), into_frame = buttons2_frame)
            self.program.newButton( Name='Eliminar producto',Row = 0, Col = 1, Pos = 'NW', Command= lambda: self.deleteItemFromList(self.items_table), into_frame = buttons2_frame)

            table_frame =  self.program.newFrame(Row = 2 , ColSpan = 2, Pos='NWE', Margin = 5, Bg=self.frame_bgc)
          
            columns = ('Codigo', "Descripcion" , "Cantidad", "Precio unit", "ITBMS","Tasa ITBMS", "Total")
            self.items_table = self.program.newTable(columns, Pos='NWE' ,into_frame = table_frame,data=self.items)

            footer_frame =  self.program.newFrame(Row = 3 , ColSpan = 2, Pos="NWE", Margin = 5, Bg="white")
           
            buttons_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos="NW", Margin = 5, Bg=self.frame_bgc, into_window = footer_frame)

            self.program.newButton( Name='Generar',Row = 0, Col = 0, Pos = 'NW', Command= self.controller.save, into_frame = buttons_frame)
            self.program.newButton( Name='Nota',Row = 0, Col = 1, Pos = 'NE', Command= lambda: self.showNotaModal(), into_frame = buttons_frame)
            self.program.newButton( Name='Descuentos',Row = 0, Col = 2, Pos = 'NE', Command= lambda: self.showDescModal(), into_frame = buttons_frame)
            self.program.newButton( Name='Pagos',Row = 0, Col = 3, Pos = 'NE', Command= lambda: self.showPagosModal(), into_frame = buttons_frame)

            total_frame =  self.program.newFrame(Row = 0 , Col = 2, Pos="NE", Margin = 5, Bg=self.frame_bgc,into_window = footer_frame)

            self.program.newLabel(  LabelName = "Subtotal :", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = total_frame)
            self.program.newLabel(  LabelName = self.controller.subtotal.get(),Pos = 'E', Row = 0, Col = 1, into_frame = total_frame )

            self.program.newLabel(  LabelName = "Pagos :", Row = 1, Col = 0, Bg=self.frame_bgc , into_frame = total_frame)
            self.program.newLabel(  LabelName = self.controller.payment.get(), Pos = 'E',Row = 1, Col = 1, into_frame = total_frame)

            self.program.newLabel(  LabelName = "Descuentos :", Row = 2, Col = 0, Bg=self.frame_bgc , into_frame = total_frame)
            self.program.newLabel(  LabelName = self.controller.discount.get(), Pos = 'E',Row = 2, Col = 1, into_frame = total_frame)

            self.program.newLabel(  LabelName = "Impuestos :", Row = 3, Col = 0, Bg=self.frame_bgc , into_frame = total_frame)
            self.program.newLabel(  LabelName = self.controller.tax.get(), Row = 3, Pos = 'E',Col = 1, into_frame = total_frame)

            self.program.newLabel(  LabelName = "Total :", Row = 4, Col = 0, Pos = 'E',Bg=self.frame_bgc , into_frame = total_frame)
            self.program.newLabel(  LabelName = self.controller.total.get(), Row = 4, Pos = 'E',Col = 1, into_frame = total_frame)

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")

    def updateTotals(self):
        
        total = 0.0
        subtotal = 0.0

        for row in self.items:
            subtotal += (float(row[2]) * float(row[3]))
            total += float(row[6])


        self.controller.subtotal.set(subtotal)
        # self.tax = StringVar()
        self.controller.total.set(total)
        # self.payment = StringVar()
        # self.discount = StringVar()

    def showProductSelectTable(self):

        try:
         
            modal = self.program.modal(title = "Seleccionar producto" , width = 700 , height =400)     
            modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)

            filter_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NW', Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)

            self.program.newLabel(  LabelName = "Filtro", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = filter_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = self.searchProd , into_frame = filter_frame)
           
            table_container =  self.program.newFrame(Row = 1 , Col = 0, Pos='NWE', Margin = 5, Bg=self.frame_bgc, into_window = modal_frame)

           # List table
            self.prod_table_obj = self.program.newTable(("#","Codigo","Descripcion","Precio"), Pos='NWE' ,into_frame = table_container, data = self.productList )

            variable_container =  self.program.newFrame(Row = 2, Col = 0, Pos='NWE', Margin = 5, Bg=self.frame_bgc, into_window = modal_frame)

            self.program.newLabel(  LabelName = "Cantidad", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = variable_container)
            self.program.newEntry(  Row =0, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.cantidad, into_frame = variable_container)

            product_modal_button = self.program.newFrame(Row = 3, Col = 0, Pos='NW', Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)
            self.program.newButton( Name='Agregar a factura',Row = 0, Col = 0, Pos = 'NW', Command=lambda : self.selectedItemFromList(self.prod_table_obj,modal), into_frame = product_modal_button)

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")

    def selectedItemFromList(self,obj,modal):
 
        data = self.program.getTableItem(obj)
        cant = self.controller.cantidad.get()

        input_validate = helper.is_numeric(cant,'Cantidad') 

        if input_validate :
            if  len(data) == 0 :  
                
                messagebox.showerror("Error", "No se ha seleccionado el producto")
            elif int(cant) < 1 : 
                messagebox.showerror("Error", "Debe asignar una cantidad positiva")
            else: 
                total = float(cant) * float(data[3]) 
                
                row = [data[1], data[2], cant ,data[3],0,0,str(total)]

                self.items.append(row)
                self.controller.cantidad.set('')
                self.updateTotals()
                self.index()
                modal.destroy()

    def deleteItemFromList(self,obj):
        
        index = obj.index(obj.selection())
        self.items.remove(self.items[index-1])
        self.updateTotals()
        self.index()
    
    def refreshProductsList(self):
        self.prod_table_obj.delete(*self.prod_table_obj.get_children())
        self.program.insertTableData(self.prod_table_obj,self.productList)
      
    def refreshCustomerList(self):
        self.cust_table_obj.delete(*self.cust_table_obj.get_children())
        self.program.insertTableData(self.cust_table_obj,self.customerList)
      
    def filterList(self,table): 
        
        if table == 'items':
            filterBy = self.searchProd.get()
         
            if filterBy != "": 
                self.productList = helper.filteringList(self.productList,filterBy)
            else: 
                self.productList = self.controller.getProductList()
            self.refreshProductsList()

        elif table == "customers":
            filterBy = self.searchCust.get()
            
            if filterBy != "": 
                self.customerList = helper.filteringList(self.customerList,filterBy)
            else: 
                self.customerList = self.controller.getCustomerList()
            self.refreshCustomerList()
       
    def showCustomerSelectTable(self):

        try:
         
            modal = self.program.modal(title = "Seleccionar Cliente" , width = 500 , height =400)     
            modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)

            filter_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NW', Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)

            self.program.newLabel(  LabelName = "Filtro", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = filter_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = self.searchCust , into_frame = filter_frame)
       
            table_container =  self.program.newFrame(Row = 1 , Col = 0, Pos='NWE', Margin = 5, Bg=self.frame_bgc, into_window = modal_frame)

           # List table
            self.cust_table_obj = self.program.newTable(("#","Nombre","RUC"), Pos='NWE' ,into_frame = table_container, data = self.customerList )

            product_modal_button = self.program.newFrame(Row = 3, Col = 0, Pos='NW', Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)
            self.program.newButton( Name='Seleccionar',Row = 0, Col = 0, Pos = 'NW', Command=lambda : self.selectedCustomerFromList(self.cust_table_obj,modal), into_frame = product_modal_button)

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")

    def selectedCustomerFromList(self,obj,modal):

        data = self.program.getTableItem(obj)
        data = self.controller.getCustomerInfo(data[0])[0]
       
        if len(data) > 0:
            self.controller.Nombre.set(data[1])
            self.controller.RUC.set(data[4])
            self.controller.DV.set(data[5])
            self.controller.Contacto.set(data[12])
            self.controller.Term.set('')
        else: 
            self.controller.Nombre.set('')
            self.controller.RUC.set('')
            self.controller.DV.set('')
            self.controller.Contacto.set('')
            self.controller.Term.set('')
        self.index()
        modal.destroy()

    def dateKeeper(self):
       
        self.cal = self.program.newDatePicker(lambda : self.setDate())
        

    def setDate(self):
        self.controller.Date.set(self.cal[0].selection_get())
        self.cal[1].destroy()

    def showNotaModal(self):
        try:
         
            modal = self.program.modal(title = "Agregar nota" , width = 250 , height =300)     
            modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)

            entry_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NW', Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)

            self.program.newLabel(  LabelName = "Nota:", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = entry_frame)
            self.program.newLongText(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = self.searchProd , into_frame = entry_frame)

            self.program.newButton( Name='Ok',Row = 2, Col = 0, Pos = 'NW', Command=lambda : modal.destroy() , into_frame = modal_frame)

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")

    def showDescModal(self):
        try:
         
            modal = self.program.modal(title = "Descuento" , width = 500 , height =400)     
            modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)


            self.program.newButton( Name='Ok',Row = 2, Col = 0, Pos = 'NW', Command=lambda : modal.destroy() , into_frame = modal_frame)

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")

    def showPagosModal(self):
        try:
         
            modal = self.program.modal(title = "Pagos" , width = 500 , height =400)     
            modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)


            self.program.newButton( Name='Ok',Row = 2, Col = 0, Pos = 'NW', Command=lambda : modal.destroy() , into_frame = modal_frame)

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")