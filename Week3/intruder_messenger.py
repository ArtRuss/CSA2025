import time
import json

import paho.mqtt.client as mqtt

import time
import json

import paho.mqtt.client as mqtt

if __name__ == "__main__":
    local_broker = "broker.hivemq.com"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "intruder_messenger")
    client.connect(local_broker, 1883, keepalive=15)
    client.loop_start()

    try:
        while True:
            answer = int(input("Is the village being raided? Type 0 for no. Type 1 for yes."))
            payload = {"status": {"value": answer, "unit": "boolints"}}
            client.publish("MATIAS_TORO/intruder/alarm/report", json.dumps(payload), qos=0)

    except KeyboardInterrupt:
        print("\nGracefully exiting application...")

    print("Closing connection.")
    client.loop_stop()
    client.disconnect()
