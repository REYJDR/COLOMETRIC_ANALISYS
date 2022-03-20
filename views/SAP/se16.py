from tkinter.constants import TRUE, W
from controllers.productsController import *
from helpers import helper
from sap.sapsdk_con import sap_connect as sap

class view:

    def __init__(self, program):
        
        self.program = program
        self.controller = productsController()
        self.frame_bgc = "#f5f5f5"

        self.sap_table = StringVar()
        self.sap_table_row = StringVar()

        self.table_info = []

        self.columns = []
       
    def openFilterModal(self, fields):

        try:
           
            modal = self.program.modal(title = "Filtro" , width = 473 , height = 50 * int(len(fields)) )     
          
            modal_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NWE', Margin = 5, Bg= self.frame_bgc, into_window = modal)
            
            customer_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos='NE', Margin = 5, Bg=self.frame_bgc, into_window = modal_frame)

            count = 0
            val = []
            for row in fields:
                
                val.append(StringVar())
               

                self.program.newLabel(  LabelName = f"{row['col']} :", Pos = 'W', Row = count, Col = 0, Bg=self.frame_bgc ,into_frame = customer_frame)
                self.program.newEntry(  Row = count, Col = 1, Pos = 'W', Long = int(row['long']) , Data = val[count],  into_frame = customer_frame )
                count += 1
                
            add_btn_frame =  self.program.newFrame(Row = 1, Col = 0, Pos="NW", Margin = 5, Bg= self.frame_bgc, into_window = modal_frame)

            self.program.newButton( Name='Guardar',Row = 0, Col = 0, Pos = 'NW', Command= lambda : self.get_info(fields,val,modal)  , into_frame = add_btn_frame)

  
        except Exception as e :
            messagebox.showerror(message=str(e) , title="Error")

    def get_info(self,fields,values,modal):
        self.table_info = []
        count = 0
        where = []
        for val in values: 
            if val.get() != '':
                where.append(f"{fields[count]['col']} = '{val.get()}'")
            count += 1

        options = [{'TEXT' : x } for x in where]

        sap_con = sap()
     
        info = sap_con.get_table_info(self.sap_table.get(), options, 20)
        
        self.columns = [ x['FIELDTEXT'] for x in info['FIELDS']]
       
        for x in info['DATA']:
            
            fields = x['WA'].strip().split('|')
            self.table_info.append(tuple(fields)) 

        self.index()
        modal.destroy()
        
    def get_filter(self):

        sap_con = sap()
        # info =  sap_con.get_table_info(  self.sap_table.get() , 20)

        filter = sap_con.get_table_filter( self.sap_table.get())
        if len(filter) > 0:
            self.openFilterModal(filter)

        # self.index()

    def index(self):

        try:
           
            self.program.header("SAP TABLE")
           
            filter_frame =  self.program.newFrame(Row = 0, Col = 0, Pos='NW', Margin = 5, Bg= self.frame_bgc )

            self.program.newLabel(  LabelName = "Tabla", Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = filter_frame)
            self.program.newEntry(  Row = 0, Col = 1, Pos = 'W', Long = 20 , Data = self.sap_table, into_frame = filter_frame)
            self.program.newButton( Name='Buscar',Row = 0, Col = 2, Pos = 'NW', Command= lambda : self.get_filter(), into_frame = filter_frame)


            table_frame =  self.program.newFrame(Row = 2, ColSpan = 2, Pos='NWE', Margin = 5, Bg= self.frame_bgc)

            if len(self.columns) == 0: 
                columns = ('#')
            else:
                columns = self.columns

            self.program.newTable( columns , Pos='NWE' ,into_frame = table_frame, data = self.table_info)

            

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")