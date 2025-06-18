import time
import json

import paho.mqtt.client as mqtt

message_received = {}

def on_message(client, userdata, message):
    global message_received
    data = json.loads(message.payload.decode('utf8'))
    print(data)
    print(message.topic)

    if data["answer"] != "not_correct":
        message_received = data

if __name__ == "__main__":
    local_broker = "broker.hivemq.com"
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, "YOUR_TEAM_NAME")
    client.on_message = on_message
    client.connect(local_broker, 1883, keepalive=15)
    client.subscribe("csa2025/BerryGood/final_clue", qos=0)
    client.loop_start()
    
    try:     
        
        while True: 
            payload = {
                    "smallest_age": "19",
                    "second_tallest_student": "Aryan",
                    "most_favorite_sport": "soccer",
                    "least_hrs_a_day_to_read": "0",
                    "cinema_or_theather": "cinema",
                    "continent_least_travelled": "antarctica",
                    "team": "BerryGood"
            }
            client.publish("csa2025/request_final_clue", json.dumps(payload), qos=0)
            print("Waiting for final clue.")
            print(message_received)       
            time.sleep(1)
            if message_received:
                print(message_received)
                break

    except KeyboardInterrupt:
        print("\nGracefully exiting application...")

    print("Closing connection.")
    client.loop_stop()
    client.disconnect()

    print("\tTo obtain one life you will pay")
    print("\tA team picture at the grotto it will be")
    print("\tTo arrive without it do not dare")
    print("\tFor it will not matter how much you plea\n")