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

    weather_sensor = sensors.WeatherSensor(dht_type=WEATHER_SENSOR_DHT, pin=WEATHER_SENSOR_PIN)
    gas_sensor = sensors.GasSensorMQ2(GAS_SENSOR_CHANNEL)
    loudness_sensor = sensors.LoudnessSensor(LOUDNESS_SENSOR_CHANEEL)

    while True:
        humidity, temperature = weather_sensor.value
        gas = gas_sensor.value
        loudness = loudness_sensor.value

        gps = None  # todo: get gps data (lon,lat)

        sensor_data = {
            prot.HUMIDITY_FIELD: humidity,
            prot.TEMPERATURE_FIELD: temperature,
            prot.GAS_FIELD: gas,
            prot.LOUDNESS_FIELD: loudness,
            prot.GPS_FIELD: gps
        }
        encoded_data = prot.dump_sensor_data(sensor_data)
        lora_endpoint.write(encoded_data)

        time.sleep(SAMPLING_FREQUENCY)
