from tkinter import IntVar
from tkinter.constants import N, NE, S, TRUE, W
from controllers.sitelinkController import *
from helpers import helper
import json

class view:


    def __init__(self, program):

        self.program = program
        self.frame_bgc = "#f5f5f5"
        self.controller = sitelinkController()
        
    def index(self):

        try:
            
            self.program.header("Configuracion de base de datos - Quickbooks")

            general_info_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos='NW', Margin = 5, Bg=self.frame_bgc)

            self.program.newLabel(  LabelName = "Instancia SQL server:", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 80 , Data = self.controller.val1 , into_frame = general_info_frame)
        
            self.program.newLabel(  LabelName = "Usuario:", Row = 1, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 1, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.val2 , into_frame = general_info_frame)

            self.program.newLabel(  LabelName = "Contraseña:", Row = 2, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 2, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.val3 , into_frame = general_info_frame , mask = True)

            self.program.newLabel(  LabelName = "Sucursales (separado por comas):", Row = 3, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 3, Col = 1, Pos = 'W', Long = 50 , Data = self.controller.val4 , into_frame = general_info_frame )

            self.program.newButton( Name = "Conectar", Row = 5, Col = 0, Pos = 'W', Command= lambda : self.controller.save() , into_frame = general_info_frame )
 

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")


 
    # def toggle(self):

    #     if not self.controller.default.get() :
    #         self.switch1.config( image = self.program.swImgOn() )
    #         self.controller.default.set(True)

    #     else:
    #         self.switch1.config( image = self.program.swImgOff() )
    #         self.controller.default.set(False)


        
    def resultWindow(self, input ) :

        result = self.controller.doQuery( input )

        if result and len(result) >0 :

            modal = self.program.modal(title = 'Resultado' , width = 1200 , height =520)     

            modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)
            
            table_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc)

            line = result[0]
            i=1
            columns = []
            for col in line:
                columns.append(f"col{i}")
                i+=1
            columns = tuple(columns)
            
            table_obj = self.program.newTable( columns , Pos='NWE' ,into_frame = modal_frame, data = result )

            add_btn_frame =  self.program.newFrame(Row = 1, Col = 0, Pos="NW", Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)

            self.program.newButton( Name='Cerrar',Row = 0, Col = 0, Pos = 'NW', Command= lambda : self.closeWindow(modal)  , into_frame = add_btn_frame)

        else: 
            
            messagebox.showerror(message="Data not found" , title="Error")


    def closeWindow(self,modal):
       
        #agraar aqui validacion de campos 
        modal.destroy()