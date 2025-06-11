#intruder_client_pubs.py

import time
import json
import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
from francislib import irsensor
from francislib import sounds

def ask_user():
    """""
    global intruder_present
    if input ("Is there an intruder present? (yes/no): ").strip().lower() == "yes":
        intruder_present = True  
    else:
        intruder_present = False
    """""
    global intruder_present
    global alarm_value
    intruder_present = irsensor.get_state()
    if intruder_present:
        sounds.set_alarm(True)
        alarm_value = "On"
    else:
        sounds.set_alarm(False)
        alarm_value = "Off"

        
    

if __name__ == "__main__":
    user_name = "Kevin_Fox"
    intruder_present = False  # Default value, can be changed by user input
    local_broker = "broker.hivemq.com"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "intruder_detector")
    client.connect(local_broker, 1883, keepalive = 15)
    client.loop_start()

    try:
        while True:
            ask_user()
            
            #Read value from sensor
            #intruder_present = True
        
            
            payload = {"User": user_name, "intruder": intruder_present, "alarm": alarm_value}
            
            client.publish("Kevin_Fox/intruder/alarm_value", json.dumps(payload), qos=0)
    except KeyboardInterrupt:
        print("Exiting the program")

    client.loop_stop()
    client.disconnect()
