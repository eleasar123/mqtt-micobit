"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import paho.mqtt.client as mqtt

def display_text(temp):
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(*clue.acceleration)
    clue_data[1].text = "Gyro: {} {} {} dps".format(*clue.gyro)
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(*clue.magnetic)
    clue_data[3].text = "Pressure: {} hPa".format(clue.pressure)
    clue_data[4].text = "Altitude: {:.0f} m".format(clue.altitude)
    clue_data[5].text = "Temperature: {} C".format(temp)
    clue_data[6].text = "Humidity: {} %".format(clue.humidity)
    clue_data[7].text = "Proximity: {}".format(clue.proximity)
    clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(*clue.color)
    clue_data.show()

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe("clue-slider")
        display_text(0)

def on_message(client, userdata, msg):
    input = str(msg.payload.decode())
    print(input)
    slider=input[0:5]
    print(slider)
    payload = input[5:]
    print(payload)
    if slider == "accelX":
        display_text(int(payload))
    if slider == "accelX":
        display_text(int(msg.payload.decode()))
    if slider == "accelY":
        display_text(int(msg.payload.decode()))
    if slider == "accelZ":
        display_text(int(msg.payload.decode()))
    if slider == "magneX":
        display_text(int(msg.payload.decode()))
    if slider == "magneY":
        display_text(int(msg.payload.decode()))
    if slider == "magneZ":
        display_text(int(msg.payload.decode()))
    if slider == "gyroX":
        display_text(int(msg.payload.decode()))
    if slider == "gyroY":
        display_text(int(msg.payload.decode()))
    if slider == "gyroZ":
        display_text(int(msg.payload.decode()))
    if slider == "colorR":
        display_text(int(msg.payload.decode()))
    if slider == "colorG":
        display_text(int(msg.payload.decode()))
    if slider == "colorB":
        display_text(int(msg.payload.decode()))
    if slider == "lightI":
        display_text(int(msg.payload.decode()))
    if slider == "pressU":
        display_text(int(msg.payload.decode()))
    if slider == "tempE":
        display_text(int(msg.payload.decode()))
    if slider == "proxI":
        display_text(int(msg.payload.decode()))
    if slider == "humiD":
        display_text(int(msg.payload.decode()))
    # display_text(int(msg.payload.decode()))

clue.sea_level_pressure = 1020  
clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
