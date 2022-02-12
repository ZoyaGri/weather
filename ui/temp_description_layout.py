import PyQt5.QtGui
from PyQt5.QtWidgets import QHBoxLayout, QLabel


class TempDescriptionLayout(QHBoxLayout):

    def __init__(self, title):
        super().__init__()
        self.__title = QLabel(title)
        self.__title.setFont(PyQt5.QtGui.QFont('SansSerif', 10))
        self.__temp_value = QLabel()
        self.__temp_value.setFont(PyQt5.QtGui.QFont('SansSerif', 10))
        self.addWidget(self.__title)
        self.addWidget(self.__temp_value)

    def setWeatherValue(self, title):
        self.__temp_value.setText(title)
