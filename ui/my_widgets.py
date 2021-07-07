from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class drawable_label(QLabel):
    def __init__(self, parent, event):
        QLabel.__init__(self, parent)
        self.event = event
        self.setStyleSheet('QLabel {background-color: #000000; color: #000000;}')
    def mousePressEvent(self, e):
        point = (e.pos().x(), e.pos().y())
        self.event.E_label_press(point)

class clickable_label(QLabel):
    def __init__(self, parent, event):
        QLabel.__init__(self, parent)
        self.event = event
        self.setStyleSheet('QLabel {background-color: #000000; color: #E6E6E6;}')
    def mousePressEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            self.event.label_click()
        elif e.buttons() == Qt.RightButton:
            self.event.del_click()

class alart_label(QLabel):
    def __init__(self, parent, event):
        QLabel.__init__(self, parent)
        self.event = event

    def mousePressEvent(self, e):
        self.event.pop_cam_click()

class my_btn(QPushButton):
    def __init__(self, parent):
        QPushButton.__init__(self, parent)
        self.setStyleSheet('QPushButton {background-color: #424242; color: #E6E6E6;}')

class my_list(QListWidget):
    def __init__(self, parent):
        QListWidget.__init__(self, parent)
        self.setStyleSheet('QListWidget {background-color: #000000; color: #E6E6E6;}')

class my_edit(QTextEdit):
    def __init__(self, parent):
        QTextEdit.__init__(self, parent)
        self.setStyleSheet('QTextEdit {background-color: #000000; color: #E6E6E6;}')

class my_line_edit(QLineEdit):
    def __init__(self, parent):
        QLineEdit.__init__(self, parent)
        self.setStyleSheet('QLineEdit {background-color: #000000; color: #E6E6E6;}')

class my_label(QLabel):
    def __init__(self, parent):
        QLabel.__init__(self, parent)
        self.setStyleSheet('QLabel {background-color: #242424; color: #E6E6E6;}')

class my_rdo(QRadioButton):
    def __init__(self, parent):
        QRadioButton.__init__(self, parent)
        self.setStyleSheet('QRadioButton {color: #E6E6E6;}')

class my_cb(QCheckBox):
    def __init__(self, parent):
        QCheckBox.__init__(self, parent)
        self.setStyleSheet('QCheckBox {background-color: #000000; color: #E6E6E6;}')
