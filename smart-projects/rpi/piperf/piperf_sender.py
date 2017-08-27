## Client (sending out psutils info)
#import piperf
import socket
import psutil
import time


def get_cpu_temp():
    args = ["vcgencmd", "measure_temp"]
    perf = subprocess.check_output(args)
    return float(perf.strip().split("=")[1].split("'")[0])

HOST = '127.0.0.1'
PORT = 54749
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#s.sendall("Hello world")
while 1:
    cpu_load = psutil.cpu_percent(interval=1)
    cpu_temp = get_cpu_temp()
    mem_load = psutil.virtual_memory().percent
    disk_load = psutil.disk_usage("/").percent
    s.sendall("{}\t{}\t{}\t{}".format(cpu_temp, cpu_load, mem_load, disk_load))
    time.sleep(5)

s.close()

