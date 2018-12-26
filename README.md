# Raspberry pi tempstation

Raspberry pi docker image for HTU21D and with MQTT client

## 1. On raspberry pi start docker image 

$ `docker run --privileged -it --rm -v /dev/i2c-1:/dev/i2c-1 -e TEMP_BROKER_ADDRESS=192.168.0.221 -e TEMP_ROOM_NAME=living_room -e TEMP_BROKER_DELAY=5 6cffc173f21d`

## 2. Add sensor config to homeassistent `configuration.yaml` file

```yaml
sensor:

  - platform: mqtt
    state_topic: 'living_room/temperature'
    name: 'Living room Temperature'
    unit_of_measurement: '°C'
    device_class: temperature

  - platform: mqtt
    state_topic: 'living_room/humidity'
    name: 'Living room Humidity'
    unit_of_measurement: '%'
    device_class: humidity
```
