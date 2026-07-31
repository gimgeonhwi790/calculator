# ch 5.2.1 ui.py
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                             QMessageBox, QPlainTextEdit, QHBoxLayout, 
                             QLineEdit, QComboBox)

from PyQt5.QtGui import QIcon
from PyQt5 import QtCore

class View(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)
        
        self.btn1=QPushButton('Calc',self)
        self.btn2=QPushButton('clear',self)
    
        self.le1=QLineEdit('0',self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        self.le1.setFocus()
        self.le1.selectAll()
        
        self.le2=QLineEdit('0',self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)
        
        self.cb = QComboBox(self)
        self.cb.addItems(['+', '-', '*', '/'])
        
        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)
        
        hbox = QHBoxLayout()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        
        self.setLayout(vbox)
        
        self.setWindowTitle('Calculator')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(350,450)
        
    def setDisplay(self, text="Button Clicked"):
        if not isinstance(text, str):
            text = "Button clicked!"
        self.te1.appendPlainText(text)
    
    def clearMessage(self):
        self.te1.clear()
    