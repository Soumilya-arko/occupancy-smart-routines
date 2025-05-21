import paho.mqtt.client as mqtt
import random
import string
import time

# Function to generate a random client ID
def generate_client_id(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print(f"Failed to connect, return code {rc}")

# Callback when the message is published
def on_publish(client, userdata, mid):
    print(f"Message {mid} published.")

def main():
    # Generate random client ID
    #client_id = generate_client_id()

    # Create MQTT client instance
    client = mqtt.Client()

    # Assign callbacks
    client.on_connect = on_connect
    client.on_publish = on_publish

    # Connect to the MQTT broker running on localhost
    client.connect("localhost", 1883, 60)

    # Start the network loop
    client.loop_start()

    topic = "test/topic"
    message = "Hello MQTT, this is a test message."

    # Publish a message to the topic
    result = client.publish(topic, message)

    # Wait for the publish acknowledgment
    status = result[0]
    if status == 0:
        print(f"Sent `{message}` to topic `{topic}`")
    else:
        print(f"Failed to send message to topic {topic}")

    # Wait to ensure message is sent before disconnecting
    time.sleep(2)

    # Stop the loop and disconnect
    client.loop_stop()
    client.disconnect()

if __name__ == "__main__":
    main()

