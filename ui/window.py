import PyQt5.QtGui
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout
from ui.search_string import SearchString
from ui.temp_description_layout import TempDescriptionLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.h_temp = TempDescriptionLayout('Температура:')
        self.h_cloud = TempDescriptionLayout('Осадки:')
        self.h_wind = TempDescriptionLayout('Ветер м/с:')
        self.h_search = SearchString()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(600, 350)

        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        self.setWindowTitle('Погода')
        self.setWindowIcon(PyQt5.QtGui.QIcon('images/ic_title.png'))

        vertical_container = QVBoxLayout()
        vertical_container.addLayout(self.h_search)
        vertical_container.addLayout(self.h_temp)
        vertical_container.addLayout(self.h_cloud)
        vertical_container.addLayout(self.h_wind)
        vertical_container.addStretch()

        self.setLayout(vertical_container)

    def add_changed_text_callback(self, callback):
        self.h_search.addTextChangedCallback(callback)

    def click_button(self, callback):
        self.h_search.setClickCallback(callback)

    def setTempValue(self, weather):
        self.h_temp.setWeatherValue(weather)

    def setCloudinessValue(self, cloud):
        self.h_cloud.setWeatherValue(cloud)

    def setWindValue(self, wind):
        self.h_wind.setWeatherValue(wind)
