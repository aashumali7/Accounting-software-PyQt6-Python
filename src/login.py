# login_page.py
from PyQt6.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QPushButton, QGroupBox,QVBoxLayout
from PyQt6.QtCore import Qt, QMargins

class LoginPage(QWidget):
    def __init__(self, stack_widget):
        super().__init__()

        self.stack_widget = stack_widget

        layout = QFormLayout()

        # Login Page Widgets
        username_label = QLabel("Username:")
        self.username_input = QLineEdit()
        layout.addRow(username_label, self.username_input)

        password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addRow(password_label, self.password_input)

        # Increase the vertical spacing between rows
        layout.setVerticalSpacing(40)

        login_button = QPushButton("Login")
        login_button.setStyleSheet("background-color: blue; color: white;")
        login_button.clicked.connect(self.on_login_clicked)
        layout.addRow(login_button)

        group_box = QGroupBox("Login")
        group_box.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_layout.setContentsMargins(QMargins(0, int(self.height() * 0.50), 0, int(self.height() * 0.50)))
        self.setStyleSheet("background-color: white;")  # Set the background color

    def on_login_clicked(self):
        # Add authentication logic here (e.g., check username and password)
        # For simplicity, let's assume login is always successful
        self.stack_widget.setCurrentIndex(2)  # Switch to Landing Page
