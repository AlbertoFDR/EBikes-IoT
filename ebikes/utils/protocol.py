import json
from typing import Dict

TEMPERATURE_FIELD = "TEMPERATURE"
HUMIDITY_FIELD = "HUMIDITY"
LOUDNESS_FIELD = "LOUDNESS"
GAS_FIELD = "GAS"
GPS_FIELD = "GPS"


def dump_sensor_data(sensor_data: Dict) -> bytes:
    return json.dumps(sensor_data)


def load_data_sensor(data: bytes) -> Dict:
    return json.loads(data.decode())
