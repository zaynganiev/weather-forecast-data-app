import requests

API_KEY = "67ab41093046d11990f2a5ac10a80fb0"

def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&cnt={forecast_days}&appid={API_KEY}"
    responce = requests.get(url)
    data = responce.json()
    return data

if __name__ == "__main__":
    print(get_data(place="Tokyo"))