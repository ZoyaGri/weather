import requests

'''api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}&lang={lang}&units={metric}'''


class ApiWeather:
    APPID = "8d90a13839dfe5a70557a160822df916"
    URL_BASE = "http://api.openweathermap.org/data/2.5/"

    def current_weather(self, city_name: str = "Chicago") -> dict:
        query_params = {
            "q": city_name,
            "appid": self.APPID,
            "lang": "ru",
            "units": "metric"
        }
        return requests.get(self.URL_BASE + "weather", params=query_params).json()
