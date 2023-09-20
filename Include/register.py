import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, \
    QHeaderView, QPushButton, QScrollArea, QLabel, QMainWindow, QInputDialog, QLineEdit, QFormLayout, QDialogButtonBox, \
    QDialog
from PyQt6 import QtCore
import pyodbc


db_config = {
    "host": "localhost",     # Host bazy danych
    "user": "root",  # Nazwa użytkownika
    "database": "ranking"   # Nazwa bazy danych
}


class RegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("rejestracja.ui", self)

        self.setStyleSheet("background-image: url(logo.png);")
        self.setFixedSize(601,474)
        style_sheet = """
                    QLineEdit {
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

        self.lineEdit_username.setStyleSheet(style_sheet)
        self.lineEdit_password.setStyleSheet(style_sheet)
        self.pushButton_2.setStyleSheet(style_sheet)
        self.pushButton.setStyleSheet(style_sheet)
        self.label_2.setStyleSheet(style_sheet)

        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.other)
        self.login_Window = None

    def register(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM login")
        rows = cursor.fetchall()

        wprowadzone_haslo = self.textEdit_pasword.toPlainText()

        for row in rows:
            if row[0] == self.lineEdit_username.toPlainText() and row[1] == self.lineEdit_password.toPlainText():
                print("zalogowano")
        conn.close()


    def other(self):
        from login import LoginWindow
        self.login_Window = LoginWindow()
        self.login_Window.show()
        self.close()