import requests


def save_corlysis(temperature, humidity, loudness, gases, latitude, longitude):
    url = "https://corlysis.com:8086/write"
    params = {"db": "ebikes-iot", "u": "token", "p": "15b6a2088bbd8f1d3ed3449f4495c394"}
    payload_temp = "Temperature,type=celsius value=" + str(temperature) + "\n"
    payload_hum = "Humidity,type=percentage value=" + str(humidity) + "\n"
    payload_loud = "Loudness,type=loudness value=" + str(loudness) + "\n"
    payload_gas = "Gases,type=gas value=" + str(gases) + "\n"
    payload_lat = "Latitude,type=latitude value=" + str(latitude) + "\n"
    payload_lon = "Longitude,type=longitude value=" + str(longitude) + "\n"

    payload = payload_temp + payload_hum + payload_loud + payload_gas + payload_lat + payload_lon
    requests.post(url, params=params, data=payload)

