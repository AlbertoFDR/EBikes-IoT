import os

GPS_DATA_FILE = os.getenv("GPS_DATA_FILE")


class GPS:
    def __init__(self):
        self._load_data()
        self.index = -1

    def _load_data(self):
        with open(GPS_DATA_FILE) as file:
            data = file.readlines()
        self.data = list(
            map(lambda l: tuple(map(lambda x: float(x), l.split(","))), data)
        )

    @property
    def value(self):
        if self.index >= len(self.data):
            self.index = self.index = 0
        else:
            self.index += 1
        return self.data[self.index]
