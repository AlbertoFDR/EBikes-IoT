import time

from ebikes.utils import protocol as prot
from ebikes.utils import sensors
from ebikes.utils.lora import lora

SAMPLING_FREQUENCY = 60

WEATHER_SENSOR_DHT = "11"
WEATHER_SENSOR_PIN = 12
GAS_SENSOR_CHANNEL = 0
LOUDNESS_SENSOR_CHANEEL = 2

if __name__ == "__main__":
    lora_endpoint = lora.LoraEndpoint()
    print("Lora [OK]")
    weather_sensor = sensors.WeatherSensor(dht_type=WEATHER_SENSOR_DHT, pin=WEATHER_SENSOR_PIN)
    print("Weather sensor [OK]")
    gas_sensor = sensors.GasSensorMQ2(GAS_SENSOR_CHANNEL)
    print("Gas sensor [OK]")
    loudness_sensor = sensors.LoudnessSensor(LOUDNESS_SENSOR_CHANEEL)
    print("Loudness sensor [OK]")

    while True:
        print("Getting data from sensors...")
        humidity, temperature = weather_sensor.value
        print(f"Humidty: {humidity} [OK]")
        print(f"Temperature: {temperature} [OK]")
        gas = gas_sensor.value
        print(f"Gas: {gas} [OK]")
        loudness = loudness_sensor.value
        print(f"Loudness: {loudness} [OK]")

        gps = None  # todo: get gps data (lon,lat)
        print(f"GPS: {gps} [OK]")
        print("All data got from sensors [OK]")
        sensor_data = {
            prot.HUMIDITY_FIELD: humidity,
            prot.TEMPERATURE_FIELD: temperature,
            prot.GAS_FIELD: gas,
            prot.LOUDNESS_FIELD: loudness,
            prot.GPS_FIELD: gps
        }
        encoded_data = prot.dump_sensor_data(sensor_data)
        print(f"Sending data to Lora Endpoint...")
        lora_endpoint.write(encoded_data)
        print(f"Data sent [OK]")

        time.sleep(SAMPLING_FREQUENCY)
