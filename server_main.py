from ebikes.utils.protocol import load_data_sensor
from ebikes.utils.lora.lora import LoraEndpoint
from ebikes.utils.storage import save_corlysis

if __name__ == "__main__":
    print("==================== CLIENT EBIKES ===================== \n")
    lora = LoraEndpoint()
    while True:
        print("Waiting to receive a message...")
        encoded_data = lora.read()
        print(f"Encoded data received: {encoded_data}")
        decoded_data = load_data_sensor(encoded_data)
        print(f"Decoded data: {load_data_sensor(encoded_data)}")
        print("Storage in Corlysis!")
        #Data to save temperature, humidity, loudness, gases, latitude, longitude
        #save_corlysis(msg)
        print("Data saved")

