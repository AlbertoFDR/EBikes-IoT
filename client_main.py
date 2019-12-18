import os
import time

from dotenv import load_dotenv
load_dotenv()

from ebikes import sensors, protocol as prot
from ebikes.fake_gps import gps
from ebikes.lora import lora


SAMPLING_FREQUENCY = int(os.getenv("SAMPLING_FREQUENCY"))

WEATHER_SENSOR_DHT = os.getenv("WEATHER_SENSOR_DHT")
WEATHER_SENSOR_PIN = int(os.getenv("WEATHER_SENSOR_PIN"))
GAS_SENSOR_CHANNEL = int(os.getenv("GAS_SENSOR_CHANNEL"))
LOUDNESS_SENSOR_CHANEEL = int(os.getenv("LOUDNESS_SENSOR_CHANEEL"))

if __name__ == "__main__":
    lora_endpoint = lora.LoraEndpoint()
    print("Lora [OK]")
    weather_sensor = sensors.WeatherSensor(dht_type=WEATHER_SENSOR_DHT, pin=WEATHER_SENSOR_PIN)
    print("Weather sensor ready [OK]")
    gas_sensor = sensors.GasSensorMQ2(GAS_SENSOR_CHANNEL)
    print("Gas sensor ready [OK]")
    loudness_sensor = sensors.LoudnessSensor(LOUDNESS_SENSOR_CHANEEL)
    print("Loudness sensor ready [OK]")
    gps_sensor = gps.GPS()

    try:
        while True:
            print("Getting data from sensors...")
            humidity, temperature = weather_sensor.value
            print(f"Humidty: {humidity}")
            print(f"Temperature: {temperature}")
            gas = gas_sensor.value
            print(f"Gas: {gas}")
            loudness = loudness_sensor.value
            print(f"Loudness: {loudness}")

            latitude, longitude = gps_sensor.value
            print(f"GPS: {(latitude, longitude)}")
            print("All data got from sensors [OK]")
            sensor_data = {
                prot.HUMIDITY_FIELD: humidity,
                prot.TEMPERATURE_FIELD: temperature,
                prot.GAS_FIELD: gas,
                prot.LOUDNESS_FIELD: loudness,
                prot.LATITUDE_FIELD: latitude,
                prot.LONGITUDE_FIELD: longitude
            }
            encoded_data = prot.dump_sensor_data(sensor_data)
            print(f"JSON data encoded: {encoded_data}")
            print(f"Sending data to Lora Endpoint...")
            lora_endpoint.write_string(encoded_data)
            print(f"Data sent [OK]")

            print(f"Sleeping {SAMPLING_FREQUENCY} seconds...")
            time.sleep(SAMPLING_FREQUENCY)
    except:
        print("Ebikes Client exit.")
