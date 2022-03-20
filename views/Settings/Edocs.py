from tkinter import IntVar
from tkinter.constants import N, NE, S, TRUE, W
from controllers.edocsController import *
from helpers import helper
import json

class view:


    def __init__(self, program):

        self.program = program
        self.frame_bgc = "#f5f5f5"
        self.controller = edocsController()
        
    def index(self):

        try:
            
            self.program.header("Configuracion de cuenta EDOC's")

            general_info_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos='NW', Margin = 5, Bg=self.frame_bgc)

            self.program.newLabel(  LabelName = "API URL:", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 80 , Data = self.controller.val1 , into_frame = general_info_frame)
        
            self.program.newLabel(  LabelName = "Usuario:", Row = 1, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 1, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.val2 , into_frame = general_info_frame)

            self.program.newLabel(  LabelName = "Contraseña:", Row = 2, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 2, Col = 1, Pos = 'W', Long = 20 , Data = self.controller.val3 , into_frame = general_info_frame , mask = True)

            self.program.newLabel(  LabelName = "Token:", Row = 3, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newEntry(  Row = 3, Col = 1, Pos = 'W', Long = 50 , Data = self.controller.val4 , into_frame = general_info_frame , mask = True)
           

            self.program.newButton( Name = "Conectar", Row = 4 , Col = 0, Pos = 'W', Command= lambda : self.controller.save()  , into_frame = general_info_frame )
 

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")
