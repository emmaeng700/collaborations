import paho.mqtt.client as mqtt

# TODO (Akontoke): Connect to HiveMQ broker
# Publish spray commands to topic: pythomedic/robot/spray
# Subscribe to: pythomedic/robot/status

BROKER_URL = "broker.hivemq.com"
BROKER_PORT = 1883
TOPIC_SPRAY  = "pythomedic/robot/spray"
TOPIC_STATUS = "pythomedic/robot/status"

def publish_spray_command(action: str, duration: int):
    client = mqtt.Client()
    client.connect(BROKER_URL, BROKER_PORT)
    payload = f'{{"action": "{action}", "duration": {duration}}}'
    client.publish(TOPIC_SPRAY, payload)
    client.disconnect()
