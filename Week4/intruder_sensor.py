from francislib import irsensor
import toml
import paho.mqtt.client as mqtt
import logging
import time

config = {} 
with open("config.toml", "r") as f:
    config = toml.load(f)

# Configure logger
logging.basicConfig(filename='intruder_detector.log', filemode='w', level=logging.INFO)

# Create MQTT client
client = mqtt.Client()
client.connect(config["broker"], config["port"], keepalive=15)
logging.info("Successfully connected to MQTT server")

# Check for intruder
while True:
    if irsensor.get_state():
        # Publish message to MQTT server
        client.publish(config["report"], "intruder detected")
        logging.info("Intruder detected, message published")
    time.sleep(5) # Check every 5 seconds