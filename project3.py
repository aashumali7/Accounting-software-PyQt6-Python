import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QStackedWidget, QHBoxLayout, QGroupBox
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


class LandingPage(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Landing Page Widgets
        welcome_label = QLabel("Welcome to the Landing Page!")
        layout.addWidget(welcome_label)

        group_box = QGroupBox("Landing Page")
        group_box.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        # Set contents margins to create a 20% gap on all sides
        margin = int(min(self.width(), self.height()) * 0.20)
        main_layout.setContentsMargins(QMargins(margin, margin, margin, margin))

        self.setStyleSheet("background-color: white;")  # Set the background color



class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multi-Page Application")

        stack_widget = QStackedWidget(self)

        registration_page = RegistrationPage(stack_widget)
        login_page = LoginPage(stack_widget)
        landing_page = LandingPage()

        stack_widget.addWidget(registration_page)
        stack_widget.addWidget(login_page)
        stack_widget.addWidget(landing_page)

        # Main Layout
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(stack_widget)
        main_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        main_layout.setContentsMargins(QMargins(int(self.width() * 0.60), 0, int(self.height() * 0.80), 0))
        self.setStyleSheet("background-color: #A4BFD8;")  # Set the initial background color

        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
