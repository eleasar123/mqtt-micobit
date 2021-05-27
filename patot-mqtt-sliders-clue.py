"""
To get started, check out the "Device Simulator Express: Getting Started" command in the command pallete, which you can access with `CMD + SHIFT + P` For Mac and `CTRL + SHIFT + P` for Windows and Linux.

To learn more about the CLUE and CircuitPython, check this link out:
https://learn.adafruit.com/adafruit-clue/circuitpython

Find example code for CPX on:
https://blog.adafruit.com/2020/02/12/three-fun-sensor-packed-projects-to-try-on-your-clue-adafruitlearningsystem-adafruit-circuitpython-adafruit/
"""

from adafruit_clue import clue
import paho.mqtt.client as mqtt

def display_text():
    clue_data[0].text = "Accel: {} {} {} m/s^2".format(accelX,accelY, accelZ)
    clue_data[1].text = "Gyro: {} {} {} dps".format(gyroX, gyroY,gyroZ)
    clue_data[2].text = "Magnetic: {} {} {} uTesla".format(magnetX, magnetY, magnetZ)
    clue_data[3].text = "Pressure: {} hPa".format(clue.pressure)
    clue_data[4].text = "Altitude: {:.0f} m".format(clue.altitude)
    clue_data[5].text = "Temperature: {} C".format(temp)
    clue_data[6].text = "Humidity: {} %".format(clue.humidity)
    clue_data[7].text = "Proximity: {}".format(clue.proximity)
    clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(colorR, colorG, colorB, lightI)
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
        accelX=int(payload)
        display_text(accelX)
    elif slider == "accelX":
        accelY=int(payload)
        display_text(accelY)
    elif slider == "accelZ":
        accelZ=int(payload)
        display_text(accelZ)
    elif slider == "magneX":
        magnetX=int(payload)
        display_text(magnetX)
    elif slider == "magneY":
        magnetY=int(payload)
        display_text(magnetY)
    elif slider == "magneZ":
        magnetZ=int(payload)
        display_text(magnetZ)
    elif slider == "gyroX":
        gyroX=int(payload)
        display_text(gyroX)
    elif slider == "gyroY":
        gyroY=int(payload)
        display_text(gyroY)
    elif slider == "gyroZ":
        gyroZ=int(payload)
        display_text(gyroZ)
    elif slider == "colorR":
        colorR=int(payload)
        display_text(colorR)
    elif slider == "colorG":
        colorG=int(payload)
        display_text(colorG)
    elif slider == "colorB":
        colorB=int(payload)
        display_text(colorB)
    elif slider == "lightI":
        lightI=int(payload)
        display_text(lightI)
    elif slider == "pressU":
        clue.pressure=int(payload)
        display_text(clue.pressure)
    elif slider == "tempE":
        temp=int(payload)
        display_text(temp)
    elif slider == "proxI":
        clue.proximity=int(payload)
        display_text(clue.proximity)
    elif slider == "humiD":
        clue.humidity=int(payload)
        display_text(clue.humidity)
    # display_text(int(msg.payload.decode()))
display_text()
clue.sea_level_pressure = 1020  
clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
