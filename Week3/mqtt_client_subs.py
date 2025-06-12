import time
import json

import paho.mqtt.client as mqtt

message_received = {}

def on_message(client, userdata, message):
    global message_received
    data = json.loads(message.payload.decode('utf8'))
    print(message.topic)
    print(data)

message_received = data

if __name__ == "__main__":
    local_broker = "broker.hivemq.com"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "healthy_pot")
    client.on_message = on_message
    client.connect(local_broker, 1883, keepalive=15)
    client.subscribe("raspb/temperature/value", qos=0)
    client.loop_start()

    while True:
        print("Waiting for message.")
        print(message_received)
        time.sleep(1)
        if message_received:
            break

    client.loop_stop()
    client.disconnect()

