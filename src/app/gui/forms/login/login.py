from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QWidget
from PyQt6.uic import loadUi

class LoginFrom(QDialog):
    #1.Property
    
    #2.Constructor
    def __init__(self):
        super().__init__()
        loadUi('login_form.ui',self)

        self.pushButtonLogin.clicked.connect(self.on_login_button_click)
    #Method
    def on_login_button_click(self):
        username = self.lineEditUsername.text()
        password = self.lineEditUsername.text()

        print(f"Username:{username}, password:{password}")

if __name__ == "__main__":
    app = QApplication([])
    login_form = LoginFrom()
    login_form.show()
    app.exec()

