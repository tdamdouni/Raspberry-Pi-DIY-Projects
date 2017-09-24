from gpiozero import MCP3008, PWMLED

pot1 = MCP3008(0)
pot2 = MCP3008(1)
led = PWMLED(21)

while True:
    print(pot1.value, pot2.value)
    led.blink(on_time=pot1.value, off_time=pot2.value, n=1, background=False)
