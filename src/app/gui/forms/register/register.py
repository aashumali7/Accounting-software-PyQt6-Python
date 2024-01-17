from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi

class RegisterForm(QDialog):
    # Constructor
    def __init__(self):
        super().__init__()
        loadUi('register.ui', self)

        self.registerButton.clicked.connect(self.on_register_button_click)

    # Method
    def on_register_button_click(self):
        username = self.usernameLineEdit.text()
        password = self.passwordLineEdit.text()
        confirm_password = self.confirmPasswordLineEdit.text()

        print(f"Username: {username}, Password: {password}, Confirm Password: {confirm_password}")

if __name__ == "__main__":
    app = QApplication([])
    register_form = RegisterForm()
    register_form.show()
    app.exec()
