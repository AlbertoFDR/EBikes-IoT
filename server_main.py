from ebikes.protocol import load_data_sensor
from ebikes.lora.lora import LoraEndpoint
from ebikes.storage import Storage
import os

from dotenv import load_dotenv
load_dotenv()

STORAGE_HOST = os.getenv("STORAGE_HOST")
STORAGE_PORT = int(os.getenv("STORAGE_PORT"))
STORAGE_USERNAME = os.getenv("STORAGE_USERNAME")

if __name__ == "__main__":
    print("==================== CLIENT EBIKES ===================== \n")
    lora = LoraEndpoint()
    storage = Storage(STORAGE_HOST, STORAGE_PORT, STORAGE_USERNAME)
    try:
        while True:
            print("Waiting to receive a message...")
            encoded_data = lora.read()
            print(f"Encoded data received: {encoded_data}")
            decoded_data = load_data_sensor(encoded_data)
            print("Data stored!")
            storage.store_data(decoded_data)
            print("Data saved")
    except:
        storage.close()
        print("Ebikes Server exit.")

