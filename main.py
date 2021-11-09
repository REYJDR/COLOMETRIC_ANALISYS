from tkinter import *
from platform import system
import os.path
import pathlib
from tkinter import messagebox
from  tkinter import ttk
import json
from io import open

class App:

    #main screen
    def __init__(self):
        
        self.config_file = self.getConfig()
        
        self.screen = Tk()
        self.view = Frame(self.screen)
        self.title = " Facturador Edocs"

        platformD = system()

        if platformD == 'Darwin':

            self.icon  = os.path.abspath('./images/logo.icns')

        else:
            self.icon  = os.path.abspath('./images/logo.ico')

        self.bodyBgColor = 'lightgray'
        self.resizable = TRUE
        self.minsizeHeight = 550
        self.minsizeWidht  = 1024

        self.padx = 5
        self.pady = 5
        self.geometry = f"{str(self.minsizeWidht)}x{str(self.minsizeHeight)}"
        self.font = "Open Sans"
        self.screen.grid_columnconfigure(0, weight=1)
        self.screen.grid_rowconfigure(0, weight=1)

    #menu
    def SetMenu(self):

        main_menu = Menu(self.screen)

        #Sub menu Archivo
        sub_menu_1 = Menu(main_menu,tearoff=0)

        routes = self.config_file['routes']

        for menu in routes:
            if menu['menu_name'] == 'main':
                if len(menu['submenu']) > 0 :
                    for menu_sub_item in menu['submenu']:
                        for group in menu_sub_item['group']:
                            sub_menu_1.add_command(label=group['name'], command= lambda class_item=group['class'] : self.openView(class_item))
                         
                        sub_menu_1.add_separator()    

                sub_menu_1.add_command(label='Salir', command = lambda : self.quitProgram())
                main_menu.add_cascade(label="Archivo",menu=sub_menu_1)

            else: 
                #new_menu =  Menu(self.screen) 
                new_sub_menu = Menu(main_menu,tearoff=0)

                if len(menu['submenu']) > 0 :
                    for menu_sub_item in menu['submenu']:
                        for group in menu_sub_item['group']:
                            new_sub_menu.add_command(label=group['name'], command= lambda class_item=group['class'] : self.openView(class_item))
                         
                        new_sub_menu.add_separator()    
                         
                main_menu.add_cascade(label=menu['menu_name'],menu=new_sub_menu)
                
                
        return main_menu

    def getConfig(self):

        ruta = f"{str(pathlib.Path().absolute())}/config.json"
        config = open(ruta,"r")
        
        data = json.load(config)
        return data

    # def mainScreenUpdate(self):
    #     self.screen.update()

    def load(self):
       
        self.screen.title(self.title)

        self.screen.config( menu=self.SetMenu() , bg=self.bodyBgColor, padx= self.padx, pady=self.padx)
        self.screen.iconbitmap(self.icon)
        self.screen.geometry(self.geometry)
        self.screen.minsize(self.minsizeWidht,self.minsizeHeight)

        if self.resizable :
            self.screen.resizable(1,1)
        else: 
            self.screen.resizable(0,0)

    def run(self):
        # RUN PROGRAM 
        self.screen.mainloop()

    #Custom object on subscreen
    def header(self,texto):
        self.screen.title(texto)
        # header = Label(self.view, text=texto)

        # header.config( 
        #     fg="white",
        #     bg="darkgray",
        #     font=(self.font, 18),
        #     pady=10 )

        # header.grid(row=0,column=0,columnspan=2)

    def newEntry(self,  Row = 0 , Col = 0, Pos = 'W', Long = 100, Show = 'normal', Orientacion = 'left', Input = "", Data = "", into_frame = None):
        
        if into_frame != None:
            insert_on =  into_frame
        else:
            insert_on =  self.view

        input = Entry(insert_on)

        input.config( width= Long,
                      state = Show,
                      justify= Orientacion,
                      textvariable= Data,
                      border=0
                      )

        if Input != "" :
            input.insert(-1, Input)

        input.grid(row = Row, column = Col , sticky=Pos , padx=5, pady=5)   

    def newLabel(self , LabelName = 'Label', Row = 0 , Col = 0, ColSpan = 0, Pos = 'W' , into_frame = None , Bg = 'white'):
        
        if into_frame != None:
            insert_on =  into_frame
        else:
            insert_on =  self.view

        label = Label(insert_on, text = LabelName)
        label.config( background= Bg)
        label.grid(row = Row,padx=5,pady=5 , sticky = Pos)

        if ColSpan != 0 :
             label.grid( columnspan=ColSpan  )
        else: 
             label.grid( column=Col  )

    def newButton(self,Name = "Button", Row = 0 , Col = 0, Pos = 'W', Command = 'null' , into_frame = None ):

        if into_frame != None:
            insert_on =  into_frame
        else:
            insert_on =  self.view

        button = Button(insert_on, text = Name, highlightbackground='lightgray')
        button.config( 
            pady=2, 
            padx=2,
            command=Command 
        )
        button.grid(row = Row,column = Col ,padx=5, pady=5 ,sticky = Pos )

    def newOptionMenu(self,  Row = 0 , Col = 0, Pos = 'W',  Long = 100, SelectedOption = '',options = "", into_frame = None):

        if into_frame != None:
            insert_on =  into_frame
        else:
            insert_on =  self.view

        selectOption = OptionMenu(insert_on ,SelectedOption,*options)
        selectOption.config( width= Long , border=0)
        selectOption.grid(row = Row,column= Col ,padx=5, pady=5 ,sticky = Pos )

    def newTable(self, columns, Row = 0 , Col = 0,  ColSpan = 0, Pos = 'W', into_frame = None, data = None):

        if into_frame != None:
            insert_on =  into_frame
        else:
            insert_on =  self.view
        style = ttk.Style()
        
        style.configure("Treeview",
            background="#F5F5F5",
            foreground="black",
            rowheight = 20,
            fieldbackground =  "#F5F5F5",
        )

        style.map('Treeview',
            
            background=[('selected','lightgreen')],
        
        )

        table = ttk.Treeview(insert_on, columns = columns)
        table['show'] = 'headings'
        table.grid(row = Row, padx=5, pady=5 ,sticky = Pos )
        
        table.tag_configure( 'oddrow',  background="#F5F5F5" )
        table.tag_configure( 'evenrow',  background="lightblue" )


        if ColSpan != 0 :
             table.grid( columnspan=ColSpan  )
        else: 
             table.grid( column=Col  )

        i = 1
        for hdr in columns:
            if hdr == '#' : 
              table.column(f'#{i}', anchor=CENTER, stretch = NO, width = 50 )
            table.heading(f'#{i}',text=hdr) 
           
            i+=1
        
        count = 0
        if data != None : 
           for row in data: 
                if count % 2 == 0:
                    table.insert('',0,values=row, tags=('evenrow'))
                else: 
                    table.insert('',0,values=row, tags=('oddrow'))
                count += 1
        return table
   
    def getTableItem(self, table):
        try:
           values = table.item(table.focus())['values']
        #table.
           return values
        except Exception as e:  
            messagebox.showerror('Error',str(e))  

    def newFrame(self , Bg = 'white', Row = 0 , Col = 0, ColSpan = 0,  Pos = 'W', bw = 1 , rel = 'groove', Margin = 0, into_window = None):

        if into_window != None:
            frame_into = into_window
        else:
            frame_into = self.view
            
        this_frame = Frame(frame_into)
        this_frame.config( bg=Bg , relief=rel, borderwidth=bw, width=100)
        this_frame.grid(row=Row, sticky=Pos, pady=Margin, padx=Margin  )
        this_frame.grid_rowconfigure(0, minsize=5, weight=1)
        this_frame.grid_columnconfigure(0, minsize=5, weight=1)

        if ColSpan != 0 :
             this_frame.grid( columnspan=ColSpan  )
        else: 
             this_frame.grid( column=Col  )

        return this_frame

    def ViewFrame(self):
        
            if hasattr(self, 'view'):
                for widgets in self.view.winfo_children():
                    widgets.destroy()
                    self.view.destroy

            self.view.config( bg="white" , relief='groove', borderwidth=2 , padx=5, pady=5)

            self.view.grid(row=0,column=0,sticky='NSWE')
            self.view.grid_columnconfigure([0,1,2,3,4], weight=1)
            self.view.grid_rowconfigure([0,1,2,3,4], weight=0)
           
    def modal(self, width = 150, height = 150, title = "modal"):

        # modal = Tk()
        modal = Toplevel()
        modal.config( bg=self.bodyBgColor, padx= self.padx, pady=self.padx)
        modal.geometry(f"{str(width)}x{str(height)}")
        modal.minsize(width,height)
        modal.title(title)
        modal.resizable(0,0)

        modal.focus_force()     # Get focus
        modal.lift() # Raise in stacking order
        modal.grab_set_global()
        self.screen.update()
        return modal

    def openView(self,name):
      
        try:
           
            self.ViewFrame()

            components = name.split('.')
            route = f"views.{components[0]}.{components[1]}"
            mod = __import__(route, fromlist=[components[2]])
            viewClass = getattr(mod, components[2])

            view = viewClass(self)
            view.index()

            #messagebox.showinfo('test',mod)
        except Exception as e:
            messagebox.showerror('Error',str(e))  

    def quitProgram(self):

        ask = messagebox.askquestion("Salir de Edocs", "¿Esta seguro de querer salir el programa?")
   
        if ask == 'yes':
            self.screen.quit()