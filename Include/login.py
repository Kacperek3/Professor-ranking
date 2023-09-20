import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QHeaderView, QPushButton, QScrollArea, QLabel, QMainWindow, QInputDialog, QLineEdit, QFormLayout, QDialogButtonBox, QDialog
from PyQt6 import QtCore
import pyodbc
import mysql.connector

db_config = {
    "host": "localhost",     # Host bazy danych
    "user": "root",  # Nazwa użytkownika
    "database": "ranking"   # Nazwa bazy danych
}

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("logowanie.ui", self)

        self.setStyleSheet("background-image: url(logo.png);")

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

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.other)
        self.register_window = None

    def login(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM login")
        rows = cursor.fetchall()

        for row in rows:
            if row[0] == self.textEdit_username.toPlainText() and row[1] == self.textEdit_pasword.toPlainText():
                print("zalogowano")
        conn.close()

    def other(self):
        from register import RegisterWindow
        self.register_window = RegisterWindow()  # Tworzenie instancji RegisterWindow
        self.register_window.show()
        self.close()