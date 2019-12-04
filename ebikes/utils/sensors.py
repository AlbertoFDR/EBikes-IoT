from typing import Tuple

import seeed_dht


class WeatherSensor:
    def __init__(self, dht_type="11", pin=12):
        self.sensor = seeed_dht.DHT(dht_type, pin)

    @property
    def value(self) -> Tuple[float, float]:
        return self.sensor.read()
