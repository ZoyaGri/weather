import json
import sys

from PyQt5.QtWidgets import QApplication

from data.api_weather import ApiWeather
from ui.error_dialog import ErrorDialog

from ui.window import Window

if __name__ == "__main__":
    app = QApplication(sys.argv)

    api = ApiWeather()
    w = Window()


    def showCurrentWeather():
        try:
            current_weather = api.current_weather(w.h_search.city_entry.text())
            temp = json.dumps(current_weather['main']['temp'])
            clouding = json.dumps(current_weather['weather'][0]['description'], ensure_ascii=False)
            wind = json.dumps(current_weather['wind']['speed'], ensure_ascii=False)

            w.setTempValue(temp)
            w.setCloudinessValue(clouding)
            w.setWindValue(wind)
        except:
            ErrorDialog()

    w.click_button(showCurrentWeather)
    w.show()

    sys.exit(app.exec_())
