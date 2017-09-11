#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


# mqtt credentials. Also make sure to change device_id at bottom of page
creds = {
    'clientId': 'T/eaQlBtWSJyks0VxsZ43Rg',
    'user':     'fde69094-1b56-489c-a4b3-4571b19e3746',
    'password': 'pnNDgJl5XTu8',
    'topic':    '/v1/fde69094-1b56-489c-a4b3-4571b19e3746/',
    'server':   'mqtt.relayr.io',
    'port':     1883
}
#function to read temperature
def read_temperature(device_id):
    "Read float temperature value from 1wire device DS18B20."
    #with open('/sys/bus/w1/devices/%s/w1_slave' % device_id) as f:
    with open('/sys/bus/cpu/devices/cpu0/cpufreq/cpuinfo_min_freq') as f:
        text = f.read().strip()
        fragments = text.split()
        return float(fragments[-1][2:]) / 1000.

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
        # read sensor
        device_id = 'fde69094-1b56-489c-a4b3-4571b19e3746'
        sensor_value = read_temperature(device_id)
        # publish temerature data
        message = {
            'meaning': 'temperature',
            'value': sensor_value
        }
        client.publish(credentials['topic'] + 'data', json.dumps(message))
        time.sleep(publishing_period / 1000.)

if __name__ == '__main__':
    main(creds, publishing_period)
