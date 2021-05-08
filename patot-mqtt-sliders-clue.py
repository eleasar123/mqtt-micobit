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
        clue_data[0].text = "Accel: {} {} {} m/s^2".format(accelX=int(payload))
        # display_text(int(payload))
    elif slider == "accelX":
        clue_data[0].text = "Accel: {} {} {} m/s^2".format(accelY=int(payload))
    elif slider == "accelZ":
        clue_data[0].text = "Accel: {} {} {} m/s^2".format(accelZ=int(payload))
    elif slider == "magneX":
        clue_data[2].text = "Magnetic: {} {} {} uTesla".format(magnetX=int(payload))
    elif slider == "magneY":
        clue_data[2].text = "Magnetic: {} {} {} uTesla".format(magnetY=int(payload))
    elif slider == "magneZ":
        clue_data[2].text = "Magnetic: {} {} {} uTesla".format(magnetZ=int(payload))
    elif slider == "gyroX":
        clue_data[1].text = "Gyro: {} {} {} dps".format(gyroX=int(payload))
    elif slider == "gyroY":
        clue_data[1].text = "Gyro: {} {} {} dps".format(gyroY=int(payload))
    elif slider == "gyroZ":
        clue_data[1].text = "Gyro: {} {} {} dps".format(gyroZ=int(payload))
    elif slider == "colorR":
        clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(colorR=int(payload))
    elif slider == "colorG":
        clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(colorG=int(payload))
    elif slider == "colorB":
        clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(colorB=int(payload))
    elif slider == "lightI":
        clue_data[8].text = "Color: R: {} G: {} B: {} C: {}".format(lightI=int(payload))
    elif slider == "pressU":
        clue_data[3].text = "Pressure: {} hPa".format(clue.pressure=int(payload))
    elif slider == "tempE":
        clue_data[5].text = "Temperature: {} C".format(temp=int(payload))
    elif slider == "proxI":
        clue_data[7].text = "Proximity: {}".format(clue.proximity=int(payload))
    elif slider == "humiD":
        clue_data[6].text = "Humidity: {} %".format(clue.humidity=int(payload))
    # display_text(int(msg.payload.decode()))
display_text()
clue.sea_level_pressure = 1020  
clue_data = clue.simple_text_display(text_scale=2)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()
