
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time
import threading


GPIO.setmode(GPIO.BCM)
pin = [21,20,16,19,26]
time = time.asctime(time.localtime(time.time()))
client = mqtt.Client()
passtime = ""

for i in range(len(pin)):
    GPIO.setup(pin[i], GPIO.IN)

def on_connect(client, userdata, rc):
    print("Connected with result code ")
    client.subscribe("/ESP/LED")

def on_message(client, userdata, msg):
    print(msg.topic + " " + msg.payload)

def on_disconnect(client, userdata, rc):
    print("Disconnected")


def key():
    num = 0
    if (GPIO.input(pin[0]) == 1):num = num + 1
    if (GPIO.input(pin[1]) == 1):num = num + 2
    if (GPIO.input(pin[2]) == 1):num = num + 4
    if (GPIO.input(pin[3]) == 1):num = num + 8
    return num

def ticker():

    ticker = GPIO.input(pin[4])
    return ticker


def mqtts_publish(password ,time):

    # if(client.connect):print "connect"
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.username_pw_set("NodeTest", "1234")
    client.connect("m11.cloudmqtt.com", 12980, 60)
    client.publish("/ESP/LED",passtime,2)
    client.loop_forever()



if __name__ == '__main__':
    stage = 1
    password = ""
    pas = ticker()
    inp = 0
    lastinp = 0

    try:
        thread_with_arg = threading.Thread(target = mqtts_publish,args = (password,time))
        thread_with_arg.start()
    except:
        print "kuy"

    while True:
        pas = ticker()
        inp = key()
        lastinp = inp
        if(pas == 0):
            stage = 0
        elif(pas == 1):
            if(stage == 0):
                if(inp == lastinp) : password += str(inp)
                stage = 1
                while True :
                     if(key() == 15): break
                     if(key() == 13):
                         password = ""
                     tg = ticker()
                     if(tg == 0):
                         stage = 0
                     elif(tg == 1):
                         if(stage == 0):
                             password += str(key())
                             stage = 1
                if(password != str(lastinp)):
                    passtime =  password + "," +  time
                    client.publish("/ESP/LED",passtime,2)
        password = ""
