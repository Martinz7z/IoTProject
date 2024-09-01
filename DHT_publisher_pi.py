import Adafruit_DHT
import time
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

# Configuration for DHT11 sensor
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # GPIO pin connected to the DHT11 data pin

def main():
    # PubNub setup
    PUBLISH_KEY = 'put key here'
    SUBSCRIBE_KEY = 'put key here'
    
    pnconfig = PNConfiguration()
    pnconfig.publish_key = PUBLISH_KEY
    pnconfig.subscribe_key = SUBSCRIBE_KEY
    pnconfig.uuid = "put your uuid here"  # Set a unique identifier for the client

    pubnub = PubNub(pnconfig)

    def publish_callback(envelope, status):
        if not status.is_error():
            print("Message published successfully")
        else:
            print("Failed to publish message")

    while True:
        # Read humidity and temperature from the sensor
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            message = {
                'temperature': temperature,
                'humidity': humidity
            }
            pubnub.publish().channel("your channel name here").message(message).pn_async(publish_callback)
            print(f"Temp: {temperature:.1f}C  Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from the sensor")

        time.sleep(5)  # Delay between readings

if __name__ == "__main__":
    main()
