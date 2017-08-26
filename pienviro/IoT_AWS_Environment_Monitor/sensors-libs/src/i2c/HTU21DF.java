package i2c;

import com.pi4j.io.i2c.I2CBus;
import com.pi4j.io.i2c.I2CDevice;
import com.pi4j.io.i2c.I2CFactory;
import java.io.IOException;

public class HTU21DF {

    // Device address
    private final static int ADDRESS = 0x40;

    // Commands
    private final static int TRIGGER_TEMPERATURE_MEASUREMENT = 0xF3;
    private final static int TRIGGER_HUMIDITY_MEASUREMENT = 0xF5;
    private final static int READ_USER_REGISTER = 0xE7;
    private final static int SOFT_RESET = 0xFE;

    private I2CBus bus;
    private I2CDevice device;
    private boolean initialized = false;

    public boolean initialize() {

        try {

            bus = I2CFactory.getInstance(I2CBus.BUS_1);
            device = bus.getDevice(ADDRESS);

            // soft reset device before use
            softReset();

            device.write((byte) READ_USER_REGISTER);
            int response = device.read();

            // device should return true for correct initialization
            if (response != 2) {
                throw new Exception("Incorrect reponse from device");
            }

            initialized = true;
            return true;

        } catch (Exception e) {

            return false;
        }

    }

    public double getTemperature() throws IOException, InterruptedException {

        double temperature = -1;

        if (!initialized) {

            return temperature;

        }

        device.write((byte) TRIGGER_TEMPERATURE_MEASUREMENT);
        Thread.sleep(50);

        byte[] buffer = new byte[3];

        device.read(buffer, 0, 3);

        int msb = buffer[0] & 0xFF;
        int lsb = buffer[1] & 0xFF;
        //int crc = buffer[2] & 0xFF; //crc is not used

        int temp_int = ((msb << 8) + lsb) & 0xFFFC;
        temp_int = msb << 8;
        temp_int |= lsb;

        temperature = (double) temp_int;
        temperature *= 175.72;
        temperature /= 65536;
        temperature -= 46.85;

        return temperature;
    }

    public double getHumidity() throws IOException, InterruptedException {

        double humidity = -1;

        if (!initialized) {

            return humidity;

        }

        device.write((byte) TRIGGER_HUMIDITY_MEASUREMENT);
        Thread.sleep(50);

        byte[] buffer = new byte[3];

        device.read(buffer, 0, 3);

        int msb = buffer[0] & 0xFF;
        int lsb = buffer[1] & 0xFF;
        //int crc = buffer[2] & 0xFF; //crc is not used

        int hum_int = ((msb << 8) + lsb) & 0xFFFC;
        hum_int = msb << 8;
        hum_int |= lsb;

        humidity = (double) hum_int;
        humidity *= 125;
        humidity /= 65536;
        humidity -= 6;

        return humidity;
    }

    public void softReset() throws IOException, InterruptedException {

        device.write((byte) SOFT_RESET);

        // The soft reset takes less than 15ms
        Thread.sleep(15);

    }

}
