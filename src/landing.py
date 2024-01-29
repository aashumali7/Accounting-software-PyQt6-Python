# landing_page.py
import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox
from PyQt6.QtCore import Qt, QMargins

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

if __name__ == "__main__":
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())        
