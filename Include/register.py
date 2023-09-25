import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, \
    QHeaderView, QPushButton, QScrollArea, QLabel, QMainWindow, QInputDialog, QLineEdit, QFormLayout, QDialogButtonBox, \
    QDialog, QMessageBox
from PyQt6 import QtCore
import mysql.connector
import pyodbc
import validators

db_config = {
    "host": "localhost",
    "user": "root",
    "database": "ranking"
}


class RegisterWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("rejestracja.ui", self)

        self.setStyleSheet("background-image: url(logoRejestracja.png);")
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
        self.lineEdit_email.setStyleSheet(style_sheet)
        self.lineEdit_password.setStyleSheet(style_sheet)
        self.pushButton_2.setStyleSheet(style_sheet)
        self.pushButton.setStyleSheet(style_sheet)
        self.label_2.setStyleSheet(style_sheet)

        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.LoginWin)
        self.login_Window = None

    def register(self):
        if (validators.email(self.lineEdit_email.text()) and not ' ' in self.lineEdit_username.text()  and not ' ' in self.lineEdit_password.text()
                and self.lineEdit_username.text() and self.lineEdit_password.text()):
            print("zdane")
        else:
            self.show_message_box()

    def show_message_box(self):
        # Tworzenie MessageBoxa
        message_box = QMessageBox()
        message_box.setWindowTitle("BŁĄD")
        message_box.setText("Błąd podczas rejestracji.")
        message_box.setIcon(QMessageBox.Icon.Information)
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        message_box.exec()

    def LoginWin(self):
        from login import LoginWindow
        self.login_Window = LoginWindow()
        self.login_Window.show()
        self.close()
