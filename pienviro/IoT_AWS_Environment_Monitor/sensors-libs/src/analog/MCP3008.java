package analog;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.Pin;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;

public class MCP3008 {

    private final Pin clk = RaspiPin.GPIO_01; // Pin #18, clock
    private final Pin in = RaspiPin.GPIO_04; // Pin #23, data in.  MISO: Master In Slave Out
    private final Pin out = RaspiPin.GPIO_05; // Pin #24, data out. MOSI: Master Out Slave In
    private final Pin cs = RaspiPin.GPIO_06; // Pin #25, Chip Select

    private GpioController gpio;
    private GpioPinDigitalInput inDig = null;
    private GpioPinDigitalOutput outDig = null;
    private GpioPinDigitalOutput clkDig = null;
    private GpioPinDigitalOutput csDig = null;

    public boolean initialize() {

        try {
            gpio = GpioFactory.getInstance();
            outDig = gpio.provisionDigitalOutputPin(out, "MOSI", PinState.LOW);
            clkDig = gpio.provisionDigitalOutputPin(clk, "CLK", PinState.LOW);
            csDig = gpio.provisionDigitalOutputPin(cs, "CS", PinState.LOW);
            inDig = gpio.provisionDigitalInputPin(in, "MISO");
            return true;
        } catch (Exception e) {
            System.out.println(e);
            e.printStackTrace();

            return false;

        }

    }
    
        public void shutdown() {
        gpio.shutdown();
    }
        
         public int readFromChannel(int channel) {
        csDig.high();

        clkDig.low();
        csDig.low();

        int adccommand = channel;
        adccommand |= 0x18; // 0x18: 00011000
        adccommand <<= 3;
        // Send 5 bits: 8 - 3. 8 input channels on the MCP3008.
        for (int i = 0; i < 5; i++) //
        {
            if ((adccommand & 0x80) != 0x0) // 0x80 = 0&10000000
            {
                outDig.high();
            } else {
                outDig.low();
            }
            adccommand <<= 1;
            // Clock high and low
            highLowOnPin(clkDig);
        }

        int adcOut = 0;
        for (int i = 0; i < 12; i++) // Read in one empty bit, one null bit and 10 ADC bits
        {
            highLowOnPin(clkDig);
            adcOut <<= 1;

            if (inDig.isHigh()) {

                adcOut |= 0x1;
            }

        }
        csDig.high();

        adcOut >>= 1; // Drop first bit
        return adcOut;
    }

    private static void highLowOnPin(GpioPinDigitalOutput pin) {
        pin.high();
        pin.low();
    }
    
       public double readSPL(int channel) throws InterruptedException {

        int samples = 0;
        int read;
        int highest = 0;
        while (samples < 100) {
            read = readFromChannel(channel);
            if (read > highest) {
                highest = read;
            }

            Thread.sleep(1);

            samples++;
        }

        read = highest;
        double conv = 0;

        if (read <= 527) {
            conv = 60;
        }

        if (read >= 528 && read <= 534) {
            conv = 65.5 + ((read - 528) * 0.8333);
        }

        if (read >= 535 && read <= 556) {
            conv = 70.5 + ((read - 532) * 0.2380);
        }

        if (read >= 557 && read <= 590) {
            conv = 75.5 + ((read - 557) * 0.1363);
        }

        if (read >= 591 && read <= 628) {
            conv = 80 + ((read - 591) * 0.1617);
        }

        if (read >= 629 && read <= 714) {
            conv = 85.5 + ((read - 629) * 0.0529);
        }

        if (read >= 715 && read <= 890) {
            conv = 90 + ((read - 715) * 0.02857);
        }

        if (read >= 891 && read <= 1015) {
            conv = 95 + ((read - 891) * 0.02419);
        }

        if (read > 1015) {
            conv = 100;
        }

        return conv;
    }


}
