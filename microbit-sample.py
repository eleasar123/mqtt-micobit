"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

Get started with micro:bit and MicroPython on:
https://microbit-micropython.readthedocs.io/en/latest/.
"""

from microbit import *
import paho.mqtt.client as mqtt

CIRCLE = Image("09990:90009:90009:90009:09990")

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("mousemovement")
        display.show(Image.YES)

def on_message(client, userdata, msg):
    if msg.payload.decode() == "inside":
        display.show(CIRCLE)
    
    else:
        display.show(Image.NO)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipse.org", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt