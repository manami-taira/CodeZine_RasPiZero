#!/usr/bin/python

import Adafruit_DHT
import datetime

sensor = Adafruit_DHT.DHT22

pin = 23

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
    now = datetime.datetime.now()
    str = '{0},{1:0.1f},{2:0.1f}'.format(now.strftime('%Y/%m/%d %H:%M:%S'),temperature, humidity)
    print str
    with open('/home/pi/sensor_data.csv', mode = 'a') as fh:
      fh.write(str+'\n')
else:
    print 'Fail'
