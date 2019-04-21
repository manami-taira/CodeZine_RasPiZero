$ nano notify_to_slack.py
#!/usr/bin/python
# -*- coding: utf-8 -*-
import slackweb
import Adafruit_DHT
sensor = Adafruit_DHT.DHT22
pin = 23
slack = slackweb.Slack(url="https://hooks.slack.com/services/xxxxxxxxx/xxxxxxxxx/xxxxxxxxxxxxxxxxx")
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
        msg = u"現在の温度は{0:0.1f}度、湿度は{1:0.1f}% です".format(temperature, humidity)
else:
        msg = u"温湿度を測定できませんでした"

slack.notify(text=msg)
print msg
