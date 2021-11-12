import sys
import os 
from tkinter import messagebox  
from difflib import SequenceMatcher
from tkinter.constants import TRUE

class helper: 

    def find_data_file(filename):
        if getattr(sys, "frozen", False):
            # The application is frozen
            datadir = os.path.dirname(sys.executable)
        else:
            # The application is not frozen
            # Change this bit to match where you store your data files:
            datadir = os.path.dirname(__file__)
        return os.path.join(datadir, filename)
    
    def is_numeric(input,field_name):
        try: 
            int(input)
            return True
        except ValueError: 
            messagebox.showerror("Error", f"El valor de {field_name} debe ser numerico")
            return False

    def validate_is_textonly(input):
        return
    
    def filteringList(list_to_filter,search):

        count = 0
        new_list = []

        for row in list_to_filter:
            for val in row:
                if helper.similarCorrelation(str(val), str(search)) :
                   count +=1
            if count > 0:
                new_list.append(row)
                count = 0
        
        return list(new_list)
   
    def similarCorrelation(s1 , s2):
        try:
            count = 0
            if (len(s1) > 0 and len(s2)) and len(s2) <= len(s1):
                   
                    for i in range(0, len(s2)):
                        if s1[i] == s2[i]:
                           
                            count += 1
                        else: 
                            count=0
                    
                    if count != 0 : return True 

            return False
        except Exception as e:
            
            return False