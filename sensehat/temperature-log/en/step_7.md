## Automating the script

It might be useful to have this script running when the Raspberry Pi starts up. To do this, it's best to clean up the script a little, so that you can easily comment out the lines that draw the graph. Below is the same script tidied into functions, and with the graph-drawing line commented out:

```python
from gpiozero import CPUTemperature
from time import sleep, strftime, time
import matplotlib.pyplot as plt

cpu = CPUTemperature()

plt.ion()
x = []
y = []

def write_temp(temp):
    with open("cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()    

while True:
    temp = cpu.temperature
    write_temp(temp)
#    graph(temp)
    sleep(1)

```

- Automating scripts is simple with **crontab**. This is basically a file where commands can be placed that will run at certain times or after certain events. To begin, open up a terminal window (press **Ctrl + Alt + T**).

- To edit the crontab, you just type:

    ```bash
    crontab -e
    ```
- Scroll to the bottom of the file and add this single line:

    ```bash
    @reboot python3.4 /home/pi/temp_monitor.py
    ```

    This assumes that your script is called `temp_monitor.py` and that it's saved in your home directory.

- Now reboot your Raspberry Pi. Give it a little time to run, then type the following in a terminal window:

    ```bash
    cat cpu_temp.csv
    ```

    This will enable you to see the contents of the CSV file.

- If you want to see a graph, then just uncomment the `graph(temp)` line using IDLE and run the file.

