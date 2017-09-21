#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# publish_mqtt.py

"""
Test publishing device data via MQTT to relayr cloud.

This subscribes to a given MQTT topic and publishes messages
for this topic, so it receives the same messages previously
posted.

This code needs the paho-mqtt package to be installed, e.g.
with "pip install paho-mqtt>=1.1".
"""

import json
import time

import paho.mqtt.client as mqtt

from whatTemper import whatTemper
from whatHumid import whatHumid

# mqtt credentials
creds = {
    'clientId': 'T+UZhMrQjQNS6P2c1zYbSpg',
    'user':     'f9466132-b423-40d4-ba3f-6735cd86d2a6',
    'password': '7P_2ch37D7TY',
    'topic':    '/v1/f9466132-b423-40d4-ba3f-6735cd86d2a6/',
    'server':   'mqtt.relayr.io',
    'port':     1883
}

# ATTENTION !!!
# DO NOT try to set values under 200 ms of the server
# will kick you out
publishing_period = 1000


class MqttDelegate(object):
    "A delegate class providing callbacks for an MQTT client."

    def __init__(self, client, credentials):
        self.client = client
        self.credentials = credentials

    def on_connect(self, client, userdata, flags, rc):
        print('Connected.')
        # self.client.subscribe(self.credentials['topic'].encode('utf-8'))
        self.client.subscribe(self.credentials['topic'] + 'cmd')

    def on_message(self, client, userdata, msg):
        print('Command received: %s' % msg.payload)

    def on_publish(self, client, userdata, mid):
        print('Message published.')


def main(credentials, publishing_period):
    client = mqtt.Client(client_id=credentials['clientId'])
    delegate = MqttDelegate(client, creds)
    client.on_connect = delegate.on_connect
    client.on_message = delegate.on_message
    client.on_publish = delegate.on_publish
    user, password = credentials['user'], credentials['password']
    client.username_pw_set(user, password)
    # client.tls_set(cafile)
    # client.tls_insecure_set(False)
    try:
        print('Connecting to mqtt server.')
        server, port = credentials['server'], credentials['port']
        client.connect(server, port=port, keepalive=60)
    except:
        print('Connection failed, check your credentials!')
        return

    # set 200 ms as minimum publishing period
    if publishing_period < 200:
        publishing_period = 200

    while True:
        client.loop()
        temper_value = whatTemper()
        humid_value = whatHumid()

        # publish data
        message = {
            "meaning": "Temperature", "value": temper_value,
            "meaning": "Humidity", "value": humid_value
        }

        # show what you are sending
        print(temper_value)
        print(humid_value)

        client.publish(credentials['topic'] + 'data', json.dumps(message))

        time.sleep(publishing_period / 1000.)


if __name__ == '__main__':
    main(creds, publishing_period)
