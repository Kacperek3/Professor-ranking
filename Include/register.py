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
        style_sheet_invalid = """
                            QLineEdit {
                                color: white;  
                                background-color: red;  
                                border: 3 solid red;
                                border-radius: 10px;
                            }
                    """
        if (validators.email(self.lineEdit_email.text()) and not ' ' in self.lineEdit_username.text()  and not ' ' in self.lineEdit_password.text()
                and self.lineEdit_username.text() and self.lineEdit_password.text()):
            print("zdane")
        else:
            if not validators.email(self.lineEdit_email.text()):
                self.lineEdit_email.setStyleSheet(style_sheet_invalid)

            if  ' ' in self.lineEdit_username.text() or not self.lineEdit_username.text():
                self.lineEdit_username.setStyleSheet(style_sheet_invalid)

            if  ' ' in self.lineEdit_password.text() or not self.lineEdit_password.text():
                self.lineEdit_password.setStyleSheet(style_sheet_invalid)







    def LoginWin(self):
        from login import LoginWindow
        self.login_Window = LoginWindow()
        self.login_Window.show()
        self.close()
