import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from design import Ui_MainWindow
import requests
import json

class OsnoVne(QtWidgets.QMainWindow):
    def __init__(self):
        super(OsnoVne, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    
    def init_UI(self):
        self.setWindowTitle('Прогноз погоди')
        self.setWindowIcon(QIcon('icon.png'))
        self.ui.vikno.setPlaceholderText('Berlin, Germany')
        self.ui.Button.clicked.connect(self.pogoda)

    def pogoda(self):
        token_weather = '7fa3ef27d19879aaf8926d6a096b1fff'
        city = self.ui.vikno.text()
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token_weather}&units=metric')
        data = r.json()
        with open('data.txt', 'w+') as outfile:
            json.dump(r.json(), outfile)
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']

        text = f'У {city} {temp}°'
        text2 = f'Швидкість вітру: {wind} км/год'
        text3 = f'Вологість: {humidity}%'
        text4 = f'Відчувається як: {feels_like}°'

        self.ui.invisible_edit.setText(str(text))
        self.ui.inviseble_edit2.setText(str(text4))
        self.ui.inviseble_edit3.setText(str(text3))
        self.ui.inviseble_edit4.setText(str(text2))
app = QtWidgets.QApplication([])
application = OsnoVne()
application.show()

sys.exit(app.exec())