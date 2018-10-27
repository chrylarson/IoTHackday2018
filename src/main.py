#!/usr/bin/python

from bluepy.btle import Scanner, DefaultDelegate
from guizero import App, Text, TextBox, PushButton, Slider, Picture, Waffle
import time
import config
import operator

class ScanBLE(DefaultDelegate):
    def __init__(self, iface=0):
        DefaultDelegate.__init__(self)

    # ID -> Name
    def idToName(self, id):
        if id in config.BEACON_MAP:
            return config.BEACON_MAP[id]
        return id

    # RSSI -> Feet
    # -90 = 35 feet
    # -10 = 2 feet
    def rssiToFeet(self, rssi):
        return (rssi * -1) * config.RATIO + config.OFFSET

    # Dictionary -> Key, Value
    # returns the first item of a dictionary
    def firstItem(self, data):
        key = list(data.keys())[0]
        value = data[key]
        return {key: value}

scan = Scanner().withDelegate(ScanBLE())
location = ""

app = App(title="Hello world", width=960, height=420)

welcome_message = Text(app, text="Welcome to the Mobile Nurse App")

def say_my_name():
    welcome_message.value = location

def change_text_size(slider_value):
    welcome_message.size = slider_value

text_size = Slider(app, command=change_text_size, start=10, end=80)

my_map = Picture(app, image="map.png", width=900, height=350)

def loopIt():
    device_list  = {}
    devices = scan.scan(4.0)

    for dev in devices:
      if dev.addr in config.BEACON_MAP:
        device_list[dev.addr] = dev.rssi
    
    key = max(device_list.items(), key=operator.itemgetter(1))[0]
    value = device_list[key]
    location = 'Device Location ' + str(ScanBLE().idToName(key)) + ', Distance=' + str(ScanBLE().rssiToFeet(value)) + ' Feet'
    welcome_message.value = location
    print(location)

welcome_message.repeat(5000, loopIt)
app.display()
