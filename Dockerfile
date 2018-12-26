FROM arm32v7/python:3.7-slim as builder

RUN apt-get update
RUN apt-get install python3-setuptools curl -y

RUN curl -L https://github.com/mgaggero/Adafruit_Python_HTU21D/archive/v1.0.0.tar.gz | tar zx 

RUN cd Adafruit_Python_HTU21D-1.0.0 && python3 setup.py install

FROM arm32v7/python:3.7-slim

COPY --from=builder /usr/local/lib/python3.7/site-packages/Adafruit_HTU21D-1.0.0-py3.7.egg /usr/local/lib/python3.7/site-packages/Adafruit_HTU21D-1.0.0-py3.7.egg

RUN pip3 install paho-mqtt

COPY main.py /
