import toml
import paho.mqtt.client as mqtt
import logging

config = {} 
with open("config.toml", "r") as f:
    config = toml.load(f)

# Perform actions based on message from MQTT server
def on_message(client, userdata, message):
    msg = message.payload.decode()
    if msg == "intruder detected":
        logging.info("Intruder detected message received")
        client.publish(config["off"], "alarm on")
        userin = input("Press A to alert authorities, or any other key to just turn off alarm\n")
        if userin.lower() == 'a':
            logging.info("Alerting authorities and turning off alarm")
            client.publish(config["report"], "alert authorities")
            client.publish(config["off"], "alarm off")
        else:
            logging.info("Alarm turned off")
            client.publish(config["off"], "alarm off")

# Configure logger
logging.basicConfig(filename='intruder_detector.log', filemode='w', level=logging.INFO)

# Create MQTT client
client = mqtt.Client()
client.connect(config["broker"], config["port"], keepalive=15)
logging.info("Successfully connected to MQTT server")

# Subscribe to topic and check for message
client.subscribe(config["report"])
client.on_message = on_message
client.loop_forever()