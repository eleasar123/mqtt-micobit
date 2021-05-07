from microbit import *
import paho.mqtt.client as mqtt

CIRCLE = Image("09990:90009:90009:90009:09990")
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("mousemovement")
        display.show(Image.YES)
def on_message(client, userdata, msg):
    if msg.payload.decode() == "north":
        display.show(Image.ARROW_N)
    elif msg.payload.decode() == "northeast":
        display.show(Image.ARROW_NE)
    elif msg.payload.decode() == "southeast":
        display.show(Image.ARROW_SE)
    elif msg.payload.decode() == "south":
        display.show(Image.ARROW_S)
    elif msg.payload.decode() == "southwest":
        display.show(Image.ARROW_SW)
    elif msg.payload.decode() == "northwest":
        display.show(Image.ARROW_NW)
    elif msg.payload.decode() == "west":
        display.show(Image.ARROW_W)
    elif msg.payload.decode() == "east":
        display.show(Image.ARROW_E)
    elif msg.payload.decode()=="center":
        display.show(CIRCLE)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
