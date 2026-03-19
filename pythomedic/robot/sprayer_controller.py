import paho.mqtt.client as mqtt
import json

# TODO (Akontoke): Runs on Raspberry Pi attached to the sprayer hardware
# Subscribes to MQTT topic from the backend
# Triggers GPIO pins to activate spray pump

BROKER_URL   = "broker.hivemq.com"
BROKER_PORT  = 1883
TOPIC_SPRAY  = "pythomedic/robot/spray"
TOPIC_STATUS = "pythomedic/robot/status"

def on_message(client, userdata, msg):
    command = json.loads(msg.payload.decode())
    if command.get("action") == "spray":
        duration = command.get("duration", 3)
        # TODO: activate GPIO spray pump for `duration` seconds
        print(f"Spraying for {duration}s")

def start():
    client = mqtt.Client()
    client.on_message = on_message
    client.connect(BROKER_URL, BROKER_PORT)
    client.subscribe(TOPIC_SPRAY)
    print("Robot controller listening...")
    client.loop_forever()

if __name__ == "__main__":
    start()
