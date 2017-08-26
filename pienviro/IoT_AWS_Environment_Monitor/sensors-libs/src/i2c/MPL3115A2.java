package i2c;

import com.pi4j.io.i2c.I2CBus;
import com.pi4j.io.i2c.I2CDevice;
import com.pi4j.io.i2c.I2CFactory;

public class MPL3115A2 {

    public static final int ADDRESS = 0x60;
    public static final int CTRL_REG1 = 0x26;
    public static final byte CTRL_REG1_RST = 0x04;

    //OST bit will initiate a measurement immediately
    public static final byte CTRL_REG1_OST = 0x02;

    private I2CDevice device = null;
    private I2CBus bus = null;

    public boolean initialize() {

        try {

            bus = I2CFactory.getInstance(I2CBus.BUS_1);
            device = bus.getDevice(ADDRESS);
            device.write(CTRL_REG1, CTRL_REG1_RST);

            return true;
        } catch (Exception e) {
            return false;
        }

    }

    public double getTemperature() throws Exception {

        device.write(CTRL_REG1, CTRL_REG1_OST);
        Thread.sleep(50);

        byte[] buf = new byte[6];
        device.read(buf, 0, 6);

        int temperature_int = buf[4] << 8;
        temperature_int |= buf[5] & 0xff;
        temperature_int >>= 4;

        double temperature = (double) (temperature_int) / (double) 16.0;

        return temperature;
    }

    public double getPressure() throws Exception {

        device.write(CTRL_REG1, CTRL_REG1_OST);
        Thread.sleep(50);

        byte[] buf = new byte[6];
        device.read(buf, 0, 6);

        int pressure_int = buf[1] << 8;
        pressure_int |= buf[2] & 0xff;
        pressure_int = pressure_int << 8;
        pressure_int |= buf[3] & 0xff;
        pressure_int >>= 4;

        double pressure = ((double) pressure_int) / ((double) 4.0);
        pressure /= 100; // convert from pascals to hectopascals

        return pressure;
    }

    public double getAltitude() throws Exception {

        device.write(CTRL_REG1, CTRL_REG1_OST);
        Thread.sleep(50);

        byte[] buf = new byte[6];
        device.read(buf, 0, 6);

      //  int altitude_int = buf[1] << 8;
        int altitude_int = buf[1] << 16;
        altitude_int |= ( buf[2] <<8 & 0xff00);
        //altitude_int = altitude_int << 8;
        altitude_int |= buf[3] & 0xff;
        altitude_int >>= 4;
        

        double altitude = ((double) altitude_int) / ((double) 16.0);

        return altitude;
    }

}
