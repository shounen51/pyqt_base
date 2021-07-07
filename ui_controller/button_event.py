import json
import time
import sys
from datetime import datetime
import random
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from utils.utils import load_json, save_json

class btn_events():
    def __init__(self, main_window):
        self.main = main_window

    def btnClike(self):
        print(self.main.ui.textEdit.text())
        self.main.ui.label.setText(self.main.ui.textEdit.text())