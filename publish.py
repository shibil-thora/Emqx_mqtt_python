# MQTT Broker Info
# Broker Status:
# Available
# Broker:
# broker.emqx.io
# TCP Port:
# 1883
# WebSocket Port:
# 8083
# SSL/TLS Port:
# 8883
# WebSocket Secure Port:
# 8084
# QUIC Port:
# 14567
# Certificate Authority:
# broker.emqx.io-ca.crt 


# python 3.6

import json
import logging
import random
import time

from paho.mqtt import client as mqtt_client 

BROKER = 'broker.emqx.io'
PORT = 1883
TOPIC = "python/mqtt"
# generate client ID with pub prefix randomly
CLIENT_ID = f'python-mqtt-{random.randint(0, 1000)}'
USERNAME = 'emqx'
PASSWORD = 'public'


def connect_mqtt(): 
    def on_connect(client, userdata, flags, rc): 
        if rc == 0: 
            print('Connected to MQTT Broker') 

        else: 
            print(f'Failed to connect, return code {rc}') 

    client = mqtt_client.Client(CLIENT_ID)  
    client.username_pw_set(username=USERNAME, password=PASSWORD) 
    client.on_connect = on_connect 
    client.connect(BROKER, PORT) 
    return client 


def publish(client): 
    msg_count = 1 
    while True: 
        time.sleep(1) 
        msg = f'Messages: {msg_count}' 
        result = client.publish(TOPIC, msg) 

        status = result[0] 
        if status == 0: 
            print(f'send {msg} to topic: {TOPIC}') 
        else: 
            print(f'Failed to send message to topic {TOPIC}') 
        msg_count += 1 
        if msg_count > 5: 
            break 

def run(): 
    client = connect_mqtt() 
    client.loop_start()
    publish(client) 
    client.loop_stop()  


if __name__ == '__main__': 
    run()