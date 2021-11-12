from tkinter.constants import TRUE, W
from controllers.customersController import *
from helpers import helper

class view:

    def __init__(self, program):
        
        self.program = program
        self.cust_controller = customersController()
        self.frame_bgc = "#f5f5f5"
        self.getInitList()
        self.condition = StringVar()
        self.condition.trace("w", lambda name, index, mode : self.filterList() )

    def getInitList(self):
        columns = ( 
            "id",
            "dNombRec" ,
            "dRuc",
            "dDV",
            "dCorElectRec")

        self.list = self.cust_controller.getCustomerList(columns)

    def index(self):

        try:
           
            self.program.header("Clientes")

            filter_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NW', Margin = 5, Bg= self.frame_bgc )

            self.program.newLabel(  LabelName = "Filtro", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = filter_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = self.condition, into_frame = filter_frame)

            # Add new register button        
            add_btn_frame =  self.program.newFrame(Row = 1, Col = 0, Pos="NW", Margin = 5, Bg= self.frame_bgc)
            self.program.newButton( Name='Agregar cliente',Row = 0, Col = 0, Pos = 'NW', Command = lambda : self.viewEditModal('ADD'), into_frame = add_btn_frame)


            # List table
            table_frame =  self.program.newFrame(Row = 2, ColSpan = 2, Pos='NWE', Margin = 5, Bg= self.frame_bgc)
          

            table_obj = self.program.newTable(("#","Nombre","Ruc","Dv","Correo"), Pos='NWE' ,into_frame = table_frame, data = self.list)

            # Select item button
            select_item_frame =  self.program.newFrame(Row = 3, Col = 0, Pos="NW", Margin = 5, Bg= self.frame_bgc)

            self.program.newButton( Name='Ver \ Editar',Row = 0, Col = 0, Pos = 'NW', Command = lambda: self.getSelectedItem(table_obj) , into_frame = select_item_frame)

            self.program.newButton( Name='Eliminar',Row = 0, Col = 1, Pos = 'NW', Command = lambda: self.deleteSelectedItem(table_obj) , into_frame = select_item_frame)


        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")
    
    def newCustomerWindow(self,title): 
        try:
           
            modal = self.program.modal(title = title , width = 473 , height =320)     
          
            modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)
            
            customer_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos='NE', Margin = 5, Bg=self.frame_bgc, into_window = modal_frame)

            self.program.newLabel(  LabelName = "Nombre :", Pos = 'W', Row = 0, Col = 0, Bg=self.frame_bgc ,into_frame = customer_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data =self.cust_controller.dNombRec,  into_frame = customer_frame )
            
            self.program.newLabel(  LabelName = "Tipo de contribuyente:",Bg=self.frame_bgc, Row = 1, Col = 0, into_frame = customer_frame)
            self.program.newOptionMenu( SelectedOption = self.cust_controller.dTipoRuc , Row = 1, Col = 1, Pos = 'W', Long = 5, options=self.cust_controller.tipoContribuyentes(), into_frame = customer_frame)
                
            self.program.newLabel(  LabelName = "Tipo de Receptor:",Bg=self.frame_bgc, Row = 2, Col = 0, into_frame = customer_frame)
            self.program.newOptionMenu( SelectedOption = self.cust_controller.iTipoRec , Row = 2, Col = 1, Pos = 'W', Long = 5, options=self.cust_controller.tipoReceptor(), into_frame = customer_frame)
                

            self.program.newLabel(  LabelName = "RUC :", Pos = 'W', Row = 3, Col = 0, Bg=self.frame_bgc ,into_frame = customer_frame)
            self.program.newEntry(  Row = 3, Col = 1, Pos = 'W', Long = 20 , Data = self.cust_controller.dRuc, into_frame = customer_frame)
            
            self.program.newLabel(  LabelName = "DV :", Pos = 'W', Row = 3, Col = 2, Bg=self.frame_bgc ,into_frame = customer_frame)
            self.program.newEntry(  Row = 3, Col = 3, Pos = 'W', Long = 2 , Data = self.cust_controller.dDV, into_frame = customer_frame)
            

            self.program.newLabel(  LabelName = "Telefono :", Pos = 'W', Row = 4, Col = 0,Bg=self.frame_bgc  ,into_frame = customer_frame)
            self.program.newEntry(  Row = 4, Col = 1, Pos = 'W', Long = 20 , Data = self.cust_controller.dTfnRec, into_frame = customer_frame)
            
            self.program.newLabel(  LabelName = "Correo :", Pos = 'W', Row = 5, Col = 0,Bg=self.frame_bgc  ,into_frame = customer_frame)
            self.program.newEntry(  Row = 5, Col = 1, Pos = 'W', Long = 20 , Data = self.cust_controller.dCorElectRec, into_frame = customer_frame)
            
            self.program.newLabel(  LabelName = "Direccion :", Pos = 'W', Row = 6, Col = 0,Bg=self.frame_bgc  ,into_frame = customer_frame)
            self.program.newEntry(  Row = 6, Col = 1, Pos = 'W', Long = 20 , Data = self.cust_controller.dDirecRec, into_frame = customer_frame)
                
            add_btn_frame =  self.program.newFrame(Row = 1, Col = 0, Pos="NW", Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)

            self.program.newButton( Name='Guardar',Row = 0, Col = 0, Pos = 'NW', Command= lambda : self.saveCust(modal)  , into_frame = add_btn_frame)

  
        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")

    def viewEditModal(self,type):
        if type == 'UPDATE':
            self.newCustomerWindow('Informacion de cliente')
        else: 
            self.cust_controller.clearData()
            self.newCustomerWindow('Agregar cliente')   

    def saveCust(self,modal):
       
        #agraar aqui validacion de campos 
        self.cust_controller.saveCustomer()
        self.cust_controller.clearData()
        self.index()
        modal.destroy()

    def getSelectedItem(self,obj): 
        data = self.program.getTableItem(obj)

        cust_info = self.cust_controller.getCustomerById( data[0] )
        self.cust_controller.setCustInfoValues(cust_info)
        self.viewEditModal('UPDATE')
        
    def deleteSelectedItem(self,obj):
        data = self.program.getTableItem(obj)
        ask = messagebox.askquestion("Eliminar cliente", f"¿Esta seguro de querer eliminar la información del cliente {data[1]}?")

        if ask == 'yes':
            self.cust_controller.deleteCustomer(data[0])
            self.index()
        
    def filterList(self): 
        
        filterBy = self.condition.get()
        if filterBy != "": 
            self.list = helper.filteringList(self.list,filterBy)
        else: 
            self.getInitList()
        self.index()
