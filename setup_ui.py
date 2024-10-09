import subprocess

# Create the ui Python file from QtCreator's .ui
subprocess.call("pyside2-uic ui/mainwindow.ui -o ui/ui_mainwindow.py") 
