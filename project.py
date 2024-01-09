import sys
import json
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget

settings = {}
try:
    with open('accounting.json', 'r') as file:
        settings = json.load(file)
except FileNotFoundError:
    settings = {}
print(settings)            


app = QApplication(sys.argv)
window = QWidget()  # Instantiate the QWidget class
window.showMaximized()
window.setWindowTitle('Admin Registration')
window.show()
sys.exit(app.exec())
