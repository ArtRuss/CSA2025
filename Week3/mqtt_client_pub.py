import time
import json

import paho.mqtt.client as mqtt

if __name__ == "__main__":
    local_broker = "broker.hivemq.com"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "temperature_controller")
    client.connect(local_broker, 1883, keepalive=15)
    client.loop_start()

    try:
        while True:
            answer = int(input("What value of temperature should we publish?"))
            payload = {"temperature": {"value": answer, "unit": "celsius"}}
            client.publish("raspb/temperature/value", json.dumps(payload), qos=0)

    except KeyboardInterrupt:
        print("\nGracefully exiting application...")

    print("Closing connection.")
    client.loop_stop()
    client.disconnect()
