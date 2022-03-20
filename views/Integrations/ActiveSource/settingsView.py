
from tkinter.constants import N, NE, S, TRUE, W
from controllers.dataSourceController import *


class view:


    def __init__(self, program):

        self.program = program
        self.frame_bgc = "#f5f5f5"
        self.controller = dataSourceController()
      

    def index(self):

        try:
            
            self.program.header("Activacion de fuente de datos")

            general_info_frame =  self.program.newFrame(Row = 0 , Col = 0, Pos='NWE', Margin = 5, Bg=self.frame_bgc)
            self.program.newLabel(  LabelName = 'Fuente', Row = 0, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
            self.program.newLabel(  LabelName = 'Estado', Pos = 'W', Row = 0, Col = 2, Bg=self.frame_bgc , into_frame = general_info_frame)
           
            i = 1
            for item in self.controller.list :
                srcName =  item['val1']
                if item['val2'] == 'X' : 
                    status = True
                else: 
                    status = False 

                self.program.newLabel(  LabelName = srcName, Row = i, Col = 0, Bg=self.frame_bgc , into_frame = general_info_frame)
                self.program.newToggleSwitch(  Row = i, Col = 1, Pos = 'W', Command = lambda  srcName=item['val1'] : self.toggle( srcName, status ), is_on =  status,into_frame = general_info_frame )
                i += 1

        except Exception as e :

            messagebox.showerror(message=str(e) , title="Error")


 
    def toggle(self,source,state):
        print(source)
        if state :
            self.controller.setActiveSource(source,'')
        else: 
            self.controller.setActiveSource(source,'X')
        self.refresh()



    def refresh(self):

       self.program.openView('Integrations.ActiveSource.settingsView.view')
         
