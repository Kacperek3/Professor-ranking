import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QHeaderView, QPushButton, QScrollArea, QLabel, QMainWindow, QInputDialog, QLineEdit, QFormLayout, QDialogButtonBox, QDialog
from PyQt6 import QtCore
import pyodbc
import mysql.connector
from PyQt6 import QtCore
import styles

db_config = {
    "host": "localhost",
    "user": "root",
    "database": "ranking"
}

class LoginWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("logowanie.ui", self)

        self.setStyleSheet("background-image: url(logoLogowanie.png);")

        self.lineEdit_username.setStyleSheet(styles.style_sheet)
        self.lineEdit_password.setStyleSheet(styles.style_sheet)
        self.pushButton_2.setStyleSheet(styles.style_sheet)
        self.pushButton.setStyleSheet(styles.style_sheet)
        self.label_2.setStyleSheet(styles.style_sheet)

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.RegisterWin)
        self.register_window = None

    def login(self):
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM logowanie")
        rows = cursor.fetchall()
        for row in rows:
            if row[0] == self.lineEdit_username.text() and row[2] == self.lineEdit_password.text():
                from general import GeneralWindow
                self.general_window = GeneralWindow(self.lineEdit_username.text())
                self.general_window.show()
                self.close()
        conn.close()

    def RegisterWin(self):
        from register import RegisterWindow
        self.register_window = RegisterWindow()
        self.register_window.show()
        self.close()