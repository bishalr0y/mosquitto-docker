import paho.mqtt.client as mqtt 
from random import randrange, uniform
import time

username = "username"
password = "password"

# mqttBroker ="mqtt.eclipseprojects.io"
mqttBrokerHost = "localhost"
mqttBrokerPort = 1883 

client = mqtt.Client("Temperature_Inside")

client.username_pw_set(username, password)

# client.connect(mqttBroker)
client.connect(mqttBrokerHost, mqttBrokerPort) 

while True:
    randNumber = uniform(20.0, 21.0)
    client.publish("TEMPERATURE", randNumber)
    print("Just published " + str(randNumber) + " to topic TEMPERATURE")
    time.sleep(2)