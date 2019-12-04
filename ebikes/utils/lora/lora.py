from typing import Tuple

import ebikes.utils.lora.lib as pyrfm

conf = {
    'll': {
        'type': 'rfm95'
    },
    'pl': {
        'type': 'serial_seed',
        'port': '/dev/serial0'
    }
}


class LoraEndpoint:
    def __init__(self, modem="Bw125Cr45Sf128", preamble_length=8, frequency=433, tx_power=13):
        self.ll = pyrfm.getLL(conf)
        if self.ll.setOpModeSleep(True, True):
            self.ll.setFiFo()
            self.ll.setOpModeIdle()
            self.ll.setModemConfig(modem)
            self.ll.setPreambleLength(preamble_length)
            self.ll.setFrequency(frequency)
            self.ll.setTxPower(tx_power)

    def read(self) -> Tuple[bytes, bytes]:
        if self.ll.waitRX(timeout=3):
            data = self.ll.recv()
            header = data[0:4]
            msg = data[4:]
            return header, msg

    def write_string(self, text: str) -> None:
        self.ll.sendStr(text)
        self.ll.waitPacketSent()

    def write(self, data: bytes) -> None:
        self.ll.send(data)
        self.ll.waitPacketSent()
