import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
    print("Connected with result code "+ str(rc))

    client.subscribe("/ESP/LED")

def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def mqtts(password):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.username_pw_set("NodeTest", "1234")
    client.connect("m11.cloudmqtt.com", 12980, 60)

    client.publish("/ESP/LED", password)

    client.loop_forever()

if __name__ == '__main__':
    pas = "1234"
    mqtts(pas)
