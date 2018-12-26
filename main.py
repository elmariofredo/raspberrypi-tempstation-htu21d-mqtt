#!/usr/bin/env python3
#
import os
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
from Adafruit_HTU21D.HTU21D import HTU21D

broker = os.environ["TEMP_BROKER_ADDRESS"]
room_name = os.environ["TEMP_ROOM_NAME"]
delay = int(os.environ["TEMP_BROKER_DELAY"])

client = mqtt.Client()
client.connect(broker)
client.loop_start()

h = HTU21D()

temperature=0
humidity=0

while True:

    
    current_temperature = h.read_temperature()

    current_humidity = h.read_humidity()

    if current_temperature != temperature:
        temperature = current_temperature
        client.publish(room_name + '/temperature', temperature)

    if current_humidity != humidity:
        humidity = current_humidity
        client.publish(room_name + '/humidity', humidity)

    time.sleep(delay)

