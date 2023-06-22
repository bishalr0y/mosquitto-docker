import paho.mqtt.server as mqtt


def on_connect(client, userdata, flags, rc):
    print(f"Client connected: {client}")


def on_message(client, userdata, msg):
    print(f"Message received: {msg.topic} - {msg.payload}")


def on_publish(client, userdata, mid):
    print("Message published")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Client subscribed")


def on_disconnect(client, userdata, rc):
    print(f"Client disconnected: {client}")


broker_host = "localhost"
broker_port = 1883


mqtt_server = mqtt.MQTTServer(broker_host, broker_port)

mqtt_server.on_connect = on_connect
mqtt_server.on_message = on_message
mqtt_server.on_publish = on_publish
mqtt_server.on_subscribe = on_subscribe
mqtt_server.on_disconnect = on_disconnect

mqtt_server.start()
