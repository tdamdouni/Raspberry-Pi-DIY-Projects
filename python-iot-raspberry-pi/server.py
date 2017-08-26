from flask import Flask,redirect
from flask import render_template
from flask import request
import os, json
import time
import ibmiotf.application
from twilio.rest import TwilioRestClient

vcap = json.loads(os.getenv("VCAP_SERVICES"))
twilioAccount = vcap["user-provided"][0]["credentials"]["accountSID"]
twilioToken = vcap["user-provided"][0]["credentials"]["authToken"]
twilioClient = TwilioRestClient(twilioAccount, twilioToken)

client = None

phoneNumberTo = ""
textMessage = "Button Pushed"
phoneNumberFrom = os.getenv("PHONE_NUMBER_FROM")
deviceId = os.getenv("DEVICE_ID")

def myCommandCallback(cmd):
    global phoneNumberTo
    global textMessage

    payload = json.loads(cmd.payload)
    buttonPushed = payload["buttonPushed"]
    message = twilioClient.messages.create(to=phoneNumberTo, from_=phoneNumberFrom, body=textMessage)
    print buttonPushed
try:
    options = {
        "org": vcap["iotf-service"][0]["credentials"]["org"],
        "id": vcap["iotf-service"][0]["credentials"]["iotCredentialsIdentifier"],
        "auth-method": "apikey",
        "auth-key": vcap["iotf-service"][0]["credentials"]["apiKey"],
        "auth-token": vcap["iotf-service"][0]["credentials"]["apiToken"]
    }
    client = ibmiotf.application.Client(options)
    client.connect()

    client.deviceEventCallback = myCommandCallback
    client.subscribeToDeviceEvents(event="input")

except ibmiotf.ConnectionException as e:
    print e

app = Flask(__name__)

if os.getenv("PORT"):
    port = int(os.getenv("PORT"))
else:
    port = 8080

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/light/<command>', methods=['GET', 'POST'])
def light_route(command):
    print command
    myData = {'command' : command}
    client.publishEvent("raspberrypi", deviceId, "light", "json", myData)
    return redirect("/", code=302)

@app.route('/phoneNumber', methods=['POST'])
def phone_number_route():
    global phoneNumberTo
    global textMessage

    phoneNumber =  request.form['phoneNumber']
    textMessage =  request.form['message']
    if phoneNumber.startswith('+'):
        phoneNumberTo = phoneNumber
    else:
        phoneNumberTo = "+1" + phoneNumber

    return redirect("/", code=302)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
