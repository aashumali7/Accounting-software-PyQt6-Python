import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QStackedWidget, QHBoxLayout, QGroupBox, QDialog,QComboBox
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import Qt

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
        layout.setVerticalSpacing(30)

        ok_button = QPushButton("Register")
        ok_button.clicked.connect(self.on_ok_clicked)
        ok_button.setStyleSheet("background-color: blue; color: white;")
        layout.addRow(ok_button)

        group_box = QGroupBox("Registration")
        group_box.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)  # Center the widget
        self.setStyleSheet("background-color: #D9D9D9;")  # Set the background color

    def on_ok_clicked(self):
        # Check if passwords match (add more validation if needed)
        if self.password_input.text() == self.confirm_password_input.text():
            self.stack_widget.setCurrentIndex(1)  # Switch to Login Page
        else:
            print("Password and Confirm Password do not match!")

class CustomPopup(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("This is a custom popup!")
        layout.addWidget(label)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button)

        self.setLayout(layout)


class LandingPage(QWidget):
    def __init__(self):
        super().__init__()

        # Set the background color to white
        self.setStyleSheet("background-color: white;")

        # Create a horizontal layout for the LandingPage
        main_layout = QHBoxLayout(self)

        # Set layout margins and spacing to 0
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Add a white section (80% width, 100% height)
        white_section = QWidget()
        white_section.setStyleSheet("background-color: white;")

        # Set layout margins and spacing to 0
        white_layout = QVBoxLayout(white_section)
        white_layout.setContentsMargins(0, 0, 0, 0)
        white_layout.setSpacing(5)

        # Add logo centered in the white area
        logo_label = QLabel()
        logo_pixmap = QPixmap("./unnamed.png")  # Replace with the actual path to your logo
        logo_label.setPixmap(logo_pixmap.scaled(200, 200, aspectRatioMode=Qt.AspectRatioMode.KeepAspectRatio))

        white_layout.addWidget(logo_label)

        white_label = QLabel("Welcome to the Landing Page (White Section)")
        white_layout.addWidget(white_label)
        white_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        main_layout.addWidget(white_section, 8)  # Set the white section to take 80% of the available width

        # Add a blue section (20%)
        blue_section = QWidget()
        blue_section.setStyleSheet("background-color: #B7F7EF;")

        # Set layout margins and reduced spacing to 0
        blue_layout = QVBoxLayout(blue_section)
        blue_layout.setContentsMargins(0, 0, 0, 0)
        blue_layout.setSpacing(0)  # Adjusted spacing

        # Move language dropdown to the place of "Additional Information" label
        language_dropdown = QComboBox()
        language_dropdown.addItem("English")
        language_dropdown.addItem("Spanish")
        language_dropdown.addItem("French")
        blue_layout.addWidget(language_dropdown)

        # Create buttons for each menu item
        button_customers = QPushButton("Customers")
        button_suppliers = QPushButton("Suppliers")
        button_items = QPushButton("Items")
        button_sale_register = QPushButton("Sale Register")

        # Set button styles
        button_styles = """
            QPushButton {
                background-color: none;
                color: black;
                border: black;
                font-weight: bold;
                padding: 50px;

            }
        """

        button_hover_style = """
            QPushButton:hover {
                cursor: pointinghand;
            }
        """

        button_customers.setStyleSheet(button_styles + button_hover_style)
        button_suppliers.setStyleSheet(button_styles + button_hover_style)
        button_items.setStyleSheet(button_styles + button_hover_style)
        button_sale_register.setStyleSheet(button_styles + button_hover_style)

        button_customers.setStyleSheet(button_styles)
        button_suppliers.setStyleSheet(button_styles)
        button_items.setStyleSheet(button_styles)
        button_sale_register.setStyleSheet(button_styles)

        button_customers.clicked.connect(self.show_custom_popup)
        button_suppliers.clicked.connect(self.show_custom_popup)
        button_items.clicked.connect(self.show_custom_popup)
        button_sale_register.clicked.connect(self.show_custom_popup)

        # Set cursor for buttons
        button_customers.setCursor(Qt.CursorShape.PointingHandCursor)
        button_suppliers.setCursor(Qt.CursorShape.PointingHandCursor)
        button_items.setCursor(Qt.CursorShape.PointingHandCursor)
        button_sale_register.setCursor(Qt.CursorShape.PointingHandCursor)

        blue_layout.addWidget(button_customers)
        blue_layout.addWidget(button_suppliers)
        blue_layout.addWidget(button_items)
        blue_layout.addWidget(button_sale_register)

        main_layout.addWidget(blue_section, 2)  # Set the blue section to take 20% of the available width

        # Set the layout for the main widget
        self.setLayout(main_layout)

    def show_custom_popup(self):
        popup = CustomPopup()
        popup.exec()

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
        layout.setVerticalSpacing(20)

        login_button = QPushButton("Login")
        login_button.setStyleSheet("background-color: blue; color: white;")
        login_button.clicked.connect(self.on_login_clicked)
        layout.addRow(login_button)

        group_box = QGroupBox("Login")
        group_box.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(group_box, alignment=Qt.AlignmentFlag.AlignCenter)  # Center the widget
        self.setStyleSheet("background-color: #D9D9D9;")  # Set the background color

    def on_login_clicked(self):
        # Add authentication logic here (e.g., check username and password)
        # For simplicity, let's assume login is always successful
        self.stack_widget.setCurrentIndex(2)  # Switch to Landing Page


class MainWindow(QStackedWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Accounting software")  # Set the window title
        self.setWindowIcon(QIcon("./icon2.png"))

        registration_page = RegistrationPage(self)
        login_page = LoginPage(self)
        landing_page = LandingPage()

        self.addWidget(registration_page)
        self.addWidget(login_page)
        self.addWidget(landing_page)

        self.setCurrentWidget(registration_page)
        self.showMaximized()
        self.setStyleSheet("background-color: #A4BFD8;")  # Set the background color

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
