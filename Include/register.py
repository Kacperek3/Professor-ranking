import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, \
    QHeaderView, QPushButton, QScrollArea, QLabel, QMainWindow, QInputDialog, QLineEdit, QFormLayout, QDialogButtonBox, \
    QDialog, QMessageBox
from PyQt6 import QtCore
import mysql.connector
import pyodbc
import validators
import styles
import messagebox

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


        self.lineEdit_username.setStyleSheet(styles.style_sheet)
        self.lineEdit_email.setStyleSheet(styles.style_sheet)
        self.lineEdit_password.setStyleSheet(styles.style_sheet)
        self.pushButton_2.setStyleSheet(styles.style_sheet)
        self.pushButton.setStyleSheet(styles.style_sheet)
        self.label_2.setStyleSheet(styles.style_sheet)

        self.pushButton.clicked.connect(self.register)
        self.pushButton_2.clicked.connect(self.LoginWin)
        self.login_Window = None

    def register(self):
        if (validators.email(self.lineEdit_email.text()) and not ' ' in self.lineEdit_username.text()  and not ' ' in self.lineEdit_password.text()
                and self.lineEdit_username.text() and self.lineEdit_password.text()):
            self.lineEdit_username.setStyleSheet(styles.style_sheet)
            self.lineEdit_email.setStyleSheet(styles.style_sheet)
            self.lineEdit_password.setStyleSheet(styles.style_sheet)
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            cursor.execute("SELECT username, email FROM logowanie")
            rows = cursor.fetchall()
            for row in rows:
                if row[0] == self.lineEdit_username.text():
                    self.lineEdit_username.setStyleSheet(styles.style_sheet_invalid_data_register)
                    messagebox.show_message_box_same_username_database()
                    return
                if row[1] == self.lineEdit_email.text():
                    self.lineEdit_email.setStyleSheet(styles.style_sheet_invalid_data_register)
                    messagebox.show_message_box_same_email_database()
                    return

            insert_query = "INSERT INTO logowanie (username, email, password) VALUES (%s, %s, %s)"
            data_to_insert = (self.lineEdit_username.text(), self.lineEdit_email.text(), self.lineEdit_password.text())
            cursor.execute(insert_query, data_to_insert)
            connection.commit()
            cursor.close()
            connection.close()

        else:
            if not validators.email(self.lineEdit_email.text()):
                self.lineEdit_email.setStyleSheet(styles.style_sheet_invalid_data_register)
            else:
                self.lineEdit_email.setStyleSheet(styles.style_sheet_valid_data_register)

            if  ' ' in self.lineEdit_username.text() or not self.lineEdit_username.text():
                self.lineEdit_username.setStyleSheet(styles.style_sheet_invalid_data_register)
            else:
                self.lineEdit_username.setStyleSheet(styles.style_sheet_valid_data_register)

            if  ' ' in self.lineEdit_password.text() or not self.lineEdit_password.text():
                self.lineEdit_password.setStyleSheet(styles.style_sheet_invalid_data_register)
            else:
                self.lineEdit_password.setStyleSheet(styles.style_sheet_valid_data_register)

            messagebox.show_message_box_wrong_data_register()

    def LoginWin(self):
        from login import LoginWindow
        self.login_Window = LoginWindow()
        self.login_Window.show()
        self.close()
