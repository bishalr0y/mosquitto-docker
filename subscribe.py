import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, message):
    print("received message: " ,str(message.payload.decode("utf-8")))

# mqttBroker ="mqtt.eclipseprojects.io"
mqttBrokerHost = "localhost"
mqttBrokerPort = 1883
timeToLive = 60

client = mqtt.Client("Smartphone")
client.connect(mqttBrokerHost, mqttBrokerPort, timeToLive) 

client.loop_start()

client.subscribe("TEMPERATURE")

client.on_message=on_message 

time.sleep(10)
print("here")
client.loop_forever()