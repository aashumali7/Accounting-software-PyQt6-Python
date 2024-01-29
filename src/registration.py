# registration_page.py
from PyQt6.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QGroupBox,QVBoxLayout
from PyQt6.QtCore import Qt, QMargins

class RegistrationPage(QWidget):
    def __init__(self, stack_widget):
        super().__init__()

        self.stack_widget = stack_widget

        layout = QFormLayout()

        # Registration Page Widgets
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addRow(username_label, self.username_input)

        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow(password_label, self.password_input)

        confirm_password_label = QLabel("Confirm Password:")
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow(confirm_password_label, self.confirm_password_input)

        # Increase the vertical spacing between rows
        layout.setVerticalSpacing(80)

        ok_button = QPushButton("Register")
        ok_button.clicked.connect(self.on_ok_clicked)
        ok_button.setStyleSheet("background-color: blue; color: white;")
        layout.addRow(ok_button)

        group_box = QGroupBox("Registration")
        group_box.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_layout.setContentsMargins(QMargins(0, int(self.height() * 0.30), 0, int(self.width() * 0.20)))
        self.setStyleSheet("background-color: white;")  # Set the background color

    def on_ok_clicked(self):
        # Check if passwords match (add more validation if needed)
        if self.password_input.text() == self.confirm_password_input.text():
            self.stack_widget.setCurrentIndex(1)  # Switch to Login Page
        else:
            print("Password and Confirm Password do not match!")
