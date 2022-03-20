from tkinter import IntVar
from tkinter.constants import N, NE, S, TRUE, W
from controllers.invoicesController import *
from helpers import helper
import json

class view:


    def __init__(self, program):

        self.program = program
        self.data = json.load(helper.OpenFile('config.json'))
        self.frame_bgc = "#f5f5f5"
      
        
    def index(self):

        try:
            
            self.program.header("Configuracion de base de datos")

            general_info_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos='NW', Margin = 5, Bg=self.frame_bgc)

            self.program.newLabel(  LabelName = "Host:", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = '', into_frame = general_info_frame)
           
            self.program.newLabel(  LabelName = "Nombre BD:", Row = 1, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 1, Col = 1, Pos = 'W', Long = 20 , Data = '', into_frame = general_info_frame)
           
            self.program.newLabel(  LabelName = "Usurio:", Row = 2, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 2, Col = 1, Pos = 'W', Long = 20 , Data = '', into_frame = general_info_frame)

            self.program.newLabel(  LabelName = "Contraseña:", Row = 3, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 3, Col = 1, Pos = 'W', Long = 20 , Data = '', into_frame = general_info_frame)

            self.program.newButton( Name = "Conectar", Row = 4 , Col = 0, Pos = 'W', Command = 'null' , into_frame = general_info_frame )
            # self.program.newLabel(  LabelName = "Fecha :", Row = 1, Col = 0, Bg=self.frame_bgc ,into_frame = general_info_frame)
            # self.program.newEntry(  Row = 1, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.Date, into_frame = general_info_frame)
            # self.program.newButton( Name='...',Row = 1, Col = 3, Pos = 'W', Command= lambda : self.dateKeeper(), into_frame = general_info_frame)
            
            # self.program.newLabel(  LabelName = "Itbms:",Bg=self.frame_bgc, Row = 2, Col = 0, into_frame = general_info_frame)
            # self.program.newOptionMenu( SelectedOption = self.controller.Tax, Row = 2, Col = 1, Pos = 'W', Long = 5, options=self.controller.getTaxList(), into_frame = general_info_frame)
            
            # customer_frame =  self.program.newFrame(Row = 0 , Col = 1, Pos='NE', Margin = 5, Bg=self.frame_bgc)
            
            # self.program.newLabel(  LabelName = "RUC :", Pos = 'W', Row = 0, Col = 0, Bg=self.frame_bgc ,into_frame = customer_frame)
            # self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.RUC, into_frame = customer_frame)
            # self.program.newButton( Name='...',Row = 0, Col = 2, Pos = 'W', Command= lambda : self.showCustomerSelectTable(), into_frame = customer_frame)
            
            # self.program.newLabel(  LabelName = "DV :", Pos = 'W', Row = 0, Col = 3, Bg=self.frame_bgc ,into_frame = customer_frame)
            # self.program.newEntry(  Row = 0, Col = 4, Pos = 'W', Long = 2 , Data = self.controller.DV, into_frame = customer_frame)
            
            # self.program.newLabel(  LabelName = "Nombre :", Pos = 'W', Row = 1, Col = 0, Bg=self.frame_bgc ,into_frame = customer_frame)
            # self.program.newEntry(  Row = 1, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.Nombre, into_frame = customer_frame)
            
            # self.program.newLabel(  LabelName = "Contacto :", Pos = 'W', Row = 2, Col = 0,Bg=self.frame_bgc  ,into_frame = customer_frame)
            # self.program.newEntry(  Row = 2, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.Contacto, into_frame = customer_frame)
          
            # self.program.newLabel(  LabelName = "Termino de pago :", Pos = 'W', Row = 3, Col = 0, Bg=self.frame_bgc  ,into_frame = customer_frame)
            # self.program.newEntry(  Row = 3, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.Term, into_frame = customer_frame)
          

            # table_frame =  self.program.newFrame(Row = 2 , ColSpan = 2, Pos='NWE', Margin = 5, Bg=self.frame_bgc)

            # buttons2_frame =  self.program.newFrame(Row = 1 , Col = 0, Pos="NW", Margin = 5, Bg=self.frame_bgc)

            # self.program.newButton( Name='Agregar producto',Row = 0, Col = 0, Pos = 'NW', Command= lambda: self.showProductSelectTable(), into_frame = buttons2_frame)
            # self.program.newButton( Name='Eliminar producto',Row = 0, Col = 1, Pos = 'NW', Command= lambda: self.deleteItemFromList(self.items_table), into_frame = buttons2_frame)

            # table_frame =  self.program.newFrame(Row = 2 , ColSpan = 2, Pos='NWE', Margin = 5, Bg=self.frame_bgc)
          
            # columns = ('Codigo', "Descripcion" , "Cantidad", "Precio unit", "ITBMS","Tasa ITBMS", "Total")
            # self.items_table = self.program.newTable(columns, Pos='NWE' ,into_frame = table_frame,data=self.items)

            # footer_frame =  self.program.newFrame(Row = 3 , ColSpan = 2, Pos="NWE", Margin = 5, Bg="white")
           
            # buttons_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos="NW", Margin = 5, Bg=self.frame_bgc, into_window = footer_frame)

            # self.program.newButton( Name='Generar',Row = 0, Col = 0, Pos = 'NW', Command= self.controller.save, into_frame = buttons_frame)
            # self.program.newButton( Name='Nota',Row = 0, Col = 1, Pos = 'NE', Command= lambda: self.showNotaModal(), into_frame = buttons_frame)
            # self.program.newButton( Name='Descuentos',Row = 0, Col = 2, Pos = 'NE', Command= lambda: self.showDescModal(), into_frame = buttons_frame)
            # self.program.newButton( Name='Pagos',Row = 0, Col = 3, Pos = 'NE', Command= lambda: self.showPagosModal(), into_frame = buttons_frame)

            # total_frame =  self.program.newFrame(Row = 0 , Col = 2, Pos="NE", Margin = 5, Bg=self.frame_bgc,into_window = footer_frame)

            # self.program.newLabel(  LabelName = "Subtotal :", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = total_frame)
            # self.program.newLabel(  LabelName = self.controller.subtotal.get(),Pos = 'E', Row = 0, Col = 1, into_frame = total_frame )

            # self.program.newLabel(  LabelName = "Pagos :", Row = 1, Col = 0, Bg=self.frame_bgc , into_frame = total_frame)
            # self.program.newLabel(  LabelName = self.controller.payment.get(), Pos = 'E',Row = 1, Col = 1, into_frame = total_frame)

            # self.program.newLabel(  LabelName = "Descuentos :", Row = 2, Col = 0, Bg=self.frame_bgc , into_frame = total_frame)
            # self.program.newLabel(  LabelName = self.controller.discount.get(), Pos = 'E',Row = 2, Col = 1, into_frame = total_frame)

            # self.program.newLabel(  LabelName = "Impuestos :", Row = 3, Col = 0, Bg=self.frame_bgc , into_frame = total_frame)
            # self.program.newLabel(  LabelName = self.controller.tax.get(), Row = 3, Pos = 'E',Col = 1, into_frame = total_frame)

            # self.program.newLabel(  LabelName = "Total :", Row = 4, Col = 0, Pos = 'E',Bg=self.frame_bgc , into_frame = total_frame)
            # self.program.newLabel(  LabelName = self.controller.total.get(), Row = 4, Pos = 'E',Col = 1, into_frame = total_frame)

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")
