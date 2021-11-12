from tkinter.constants import TRUE, W
from controllers.invoicesController import *

class view:

    def __init__(self, program):
        self.program = program
        self.controller = invoicesController()


    def index(self):

        try:
            self.program.header("Lista de facturas")

            frame_bgc = "#f5f5f5"

            table_frame =  self.program.newFrame(Row = 0 , ColSpan = 2, Pos='NWE', Margin = 5, Bg=frame_bgc)
          
            columns = ('Produto ID', "Descripcion" , "Cantidad", "Precio unit", "ITBMS","Tasa ITBMS", "Total")
            self.program.newTable(columns, Pos='NWE' ,into_frame = table_frame)



        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")
    