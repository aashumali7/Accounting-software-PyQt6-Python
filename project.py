#import area
import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QIcon
import winreg

#class definaion
#class ChildClass(ParentClass)
class AccountingApp(QWidget):
    #property
    settings={}
    #constructor
    def __init__(self): #self is cio Class internal object
        super().__init__() # ican call the parent constructor 
        print('hello from constructor')
         #lets try to read a json file
        self.readJsonFile()
        self.checkAdminIsCreated()
        self.buildUI()
    #method
    def checkAdminIsCreated(self):
        print("hello from checkAdminIsCreated ")

    key_path = r"SOFTWARE\accounting_software"
    value_name = "isAdminCreated"

    try:
            # Open the registry key for reading
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
        #read the value
        value, _ = winreg.QueryValueEx(key, value_name)
       
        if value.lower() == "true":
            #show login form
            print("show the login form")
            pass
        elif value.lower() == "false":
            #show the registration form
            print("show the registration form")
        else:
            print("create a entry isAdminCreated= false")    

        # Close the registry key
    except FileNotFoundError:
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, "false")
        
    winreg.CloseKey(key)
    pass    
    def readJsonFile(self): 
        try:
            with open('accounting.json', 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            self.settings = {}
        print(self.settings)  
        print(type(self.settings))
        pass      

    def buildUI(self):
        self.setStyleSheet('background-color: #A4BFD8;') #actualargument
        self.setWindowTitle(self.settings["windowTitle"])
        self.showMaximized()
        self.show()
        icon_path = self.settings.get("iconPath", "")
        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
            self.setWindowIcon(icon)
        pass

#create ClassObject
app = QApplication([])
ceo = AccountingApp() #ceo is class external object
ceo.showMaximized()
sys.exit(app.exec())
