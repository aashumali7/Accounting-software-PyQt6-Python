import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QStackedWidget, QHBoxLayout, QGroupBox, QComboBox, QMainWindow, QMenuBar, QMenu, QDialog
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap ,QAction


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

        # Set the size to 50% of the main window's width and height
        main_window_size = self.stack_widget.parent().size()
        registration_size = QSize(int(main_window_size.width() * 0.7), int(main_window_size.height() * 0.7))
        self.resize(registration_size)

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

        # Add a white section (100% width, 100% height)
        white_section = QWidget()
        white_section.setStyleSheet("background-color: white;")

        # Set layout margins and spacing to 0
        white_layout = QVBoxLayout(white_section)
        white_layout.setContentsMargins(0, 0, 0, 0)
        white_layout.setSpacing(0)

        # Add logo centered in the white area
        logo_label = QLabel()
        logo_pixmap = QPixmap('./unnamed.png')
        logo_label.setPixmap(logo_pixmap.scaledToWidth(200))
        logo_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        white_layout.addWidget(logo_label)

        white_label = QLabel("Welcome to the Landing Page (White Section)")
        white_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        white_layout.addWidget(white_label)
        white_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        main_layout.addWidget(white_section, 1)  # Set the white section to take all available width

        # Add a blue section (0%)
        blue_section = QWidget()
        blue_section.setStyleSheet("background-color: #B7F7EF;")

        # Set layout margins and spacing to 0
        blue_layout = QVBoxLayout(blue_section)
        blue_layout.setContentsMargins(0, 0, 0, 0)
        blue_layout.setSpacing(0)

        blue_label = QLabel("Additional Information (Blue Section)")
        blue_label.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)
        blue_layout.addWidget(blue_label)

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
            }
        """

        button_customers.setStyleSheet(button_styles)
        button_suppliers.setStyleSheet(button_styles)
        button_items.setStyleSheet(button_styles)
        button_sale_register.setStyleSheet(button_styles)

        # Connect buttons to open custom popups
        button_customers.clicked.connect(self.show_custom_popup)
        button_suppliers.clicked.connect(self.show_custom_popup)
        button_items.clicked.connect(self.show_custom_popup)
        button_sale_register.clicked.connect(self.show_custom_popup)

        # Add buttons to the blue layout
        blue_layout.addWidget(button_customers)
        blue_layout.addWidget(button_suppliers)
        blue_layout.addWidget(button_items)
        blue_layout.addWidget(button_sale_register)

        blue_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        main_layout.addWidget(blue_section, 0)  # Set the blue section to a fixed size (0 means it takes no space)

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

        # Set the size to 50% of the main window's size
        main_window_size = self.stack_widget.parent().size()
        login_size = QSize(int(main_window_size.width() * 0.5), int(main_window_size.height() * 0.5))
        self.resize(login_size)

    def on_login_clicked(self):
        # Add authentication logic here (e.g., check username and password)
        # For simplicity, let's assume login is always successful
        landing_page = LandingPage()
        self.stack_widget.addWidget(landing_page)
        self.stack_widget.setCurrentWidget(landing_page)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Accounting Software")
        self.setWindowIcon(QIcon("./icon2.png"))

        # Stack Widget
        stack_widget = QStackedWidget(self)

        registration_page = RegistrationPage(stack_widget)
        login_page = LoginPage(stack_widget)

        stack_widget.addWidget(registration_page)
        stack_widget.addWidget(login_page)

        # Set the initial page to be the registration page
        stack_widget.setCurrentWidget(registration_page)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(stack_widget)  # Add the stack_widget

        central_widget = QWidget(self)
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("background-color: #A4BFD8;")  # Set the initial background color
        self.showMaximized()

    def on_language_changed(self, index):
        # You can add your logic here for language change if needed
        print("Selected Language:", index)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
