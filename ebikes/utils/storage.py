import requests


def save_corlysis(temperature, humidity, loudness, gases):
    url = "https://corlysis.com:8086/write"
    params = {"db": "ebikes-iot", "u": "token", "p": "15b6a2088bbd8f1d3ed3449f4495c394"}
    payload_temp = "Temperature,type=celsius value=" + temperature + "\n"
    payload_hum = "Humidity,type=percentage value=" + humidity + "\n"
    payload_loud = "Loudness,type=loudness value=" + loudness + "\n"
    payload_gas = "Gases,type=gas value=" + gases + "\n"
    payload = payload_temp + payload_hum + payload_loud + payload_gas
    r = requests.post(url, params=params, data=payload)

save_corlysis("32", "30", "30", "30")
