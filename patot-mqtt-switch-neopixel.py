from adafruit_circuitplayground import cp
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    # print("Connected with result code "+str(rc))
    if rc == 0:
        cp.red_led = True
        client.subscribe("cpx-switch")
'''This function will interpret the payload message and turn on and
 off the neopixel light index
with the corresponding payload compared to'''
def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode())
    if msg.payload.decode() == "1true":
        cp.pixels[0] = (255, 255, 255)
    elif msg.payload.decode() == "2true":
        cp.pixels[1] = (255, 255, 255)
    elif msg.payload.decode() == "3true":
        cp.pixels[2] = (255, 255, 255)
    elif msg.payload.decode() == "1false":
        cp.pixels[0] = (0, 0, 0)
    elif msg.payload.decode() == "2false":
        cp.pixels[1] = (0, 0, 0)
    elif msg.payload.decode() == "3false":
        cp.pixels[2] = (0, 0, 0)

cp.red_led = False

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()

# Broker for online client: https://iamelijah2016.github.io/
# wss://mqtt.eclipse.org:443/mqtt
# wss://test.mosquitto.org:8081/mqtt