#!/usr/bin/env python
from __future__ import division
from subprocess import PIPE, Popen
import psutil
import time
from ISStreamer.Streamer import Streamer

# --------- User Settings ---------
# Initial State settings
BUCKET_NAME = ":computer: Pi3 Performance" 
BUCKET_KEY = "pi0708"
ACCESS_KEY = "PUT YOUR INITIAL STATE ACCESS_KEY HERE"
# Set the time between checks
MINUTES_BETWEEN_READS = 1
METRIC_UNITS = False
# ---------------------------------

def get_cpu_temperature():
    process = Popen(['vcgencmd', 'measure_temp'], stdout=PIPE)
    output, _error = process.communicate()
    return float(output[output.index('=') + 1:output.rindex("'")])


def main():
    streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)
    while True:
        cpu_temperature = get_cpu_temperature()
        if METRIC_UNITS:
            streamer.log("CPU Temperature(C)",cpu_temperature)
        else:
            cpu_temperature = cpu_temperature * 9.0 / 5.0 + 32.0
            streamer.log("CPU Temperature(F)",str("{0:.2f}".format(cpu_temperature)))

        cpu_percents = psutil.cpu_percent(percpu=True)
        streamer.log_object(cpu_percents, key_prefix="cpu")

        cpu_percent = psutil.cpu_percent(percpu=False)
        streamer.log("CPU Usage",cpu_percent)

        disk = psutil.disk_usage('/')
        disk_total = disk.total / 2**30    
        streamer.log("Disk Total(GB)",str("{0:.2f}".format(disk_total))) 
        disk_used = disk.used / 2**30
        streamer.log("Disk Used(GB)",str("{0:.2f}".format(disk_used))) 
        disk_free = disk.free / 2**30
        streamer.log("Disk Free(GB)",str("{0:.2f}".format(disk_free))) 
        disk_percent_used = disk.percent
        streamer.log("Disk Used(%)",str("{0:.2f}".format(disk_percent_used))) 

        mem = psutil.virtual_memory()
        mem_total = mem.total / 2**20      
        streamer.log("Memory Total(MB)",str("{0:.2f}".format(mem_total))) 
        mem_avail = mem.available / 2**20      
        streamer.log("Memory Available(MB)",str("{0:.2f}".format(mem_avail))) 
        mem_percent_used = mem.percent
        streamer.log("Memory Used(%)",str("{0:.2f}".format(mem_percent_used))) 
        mem_used = mem.used / 2**20
        streamer.log("Memory Used(MB)",str("{0:.2f}".format(mem_used))) 
        mem_free = mem.free / 2**20
        streamer.log("Memory Free(MB)",str("{0:.2f}".format(mem_free))) 

        net = psutil.net_io_counters()
        net_bytes_sent = net.bytes_sent / 2**20      
        streamer.log("Network MB Sent",str("{0:.2f}".format(net_bytes_sent))) 
        net_bytes_recv = net.bytes_recv / 2**20      
        streamer.log("Network MB Received",str("{0:.2f}".format(net_bytes_recv))) 
        net_errin = net.errin    
        streamer.log("Network Errors Receiving",str(net_errin)) 
        net_errout = net.errout    
        streamer.log("Network Errors Sending",str(net_errout)) 
        net_dropin = net.dropin    
        streamer.log("Incoming Packets Dropped",str(net_dropin)) 
        net_dropout = net.dropout    
        streamer.log("Outgoing Packets Dropped",str(net_dropout)) 

        streamer.flush()
        time.sleep(60*MINUTES_BETWEEN_READS)

if __name__ == '__main__':
    main()
