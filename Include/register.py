import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, \
    QHeaderView, QPushButton, QScrollArea, QLabel, QMainWindow, QInputDialog, QLineEdit, QFormLayout, QDialogButtonBox, \
    QDialog
from PyQt6 import QtCore
import pyodbc


server = 'demopython2023.database.windows.net'
database = 'demo'
username = 'sqladmin'
password = 'Tytan.2004'
driver = '{ODBC Driver 17 for SQL Server}'


class RegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("rejestracja.ui", self)

        self.setStyleSheet("background-image: url(logo.png);")
        self.setFixedSize(601,474)
        style_sheet = """
                    QTextEdit {
                        color: white;  
                        background-color: black;  
                        border: 3 solid black;
                        border-radius: 10px;
                    }
                    QTextEdit::placeholder {
                        color: white;  
                        background-color: black; 
                    }
                    QLabel{
                        color: white;
                    }
                    QPushButton{
                        color: white;  
                        border: 3 solid black;
                        border-radius: 10px;
                    }
                     QPushButton:pressed {
                        background-color: gray; 
                        border: 1px solid black;
                     }
                """

        self.textEdit_username.setStyleSheet(style_sheet)
        self.textEdit_pasword.setStyleSheet(style_sheet)
        self.pushButton_2.setStyleSheet(style_sheet)
        self.pushButton.setStyleSheet(style_sheet)
        self.label_2.setStyleSheet(style_sheet)

        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.other)
        self.login_Window = None

    def register(self):
        conn = pyodbc.connect(f'SERVER={server};DATABASE={database};UID={username};PWD={password};DRIVER={driver}')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Logowanie")
        rows = cursor.fetchall()

        wprowadzone_haslo = self.textEdit_pasword.toPlainText()

        for row in rows:
            if row[0] == self.textEdit_username.toPlainText() and row[1] == self.textEdit_pasword.toPlainText():
                print("zalogowano")
        conn.close()


    def other(self):
        from login import LoginWindow
        self.login_Window = LoginWindow()
        self.login_Window.show()
        self.close()