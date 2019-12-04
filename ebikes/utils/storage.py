import requests


def save_corlysis(temperature, humidity, loudness, gases):
    url = "https://corlysis.com:8086/write"
    params = {"db": "ebikes-iot", "u": "token", "p": "15b6a2088bbd8f1d3ed3449f4495c394"}
    payload_temp = "Temperature, type=celsius value=" + temperature + "\n"
    payload_hum = "Humidity, type=percentage value=" + humidity + "\n"
    payload_loud = "Loudness, type=signal value=" + loudness + "\n"
    payload_gas = "Gases, type=gases value=" + gases + "\n"
    payload = payload_temp + payload_hum + payload_loud + payload_gas
    requests.post(url, params=params, data=payload)

