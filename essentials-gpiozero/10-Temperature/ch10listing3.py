from gpiozero import MCP3008, LEDBarGraph
from time import sleep

def convert_temp(gen):
    for value in gen:
        yield (value * 3.3 - 0.5) * 100

adc = MCP3008(channel=7)
graph = LEDBarGraph (26, 19, 13, 6, 5, pwm=True)

for temp in convert_temp(adc.values):
    bars = temp / 35
    graph.value = bars
    sleep(1)


