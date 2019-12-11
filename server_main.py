from ebikes.utils.lora.lora import LoraEndpoint
from ebikes.utils.storage import save_corlysis

if __name__ == "__main__":
    print("==================== CLIENT EBIKES ===================== \n")
    lora = LoraEndpoint()
    while True:
        print("Waiting to receive a message... \n")
        msg = lora.read()
        print("Msg received! \n")
        print("Storage in Corlysis! \n")
        #Data to save temperature, humidity, loudness, gases, latitude, longitude
        #save_corlysis(msg)
        print("Data saved \n") 
