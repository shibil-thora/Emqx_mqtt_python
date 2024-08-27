import random 

from paho.mqtt import client as mqtt_client 

BROKER = 'broker.emqx.io'
PORT = 1883
TOPIC = "python/mqtt"
CLIENT_ID = f'subscribe-{random.randint(0, 100)}'

USERNAME = 'emqx' 
PASSWORD = 'public'


def connect_mqtt(): 
    def on_connect(client, userdata, flags, rc): 
        if rc == 0: 
            print("Connected to MQTT broker") 
        else: 
            print(f"Failed to connect, return code {rc}") 

    client = mqtt_client.Client(CLIENT_ID) 
    client.username_pw_set(USERNAME, PASSWORD)
    client.on_connect = on_connect 

    client.connect(BROKER, PORT) 
    return client 


def subscibe(client): 
    def on_message(client, userdata, msg): 
        print(f'Received {msg.payload.decode()} from {msg.topic} topic') 

    client.subscribe(TOPIC) 
    client.on_message = on_message 


def run():  
    client = connect_mqtt() 
    subscibe(client) 
    client.loop_forever() 

if __name__ == '__main__': 
    run()