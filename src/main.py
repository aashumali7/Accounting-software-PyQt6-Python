from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout,QWidget
from app.gui.forms.login.login import LoginForm
from app.gui.forms.register.register import RegisterForm

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")

        #Create buttons for opening login and register forma
        login_button = QPushButton("Open Login Form") 
        login_button.clicked.connect(self.open_login_form)

        register_button = QPushButton("Open Register Form") 
        register_button.clicked.connect(self.open_register_form)

        #create a layout
        layout = QVBoxLayout()
        layout.addWidget(login_button)
        layout.addWidget(register_button)

        #set the layout to the main window 
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def open_login_form(self):
        login_form = LoginForm()
        login_form.exec()

    def open_register_form(self):
        register_form = RegisterForm()
        register_form.exec()


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.show()
    app.exec()