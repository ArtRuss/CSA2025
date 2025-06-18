#intruder_client_subs.py

import time
import json
import tomllib
import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
from francislib import irsensor

message_rec = {}

def tidy_message(message):
    user = message.get("User")
    intruder = message.get("intruder")
    alarm = message.get("alarm")
    print(f"{user}: {intruder} Alarm is {alarm}")


def on_message(client, userdata, message):
    global message_rec
    try:
        data = json.loads(message.payload.decode('utf-8'))
        message_rec = data
        #print(message.topic)
        #print(data)
        return data
    except json.JSONDecodeError:
        print("Received invalid JSON payload")
        return None
    # Uncomment the line below if you want to store the received message in a global variable
    
    


if __name__ == "__main__":
    with open("config.toml", "rb") as f:
        config = tomllib.load(f)
    
    local_broker = config["mqtt"]["broker"]
    port = config["mqtt"]["port"]
    alive = config["mqtt"]["keepalive"]
    #local_broker = "broker.hivemq.com"
    client = mqtt.Client(callback_api_version=CallbackAPIVersion.VERSION2, client_id="intruder_detector_subscriber")
    client.on_message = on_message
    client.connect(local_broker, port, keepalive=alive)
    try:
        user_name = input("Please enter your user name: ").strip()
    except KeyboardInterrupt:
        exit()
    client.subscribe(f"{user_name}/security", qos=0)
    client.loop_start()
    try:
        while True:
            #print("Waiting for message")
            time.sleep(1)
            data_received = on_message
            if(on_message):
                tidy_message(message_rec)
                #print(message_rec)
    except KeyboardInterrupt:
        print("Program interrupted by user")
    
    client.loop_stop()
    client.disconnect()
    print("Exiting the program")