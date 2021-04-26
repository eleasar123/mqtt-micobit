from microbit import *
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("mousemovement")
        display.show(Image.YES)

def on_message(client, userdata, msg):
    if msg.payload.decode() == "north":
        display.show(Image.ARROW_N)
    if msg.payload.decode() == "northeast":
        display.show(Image.ARROW_NE)
    if msg.payload.decode() == "southeast":
        display.show(Image.ARROW_SE)
    if msg.payload.decode() == "south":
        display.show(Image.ARROW_S)
    if msg.payload.decode() == "southwest":
        display.show(Image.ARROW_SW)
    if msg.payload.decode() == "northwest":
        display.show(Image.ARROW_NW)
    if msg.payload.decode() == "west":
        display.show(Image.ARROW_W)
    if msg.payload.decode() == "east":
        display.show(Image.ARROW_E)
    else:
        display.show(Image.NO)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("wss://test.mosquitto.org:8081/mqtt", 1883, 60)

client.loop_forever()
