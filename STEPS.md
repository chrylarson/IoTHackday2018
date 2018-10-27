On PI
- set password on PI
- connect PI to WiFi
- `sudo ifconfig` to get IP address of RaspberryPi

On Laptop
- Open Terminal
- `ssh pi@{ip_address}`

On PI
- `cd ~/`
- `wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.40.tar.xz`
- `tar xvf bluez-5.40.tar.xz`
- `sudo apt-get update`
- `sudo apt-get install -y libusb-dev libdbus-1-dev libglib2.0-dev libudev-dev libical-dev libreadline-dev`
- `cd bluez-5.40`
- `./configure`
- `make`
- `sudo make install`
- `systemctl status bluetooth`
- 
```
pi@CBraspberrypi:~/IoTHackday2018 $ systemctl status bluetooth
● bluetooth.service - Bluetooth service
   Loaded: loaded (/lib/systemd/system/bluetooth.service; enabled)
   Active: active (running) since Sat 2018-10-27 10:17:10 CDT; 58min ago
     Docs: man:bluetoothd(8)
 Main PID: 879 (bluetoothd)
   Status: "Running"
   CGroup: /system.slice/bluetooth.service
           └─879 /usr/lib/bluetooth/bluetoothd
```
- `sudo apt-get install python-pip`
- `sudo apt-get install libglib2.0-dev`
- `sudo pip3 install bluepy`
- `sudo pip3 install guizero`
