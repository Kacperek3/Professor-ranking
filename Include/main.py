import sys
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout, QHeaderView, QPushButton, QScrollArea, QLabel, QMainWindow, QInputDialog, QLineEdit, QFormLayout, QDialogButtonBox, QDialog
from PyQt6 import QtCore
import pyodbc
from login import LoginWindow

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
    print("alan")
