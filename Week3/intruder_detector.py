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
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "intruder_detector_mtoro")
    client.on_message = on_message # Has to do with receiving messages
    client.connect("broker.hivemq.com", 1883, keepalive=15)
    client.subscribe("MATIAS_TORO/intruder/alarm/report", qos=0) # Making default qos value explicit
    client.loop_start()

    while True:
        print("Sir Lancelot is scanning the premises...")
        print(message_received)
        time.sleep(1)
        if message_received:
            break

    if message_received["status"]["value"]:
        print("Brace thyselves! An attack is upon us!")
    else:
        print("Rest easy my lieges. No attack spotted.")

    client.loop_stop()
    client.disconnect()

'''
'''

"""
MQTT based intruder detector:

Receive the alarm of an intruder: [x]
- Subscribe to topic: [x] THIS WILL DEAL W/ RECEIVING MESSAGES


YOUR_NAME/intruder/alarm/report [x]

Decide an action: []
- Turn off the alarm: []
- Publish to topic: [ ]




THIS IS WHAT THE LISTENER DECIDES WHO TO SNITCH TO

YOUR_NAME/intruder/alarm/value/off [ ] 
 + You need to publish here

- Report to authorities: [ ]
- Publish to topic: [ ]

YOUR_NAME/intruder/authorities/report [ ]
"""

"""
TEST SCRIPT:

+ We need to write a test sript to publish the intruder alarm.
+ We should do something like "get intruder state", which we can just plug Francis's data into.
"""


'''
[ ] AFTER YOU'RE DONE, YOU NEED TO MAKE RANDOM DATA POINTS TO SKIP THE DECISION TREE
'''
