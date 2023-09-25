from PyQt6.QtWidgets import QMessageBox
import sys


def show_message_box_wrong_data_register():
    message_box = QMessageBox()
    message_box.setWindowTitle("BŁĄD")
    message_box.setText("Nieprawidłwe dane.")
    message_box.setIcon(QMessageBox.Icon.Information)
    message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    message_box.exec()

def show_message_box_same_username_database():
    message_box = QMessageBox()
    message_box.setWindowTitle("BŁĄD")
    message_box.setText("Nazwa użytkownika jest zajęta.")
    message_box.setIcon(QMessageBox.Icon.Information)
    message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    message_box.exec()

def show_message_box_same_email_database():
    message_box = QMessageBox()
    message_box.setWindowTitle("BŁĄD")
    message_box.setText("Email jest już wykorzystany.")
    message_box.setIcon(QMessageBox.Icon.Information)
    message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
    message_box.exec()