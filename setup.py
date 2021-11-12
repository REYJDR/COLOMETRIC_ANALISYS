import sys

from cx_Freeze import setup, Executable

application_title = "Edocs-Factruados" 
main_python_file = "run.py"


base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {
                    "packages": ["controllers","data","images","models","views"],
                     "include_files" : ['config.json', 'db_script.sql'],
                     "includes": ["tkinter"]
                     }

setup(
        name = application_title,
        version = "1.0",
        description = "Sample cx_Freeze script",
        options = {"build_exe" : build_exe_options},
        executables = [Executable(main_python_file, base = base)])

# import PyInstaller.__main__

# PyInstaller.__main__.run([
#     'run.py',
#     '-n Edocs',
#     '-i "images/logo.icns"'
#     '--windowed',
#     '--onefile',
#     '--collect-datas views'
  
    
# ])
