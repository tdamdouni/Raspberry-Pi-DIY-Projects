from bottle import route, run, template, request
import os

ID = 'B0 A1 56'
MIDDLE = ' 06 C9 '

ZONES = {
    'zone1': {'on': '03', 'off': '04'},
    'zone2': {'on': '05', 'off': '06'},
    'zone3': {'on': '07', 'off': '08'},
    'zone4': {'on': '09', 'off': '0A'}}

def light_on(zone):
    print(zone + "on")
    send(ZONES[zone]['on'])


def light_off(zone):
    print(zone + "off")
    send(ZONES[zone]['off'])

def send(code):
    global ID, MIDDLE
    for i in range(1, 5):
        message = ID + MIDDLE + code + ' 00'
        os.system('./send_cmd "' + message + '"')

# Handler for the home page
@route('/')
def index():
    zone = request.GET.get('zone', 'zone1')
    state = request.GET.get('state', 'off')
    if state == 'on':
        light_on(zone)
    else:
        light_off(zone)
    return template('home.tpl')

# Start the webserver running on port 80
run(host="0.0.0.0", port=80)