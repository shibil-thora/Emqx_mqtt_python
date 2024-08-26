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
TOPIC = "python-mqtt/tcp"
# generate client ID with pub prefix randomly
CLIENT_ID = f'python-mqtt-tcp-pub-sub-{random.randint(0, 1000)}'
USERNAME = 'emqx'
PASSWORD = 'public'

FIRST_RECONNECT_DELAY = 1
RECONNECT_RATE = 2
MAX_RECONNECT_COUNT = 12
MAX_RECONNECT_DELAY = 60

FLAG_EXIT = False


def connect_mqtt(): 
    pass