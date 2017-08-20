import unicornhat
import subprocess
import psutil
import time

unicornhat.brightness(.7)

def get_cpu_temp():
    args = ["vcgencmd", "measure_temp"]
    perf = subprocess.check_output(args)
    return float(perf.strip().split("=")[1].split("'")[0])
    
"""    
def get_ram_load():
    args = ["free"]
    ram = subprocess.check_output(args)
    ram = ram.split("\n")
    for i, line in enumerate(ram):
        if i == 1:
            total, used, free = [x for x in line.strip().split(" ") if x != ""][1:4]
    ram_load = int(used) / float(total)
    print int(total) / 1024.0 , int(used) / 1024.0, int(free) / 1024.0
    return ram_load
"""

def show_bar(perc, color, startpos = 0):
    frac = perc/100.0
    full = int(round(frac*8,0))
    rem = (frac*8) % 1
    for i in range(0, full):
        unicornhat.set_pixel(startpos, i, color[0], color[1], color[2])
        unicornhat.set_pixel(startpos+1, i, color[0], color[1], color[2])
    if full < 8:
        unicornhat.set_pixel(startpos, full, int(color[0]*rem), int(color[1]*rem), int(color[2]*rem))
        unicornhat.set_pixel(startpos+1, full, int(color[0]*rem), int(color[1]*rem), int(color[2]*rem))
    
def show_heat(n, startpos, max_val):
    frac = n / float(max_val)
    rem = (frac*8) % 1
    full = int(frac*8 - rem)
    colors = [(255,0,0), (128, 255, 0), (255, 255, 0), (255,0,0)]
    color = colors[int(round(4*frac,1))-1]
    #print n, frac, full, rem, color
    for i in range(0, full):
        unicornhat.set_pixel(startpos, i, color[0], color[1], color[2])
        unicornhat.set_pixel(startpos+1, i, color[0], color[1], color[2])
    if full < 8:
        unicornhat.set_pixel(startpos, full, int(color[0]*rem), int(color[1]*rem), int(color[2]*rem))
        unicornhat.set_pixel(startpos+1, full, int(color[0]*rem), int(color[1]*rem), int(color[2]*rem))
    

def monitor_pi(cpu_temp, cpu_load, mem_load, disk_load):
    show_heat(cpu_temp, startpos=6, max_val = 80)
    show_bar(cpu_load, color=(255, 92, 0), startpos = 4)
    show_bar(mem_load, color=(0, 255, 255), startpos = 2)
    show_bar(disk_load, color=(255, 0, 255), startpos = 0)
    unicornhat.show()
    
def clean():
    unicornhat.clear()
    
if __name__ == "__main__":
    
    while 1:
        cpu_load = psutil.cpu_percent(interval=1)
        cpu_temp = get_cpu_temp()
        mem_load = psutil.virtual_memory().percent
        disk_load = psutil.disk_usage("/").percent
        show_heat(cpu_temp, startpos=6, max_val = 80)
        show_bar(cpu_load, color=(255, 92, 0), startpos = 4)
        show_bar(mem_load, color=(0, 255, 255), startpos = 2)
        show_bar(disk_load, color=(255, 0, 255), startpos = 0)
        unicornhat.show()
        time.sleep(1)
        unicornhat.clear()
        
        
    
