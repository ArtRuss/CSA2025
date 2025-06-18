from francislib import sounds
import toml
import paho.mqtt.client as mqtt
import logging

config = {} 
with open("config.toml", "r") as f:
    config = toml.load(f)

# Perform actions based on message from MQTT server
def on_message(client, userdata, message):
    msg = message.payload.decode()
    if msg == "alarm off":
        sounds.set_alarm(False)
# Configure logger
logging.basicConfig(filename='intruder_detector.log', filemode='w', level=logging.INFO)

# Create MQTT client
client = mqtt.Client()
client.connect(config["broker"], config["port"], keepalive=15)
logging.info("Successfully connected to MQTT server")

# Subscribe to topic and check for message
client.subscribe(config["off"])
client.on_message = on_message
client.loop_forever()