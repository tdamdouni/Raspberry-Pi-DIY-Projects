# Raspberry Pi System Stats

_Captured: 2017-05-10 at 23:53 from [learn.pimoroni.com](https://learn.pimoroni.com/tutorial/networked-pi/raspberry-pi-system-stats-python)_

Live system stats are the "hello world" of Raspberry Pi networking. In this guide you'll learn about a couple of Python modules:

  * flask - for serving web pages
  * psutil - for getting system stats

By combining these, you will create a simple HTTP server that delivers your system stats in a RESTful fashion. You can jazz this up with javascript to create realtime stats, or just merge everything into one page for a quick overview of your Pi!

## About the modules

Flask is a simple and expressive framework for serving web pages from Python. These can be either static or dynamic, we'll just be using simple routes to serve CPU, Memory and Disk information to three different URLs.

psutil ( Python System & Process Utilities ) is a great little cross-platform module for retrieving various snippets of system information. This will supply the CPU percentage and Memory/Disk utilisation stats that we'll be serving with Flask.

## Installing

Before we start running any scripts, you'll need to install both psutil and Flask, this can be done using the Python Package Manager; pip.

First you'll need to install pip itself ( skip this step if you've already done so ):
    
    
    sudo apt-get install python-pip
    

Then you'll need to install flask and psutil:
    
    
    sudo pip install psutil flask
    

## The Code

Glueing Flask and psutil together into a simple system-stats web service is simple.

The following is a barebones example which will serve up CPU percentage at /cpu and available/total memory at /memory.

### Download Code

Right-click and download: [system-stats.py](https://learn.pimoroni.com/tutorial/networked-pi/system-stats.py)
    
    
    import psutil
    
    from flask import Flask
    
    app = Flask(__name__)
    #app.debug = True # Uncomment to debug
    
    @app.route('/')
    def home():
        return 'System Stats!'
    
    @app.route('/cpu')
    def cpu():
        return str(psutil.cpu_percent()) + '%'
    
    @app.route('/memory')
    def memory():
        memory = psutil.virtual_memory()
        # Divide from Bytes -> KB -> MB
        available = round(memory.available/1024.0/1024.0,1)
        total = round(memory.total/1024.0/1024.0,1)
        return str(available) + 'MB free / ' + str(total) + 'MB total ( ' + str(memory.percent) + '% )'
    
    @app.route('/disk')
    def disk():
        disk = psutil.disk_usage('/')
        # Divide from Bytes -> KB -> MB -> GB
        free = round(disk.free/1024.0/1024.0/1024.0,1)
        total = round(disk.total/1024.0/1024.0/1024.0,1)
        return str(free) + 'GB free / ' + str(total) + 'GB total ( ' + str(disk.percent) + '% )'
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0')
    

Download this code to your Raspberry Pi and run with:
