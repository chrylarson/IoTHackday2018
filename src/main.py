#!/usr/bin/python

from bluepy.btle import Scanner, DefaultDelegate
import time
import config

class ScanBLE(DefaultDelegate):
    def __init__(self, iface=0):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, scanEntry, isNewDev, isNewData):
        if isNewDev:
            print "New ID: ", self.idToName(scanEntry.addr), " RSSI: ", self.rssiToFeet(scanEntry.rssi)
        elif isNewData:
            print "Old ID: ", self.idToName(scanEntry.addr), " RSSI: ", self.rssiToFeet(scanEntry.rssi)
    
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

scan = Scanner().withDelegate(ScanBLE())
devices = scan.scan(10.0)

while True:
    time.sleep(1)
