import json
from typing import Dict

TEMPERATURE_FIELD = "temperature"
HUMIDITY_FIELD = "humidity"
LOUDNESS_FIELD = "loudness"
GAS_FIELD = "gas"
LATITUDE_FIELD = "latitude"
LONGITUDE_FIELD = "longitude"


def dump_sensor_data(sensor_data: Dict) -> str:
    return json.dumps(sensor_data)


def load_data_sensor(data: bytes) -> Dict:
    return json.loads(data.decode())
