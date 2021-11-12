from tkinter.constants import TRUE, W
from controllers.productsController import *
from helpers import helper

class view:

    def __init__(self, program):
        
        self.program = program
        self.controller = productsController()
        self.frame_bgc = "#f5f5f5"
        self.condition = StringVar()
        self.condition.trace("w", lambda name, index, mode : self.filterList() )

        self.getInitList()


    def getInitList(self):
        self.columns = ( 
                    "id ",
                    "dCodProd" ,
                    "dDescProd" ,
                    "cUnidad",
                    "dPrUnit" 
                   )

        self.list = self.controller.getProductList(self.columns)

    def index(self):

        try:
           
            self.program.header("Productos")
           
            filter_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NW', Margin = 5, Bg= self.frame_bgc )

            self.program.newLabel(  LabelName = "Filtro", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = filter_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = self.condition, into_frame = filter_frame)
            # self.program.newButton( Name='Buscar',Row = 0, Col = 2, Pos = 'NW', Command= lambda : self.filterList(), into_frame = filter_frame)


            add_btn_frame =  self.program.newFrame(Row = 0, Col = 1, Pos="NE", Margin = 5, Bg= self.frame_bgc)

            self.program.newButton( Name='Agregar Producto',Row = 0, Col = 0, Pos = 'NW', Command= lambda : self.viewEditModal('CREATE'), into_frame = add_btn_frame)


            table_frame =  self.program.newFrame(Row = 2, ColSpan = 2, Pos='NWE', Margin = 5, Bg= self.frame_bgc)
          

            table_obj = self.program.newTable(("#",'Produto ID', "Descripcion" ,  "Unidad" , "Precio unit" ) , Pos='NWE' ,into_frame = table_frame, data = self.list)

            
            # Select item button
            select_item_frame =  self.program.newFrame(Row = 3, Col = 0, Pos="NW", Margin = 5, Bg= self.frame_bgc)

            self.program.newButton( Name='Ver \ Editar',Row = 0, Col = 0, Pos = 'NW', Command = lambda: self.getSelectedItem(table_obj) , into_frame = select_item_frame)

            self.program.newButton( Name='Eliminar',Row = 0, Col = 1, Pos = 'NW', Command = lambda: self.deleteSelectedItem(table_obj) , into_frame = select_item_frame)


        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")
    
    def filterList(self): 
        
        filterBy = self.condition.get()
        if filterBy != "": 
            self.list = helper.filteringList(self.list,filterBy)
        else: 
            self.getInitList()
        self.index()


    def newProductWindow(self,title):

        modal = self.program.modal(title = title , width = 473 , height =320)     

        modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)
        
        

        product_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos='NE', Margin = 5, Bg=self.frame_bgc, into_window = modal_frame)
        
        self.program.newLabel(  LabelName = "Codigo :", Pos = 'W', Row = 0, Col = 0, Bg=self.frame_bgc ,into_frame = product_frame)
        self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data =self.controller.dCodProd ,  into_frame = product_frame)
        
        self.program.newLabel(  LabelName = "Descripcion :", Pos = 'W', Row = 1, Col = 0, Bg=self.frame_bgc ,into_frame = product_frame)
        self.program.newEntry(  Row = 1, Col = 1, Pos = 'W', Long = 20 , Data =self.controller.dDescProd ,  into_frame = product_frame)


        self.program.newLabel(  LabelName = "Fecha caducidad :", Pos = 'W', Row = 2, Col = 0, Bg=self.frame_bgc ,into_frame = product_frame)
        self.program.newEntry(  Row = 2, Col = 1, Pos = 'W', Long = 20 , Data =self.controller.dFechaCad ,  into_frame = product_frame)

        self.program.newLabel(  LabelName = "Fecha Fabricación :", Pos = 'W', Row = 3, Col = 0, Bg=self.frame_bgc ,into_frame = product_frame)
        self.program.newEntry(  Row = 3, Col = 1, Pos = 'W', Long = 20 , Data =self.controller.dFechaFab ,  into_frame = product_frame)

        self.program.newLabel(  LabelName = "Precio unitario :", Pos = 'W', Row = 4, Col = 0, Bg=self.frame_bgc ,into_frame = product_frame)
        self.program.newEntry(  Row = 4, Col = 1, Pos = 'W', Long = 20 , Data =self.controller.dPrUnit ,  into_frame = product_frame)

        self.program.newLabel(  LabelName = "Unidad :", Pos = 'W', Row = 5, Col = 0, Bg=self.frame_bgc ,into_frame = product_frame)
        self.program.newEntry(  Row = 5, Col = 1, Pos = 'W', Long = 20 , Data =self.controller.cUnidad ,  into_frame = product_frame)

        add_btn_frame =  self.program.newFrame(Row = 1, Col = 0, Pos="NW", Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)

        self.program.newButton( Name='Guardar',Row = 0, Col = 0, Pos = 'NW', Command= lambda : self.save(modal)  , into_frame = add_btn_frame)

    def viewEditModal(self,type):
        if type == 'UPDATE':
            self.newProductWindow('Informacion de producto')
        else: 
            self.controller.clearData()
            self.newProductWindow('Agregar producto')   

    def save(self,modal):
       
        #agraar aqui validacion de campos 
        self.controller.save()
        self.controller.clearData()
        self.getInitList()
        self.index()
        modal.destroy()

    def getSelectedItem(self,obj): 
        
        data = self.program.getTableItem(obj)

        info = self.controller.getProductById( data[0] )
        self.controller.setProductInfoValues(info)
        self.viewEditModal('UPDATE')
        
    def deleteSelectedItem(self,obj):
        

        data = self.program.getTableItem(obj)
        ask = messagebox.askquestion("Eliminar producto", f"¿Esta seguro de querer eliminar la información del productio {data[1]}?")

        if ask == 'yes':
            self.controller.delete(data[0])
            self.index()