#intruder_client_pubs.py

import time
import json
import tomllib
import logging
import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
from francislib import irsensor
from francislib import sounds

logger = logging.getLogger(__name__)
logging.basicConfig(filename = "intruderLogs.log", level = logging.INFO)



class SecuritySystem:
    """ A class to represent the security system for an intruder detector. """
    def __init__(self, user_name):
        self.user_name = user_name
        self.intruder_present = False
        self.alarm_on = False
        # To make output more readable, we will use messages instead of boolean values
        self.intruder_message = "No intruder detected"
        self.alarm_message = "Alarm is OFF"
    
    def get_user_name(self):
        return self.user_name
    
    def get_sensor(self):
        return irsensor.get_state()
        #return False

    """ Checks the state of the sensor and updates the alarm accordingly. """
    def check_security(self):
        intruder_present = self.get_sensor()
        if intruder_present:
            logger.info("Intruder Detected!")
            sounds.set_alarm(True) #Physically turns on the rasperry pi buzzer
            self.alarm_on = True
            logger.info("Sounding the alarm!")
            self.alarm_message = "ON"
            self.intruder_message = "Intruder detected!"
        else:
            sounds.set_alarm(False) #Physically turns off the rasperry pi buzzer
            self.alarm_on = False
            self.alarm_message = "OFF"
            self.intruder_message = "No intruder detected"

if __name__ == "__main__":
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)
    
    local_broker = config["mqtt"]["broker"]
    port = config["mqtt"]["port"]
    alive = config["mqtt"]["keepalive"]
    
    try:
        user_name = input("Please enter your user name: ").strip()
    except KeyboardInterrupt: 
        logger.info("Exiting the program")
        exit()

    s1 = SecuritySystem(user_name)
    client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2,
                         client_id = "intruder_detector")
    client.connect(local_broker, port, keepalive = alive)
    client.loop_start()

    try:
        while True:
            print(s1.intruder_message, s1.alarm_message)
            s1.check_security() #checks the state of the sensor and updates the alarm accordingly
            payload = {"User": user_name, "intruder": s1.intruder_message, "alarm": s1.alarm_message}
            topic = f"{s1.get_user_name()}/security"
            client.publish(topic, json.dumps(payload), qos=0)

    except KeyboardInterrupt:
        print("Exiting the program")
        logger.info("Exiting the program")

    client.loop_stop()
    client.disconnect()
