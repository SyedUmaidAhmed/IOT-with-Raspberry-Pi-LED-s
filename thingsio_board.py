import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
import json

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.OUT)
iot_hub = "demo.thingsboard.io"
port= 1883


#paste your username here fetched from thingsboard.io account
username="---------"


password=""
topic="v1/devices/me/telemetry"
client=mqtt.Client()
client.username_pw_set(username,password)
client.connect(iot_hub,port)
print("connection success")

data = dict()

while True:
    GPIO.output(18,GPIO.HIGH)
    print("Led is on now")
    data["GPIO-Status"]="ON"
    data_out=json.dumps(data)
    client.publish(topic,data_out,0)
    
    time.sleep(2)

    GPIO.output(18,GPIO.LOW)
    print("Led is off now")
    data["GPIO-Status"]="OFF"
    data_out=json.dumps(data)
    client.publish(topic,data_out,0)


    
    time.sleep(2)
