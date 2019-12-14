from typing import Tuple

import seeed_dht
from grove.adc import ADC


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