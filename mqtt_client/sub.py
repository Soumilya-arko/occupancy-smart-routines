import paho.mqtt.client as mqtt
import random
import string

# Function to generate a random client ID
def generate_client_id(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to a topic
    client.subscribe("test/topic")

# Callback when a message is received
def on_message(client, userdata, msg):
    print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

# Create a new MQTT client instance with a random client ID
#client_id = generate_client_id()
#client = mqtt.Client(client_id)
client = mqtt.Client()
# Assign the callback functions
client.on_connect = on_connect
client.on_message = on_message

# Connect to the MQTT broker running on localhost
client.connect("localhost", 1883, 60)

# Start the loop to process network traffic and dispatch callbacks
client.loop_start()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    print("Disconnecting...")
    client.loop_stop()
    client.disconnect()
