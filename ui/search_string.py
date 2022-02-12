import PyQt5.QtGui
import PyQt5.QtCore
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QPushButton


class SearchString(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.city_entry = QLineEdit()
        self.city_entry.setPlaceholderText('Введите город')
        self.city_entry.setFont(PyQt5.QtGui.QFont('SansSerif', 12))
        self.btn = QPushButton('Поиск')
        self.btn.setFont(PyQt5.QtGui.QFont('SansSerif', 12))
        self.btn.setShortcut(PyQt5.QtCore.Qt.Key_Return)
        self.addWidget(self.city_entry)
        self.addWidget(self.btn)

    def setClickCallback(self, find_button_callback):
        self.btn.clicked.connect(find_button_callback)

    def addTextChangedCallback(self, textChangedCallback):
        self.city_entry.textChanged.connect(textChangedCallback)
