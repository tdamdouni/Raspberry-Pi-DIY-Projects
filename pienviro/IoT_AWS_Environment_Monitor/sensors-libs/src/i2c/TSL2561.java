package i2c;

import com.pi4j.io.i2c.I2CBus;
import com.pi4j.io.i2c.I2CDevice;
import com.pi4j.io.i2c.I2CFactory;
import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class TSL2561 {

    public final static int ADDRESS = 0x39;

    // A byte sent to the TSL256x with the most significant bit (MSB) equal to 1 will be interpreted as a COMMAND byte.
    public final static int COMMAND_BIT = 0x80;
    public final static int POWER_ON = 0x03;
    public final static int POWER_OFF = 0x00;

    //Ch DATA0LOW Low byte of ADC channel 0
    public final static int DATA0LOW = 0x0C;
    public final static int DATA0HIGH = 0x0D;

    //Eh DATA1LOW Low byte of ADC channel 1
    public final static int DATA1LOW = 0x0E;
    public final static int DATA1HIGH = 0x0F;

    private I2CDevice device;
    private I2CBus bus;

    boolean initialized = false;
    public final static int SCALE = 10;

    public double getLux() throws Exception {

        if (!initialized) {

            System.out.println("Device not initialized");
            return -1.0;
        }

        int broadband = getBroadband();
        int ir = getIR();

        int scale = 1 << SCALE;
        scale = scale << 4;

        int CH0 = (broadband * scale) >> SCALE;
        int CH1 = (ir * scale) >> SCALE;

        double ratio = (CH1 / (float) CH0);

        double lux = 0d;

        if ((ratio >= 0) && (ratio <= 0.52)) {
            lux = (0.0315 * CH0) - (0.0593 * CH0 * (Math.pow(ratio, 1.4)));
        } else if (ratio <= 0.65) {
            lux = (0.0229 * CH0) - (0.0291 * CH1);
        } else if (ratio <= 0.8) {
            lux = (0.0157 * CH0) - (0.018 * CH1);
        } else if (ratio <= 1.3) {
            lux = (0.00338 * CH0) - (0.00260 * CH1);
        } else if (ratio > 1.3) {
            lux = 0;
        }

        return lux;
    }

    private int getIR() throws IOException {

        int command = 0x8E;

        int reg = command | DATA1LOW;
        int lo = device.read(reg);

        command = 0x8F;

        reg = command | DATA1HIGH;

        int hi = device.read(reg);
        int ambient = (hi << 8) + lo;

        return ambient;

    }

    private int getBroadband() throws IOException {

        int command = 0x8C;
        int reg = command | DATA0LOW;

        int lo = device.read(reg);

        command = 0x8D;

        reg = command | DATA0HIGH;

        int hi = device.read(reg);

        int broadband = (hi << 8) + lo;

        return broadband;

    }

    public boolean initialize() {

        try {
            bus = I2CFactory.getInstance(I2CBus.BUS_1); // Depends on the RasPI version
            device = bus.getDevice(ADDRESS);
            device.write(COMMAND_BIT, (byte) POWER_ON);
            initialized = true;
        } catch (Exception e) {
            System.out.println(e);
            e.printStackTrace();
        }
        return false;

    }

    public void shutdown() {

        try {
            device.write(COMMAND_BIT, (byte) POWER_OFF);
        } catch (IOException e) {
            System.out.println(e);
            e.printStackTrace();
        }

    }

}
