#!/usr/bin/python

from bluepy.btle import Scanner, DefaultDelegate
import time
import config
import operator

class ScanBLE(DefaultDelegate):
    def __init__(self, iface=0):
        DefaultDelegate.__init__(self)

    # def handleDiscovery(self, scanEntry, isNewDev, isNewData):
    #     if isNewDev:
    #         print "New ID: ", self.idToName(scanEntry.addr), " RSSI: ", self.rssiToFeet(scanEntry.rssi)
    #     elif isNewData:
    #         print "Old ID: ", self.idToName(scanEntry.addr), " RSSI: ", self.rssiToFeet(scanEntry.rssi)
    
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

while True:
    device_list  = {}
    devices = scan.scan(4.0)

    for dev in devices:
      if dev.addr in config.BEACON_MAP:
        device_list[dev.addr] = dev.rssi
    
    #device_list = sorted(device_list.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    key = max(device_list.items(), key=operator.itemgetter(1))[0]
    value = device_list[key]
    #first = ScanBLE().firstItem(device_list)
    print('Device Location ' + (ScanBLE().idToName(key) + ', Distance=' + ScanBLE().rssiToFeet(value)) + ' Feet')

    time.sleep(1)
