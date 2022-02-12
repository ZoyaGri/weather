from PyQt5.QtWidgets import QMessageBox, QPushButton
import PyQt5.QtGui


class ErrorDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ошибка')
        self.setWindowIcon((PyQt5.QtGui.QIcon('images/ic_error.png')))
        self.setText('Город не найден!')
        self.setInformativeText('Попробуйте еще раз')
        self.setDefaultButton(QPushButton())
        self.exec_()
