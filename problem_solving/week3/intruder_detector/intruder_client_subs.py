#intruder_client_subs.py

import time
import json
import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
from francislib import irsensor

message_rec = {}

def on_message(client, userdata, message):
    global message_rec
    try:
        data = json.loads(message.payload.decode('utf-8'))
        print(message.topic)
        print(data)
    except json.JSONDecodeError:
        data = {}
        print("Received invalid JSON payload")
    message_rec = data


if __name__ == "__main__":
    local_broker = "broker.hivemq.com"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "intruder_detector_subscriber")
    client.on_message = on_message
    client.connect(local_broker, 1883, keepalive=15)
    client.subscribe("Kevin_Fox/intruder/alarm_value", qos=0)
    client.loop_start()
    try:
        while True:
            print("Waiting for message")
            time.sleep(1)
            if(message_rec):
                break
    except KeyboardInterrupt:
        print("Program interrupted by user")
    
    client.loop_stop()
    client.disconnect()
    print("Exiting the program")