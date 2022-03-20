from tkinter.constants import TRUE, W
from controllers.invoicesController import *

class view:

    def __init__(self, program):
        self.program = program
        self.controller = invoicesController()

    def dateKeeper(self, type):
            self.cal = self.program.newDatePicker(lambda : self.setDate(type))
      

    def setDate(self,type):
        if type == 'from':
            self.controller.dateFrom.set(self.cal[0].selection_get())
        if type == 'to':
            self.controller.dateTo.set(self.cal[0].selection_get())

        self.cal[1].destroy()        


    def index(self):

        try:
            self.program.header("Lista de facturas")

            frame_bgc = "#f5f5f5"

            filter_frame =  self.program.newFrame(Row = 0 , Col  = 0, Pos='W', Margin = 5, Bg=frame_bgc)
            self.program.newLabel(  LabelName = "Desde", Row = 0, Col = 0, Bg= frame_bgc , into_frame = filter_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data =  self.controller.dateFrom, into_frame = filter_frame)
            self.program.newButton( Name='...',Row = 0, Col = 2, Pos = 'W', Command= lambda : self.dateKeeper('from'), into_frame = filter_frame)

            self.program.newLabel(  LabelName = "Hasta", Row = 0, Col = 3, Bg= frame_bgc , into_frame = filter_frame)
            self.program.newEntry(  Row = 0, Col = 4, Pos = 'W', Long = 20 , Data =  self.controller.dateTo, into_frame = filter_frame)
            self.program.newButton( Name='...',Row = 0, Col = 5, Pos = 'W', Command= lambda : self.dateKeeper('to'), into_frame = filter_frame)

            self.program.newButton( Name='Filtrar',Row = 0, Col = 6, Pos = 'E', Command= lambda :  '', into_frame = filter_frame)

            table_frame =  self.program.newFrame(Row = 2 , ColSpan = 2, Pos='WE', Margin = 5, Bg=frame_bgc)
          
            self.program.newButton( Name='Refrescar',Row = 0, Col = 0, Pos = 'E', Command= lambda : self.controller.extractInvoices(), into_frame = table_frame)

            columns = ('ID Cliente', "Nombre cliente" , "Documento ", "Fecha", "Total", "Pago", "Forma de pago", "Estatus FE")

            self.program.newTable(columns, Pos='WE' ,Row = 1, Col = 0, data = self.controller.invoiceList ,into_frame = table_frame, hasChkBox = True)


        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")
    