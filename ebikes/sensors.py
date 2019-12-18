from typing import Tuple

import seeed_dht
from grove.adc import ADC
import os

CLEAN_AIR = float(os.getenv("CLEAN_AIR"))

class WeatherSensor:
    def __init__(self, dht_type="11", pin=12):
        self.sensor = seeed_dht.DHT(dht_type, pin)

    @property
    def value(self) -> Tuple[float, float]:
        """
        :return: (humidty, temperature)
        """
        return self.sensor.read()


class LoudnessSensor:
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def value(self):
        return self.adc.read(self.channel)


class GasSensorMQ2:
    def __init__(self, channel):
        self.channel = channel
        self.adc = ADC()

    @property
    def value(self):
        return self.adc.read(self.channel)

def calculate_gas_ratio(gas_value):
    sensor_volt = gas_value/1024*5.0
    RS_gas = (5.0-sensor_volt)/sensor_volt
    ratio = RS_gas/CLEAN_AIR
    return ratio