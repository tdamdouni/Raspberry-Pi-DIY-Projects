Python app to demonstrate using inputs and outputs on a Raspberry Pi
================================================================================

This is a sample application shows how to use simple inputs and outputs on a
Raspberry Pi.  There is a server side component that runs in Bluemix (Cloud Foundry) and
a Python client that runs on a Raspberry Pi.

The input is a simple button.  The output is a simple LED.  If you click on/off
in the web UI in Bluemix it will turn a LED on/off.  If you press the button
it will send a text message using Twilio to the phone number and message you
type in the web ui.

To Use (Client Side - Raspberry Pi)
================================================================================

```
git clone git://git.drogon.net/wiringPi
cd wiringPi
./build
curl -LO https://github.com/ibm-messaging/iot-raspberrypi/releases/download/1.0.2/iot_1.0-1_armhf.deb
sudo dpkg -i iot_1.0-1_armhf.deb
service iot getdeviceid
sudo apt-get install python-pip
git clone https://github.com/IBM-Bluemix/python-iot-raspberry-pi.git
cd python-iot-raspberry-pi
sudo pip install -r requirements.txt
```

The client requires a file ```/home/pi/device.cfg``` to exist.
The org, auth-key, auth-token can be generated at (sign into bluemix.net first) https://internetofthings.ibmcloud.com/dashboard.  Click on API keys to generate one.

The file should look like the following
```
[application]
org=youriotorg
id=yourdeviceid
type=apikey
auth-key=yourapikey
auth-token=yourapitoken
```

To Use (Server Side)
================================================================================

```
cf create-service iotf-service iotf-service-free iot-python
#replace the phone number with a phone number you registered with twilio
cf set-env python-iot-hackathon PHONE_NUMBER_FROM "+19192006462"
#replace the device ID with the device id of your raspberry pi
#you can get it by running service iot getdeviceid on your raspberry pi
cf set-env python-iot-hackathon DEVICE_ID "b827eb36267d"
cf push myappname
```

Replace myapp name with the name of your app (ex. python-raspberry-pi)

or click the button below

[![Deploy to Bluemix](https://bluemix.net/deploy/button.png)](https://bluemix.net/deploy?repository=https://github.com/IBM-Bluemix/python-iot-raspberry-pi.git)

License
================================================================================

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

<http://www.apache.org/licenses/LICENSE-2.0>

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
