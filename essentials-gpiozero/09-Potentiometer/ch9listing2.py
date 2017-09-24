from gpiozero import MCP3008, PWMLED

pot = MCP3008(0)
led = PWMLED(21)

led.source = pot.values
    
