import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QSplitter, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        splitter = QSplitter(Qt.Orientation.Horizontal)

        # First partition (80%)
        first_widget = QWidget()
        first_widget.setStyleSheet("background-color: white;")
        splitter.addWidget(first_widget)
        splitter.setStretchFactor(0, 8)  # Set stretch factor for the first widget

        # Second partition (20%)
        second_widget = QWidget()
        second_widget.setStyleSheet("background-color: black;")
        splitter.addWidget(second_widget)
        splitter.setStretchFactor(1, 2)  # Set stretch factor for the second widget

        # Set up the main layout
        layout = QVBoxLayout()
        layout.addWidget(splitter)

        # Set the layout for the main window
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Partitioned Window")
        self.showMaximized()
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
