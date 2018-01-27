import smbus
import time

DEV_ADDRESS = 0x15


class Bearable():
    def __init__(self):
        self.bus=smbus.SMBus(1)
        self.leds = [0]*12

    def enable_hack_mode(self, on=True):
        if on:
            self.bus.write_byte_data(DEV_ADDRESS,0,0x11)
        else:
            self.bus.write_byte_data(DEV_ADDRESS,0,0x10)
        
    def set_led(self,number, brightness):
        self.leds[number] = min(brightness,8)
        
    def clear(self):
        self.leds = [0]*12
        self.update()    
        
    def update(self):
        for i in range(0, len(self.leds), 2):
            byte = self.leds[i]*16 +self.leds[i+1]
            index = (i/2)+1
            self.bus.write_byte_data(DEV_ADDRESS, index, byte)
            
if __name__=="__main__":
    bear = Bearable()
    bear.enable_hack_mode(True)
    for i in range(6):
        for j in range(8):
            bear.set_led(i,j)
            bear.set_led(i+6,j)
            bear.update()
            time.sleep(0.050)
        for j in range(8):
            bear.set_led(i, 7-j)
            bear.set_led(i+6, 7-j)
            bear.update()
            time.sleep(0.050)
        time.sleep(0.200)
        bear.clear()
        bear.update()
    bear.enable_hack_mode(False)
                        