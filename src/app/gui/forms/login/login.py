import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QWidget
from PyQt6.uic import loadUi

class LoginForm(QDialog):
    #1.Property
    
    #2.Constructor
    def __init__(self):
        super().__init__()
        print('current working directory before change:',os.getcwd())
        print(__file__)
        print(os.path.dirname(__file__))
        print('current working directory after change:',os.path.dirname(__file__))
        #path=os.getcwd()
        #path = path + '/src/app/gui/forms/login/login.ui'
        #loadUi(path,self)

        #self.pushButtonLogin.clicked.connect(self.on_login_button_click)
    #Method
    def on_login_button_click(self):
        username = self.lineEditUsername.text()
        password = self.lineEditUsername.text()

        print(f"Username:{username}, password:{password}")

if __name__ == "__main__":
    app = QApplication([])
    login_form = LoginForm()
    login_form.show()
    app.exec()