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