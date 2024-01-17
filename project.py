# Import area
import sys
import json
import os
import winreg
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
from cryptography.fernet import Fernet,InvalidToken
import base64


# Class definition
class AccountingApp(QWidget):
    # Property
    settings = {}
    encryption_Key = Fernet.generate_key().decode()
    cipher = Fernet(encryption_Key)

    # Constructor
    def __init__(self):
        super().__init__()
        print('hello from constructor')
        # Let's try to read a json file
        self.readJsonFile()
        self.checkAdminIsCreated()
        self.buildUI()

    # Method
        
    def encrypt_value(self, value):
        encrypt_value = self.cipher.encrypt(value.encode())
        return encrypt_value

    def decrypt_value(self, encrypt_value):
        try:
            decrypt_value = self.cipher.decrypt(encrypt_value).decode()
            return decrypt_value
        except InvalidToken:
         print("Error: Invalid or corrupted token. Unable to decrypt.")
         return None
            
    def checkAdminIsCreated(self):
        print("hello from checkAdminIsCreated ")

        key_path = r"SOFTWARE\as"
        value_name = "dt"
        default_json = '{"isAdmincreated":false,"isLicenseActivated":false}'
        encrypted_default_json = self.encrypt_value(default_json)
        encoded_encrypted_default_json = base64.b64encode(encrypted_default_json).decode()

        key = None
        try:
            # Open the registry key for reading
            key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path)
            # Read the value
            encrypt_value, _ = winreg.QueryValueEx(key, value_name)

            if encrypt_value:
                # Decrypt the value if it exists
                print(key)
                dt_value = winreg.QueryValueEx(key, "dt")
                print(dt_value)
                decoded_encrypt_value = base64.b64decode(encrypt_value)
                print(f"Decoded value before decryption: {decoded_encrypt_value}")
                decrypt_value = self.decrypt_value(decoded_encrypt_value)
                print(f"Existing decrypted value: {decrypt_value}")
                decrypt_value = self.decrypt_value(encrypt_value)
                print(f"Existing decrypted value: {decrypt_value}")
            else:
                # Encrypt and create an entry with the registry key and set the default JSON string
                print("Create an entry dt with default JSON value")
                winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, encoded_encrypted_default_json)
        except FileNotFoundError:
            key = winreg.CreateKey(winreg.HKEY_LOCAL_MACHINE, key_path)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, encoded_encrypted_default_json)
        finally:
            if key:
                winreg.CloseKey(key)

    def readJsonFile(self):
        try:
            with open('accounting.json', 'r') as file:
                self.settings = json.load(file)
        except FileNotFoundError:
            self.settings = {}
        print(self.settings)
        print(type(self.settings))


    def buildUI(self):
        self.setStyleSheet('background-color: #A4BFD8;')
        self.setWindowTitle(self.settings.get("windowTitle", ""))
        self.showMaximized()
        self.show()
        icon_path = self.settings.get("iconPath", "")
        if os.path.exists(icon_path):
            icon = QIcon(icon_path)
            self.setWindowIcon(icon)

# Create ClassObject
app = QApplication([])
ceo = AccountingApp()
ceo.showMaximized()
sys.exit(app.exec())
