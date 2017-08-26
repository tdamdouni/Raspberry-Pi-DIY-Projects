package Main;

import analog.MCP3008;
import i2c.HTU21DF;
import i2c.MPL3115A2;
import i2c.TSL2561;
import java.text.DecimalFormat;
import utils.AWSUtils;
import utils.PropertyFileReader;

public class Main {

    public static void main(String[] args) {

        // Sensors objects and initialization
        HTU21DF htu21df = new HTU21DF();
        htu21df.initialize();

        MPL3115A2 mpl3115a2 = new MPL3115A2();
        mpl3115a2.initialize();

        TSL2561 tsl2561 = new TSL2561();
        tsl2561.initialize();

        MCP3008 mcp3008 = new MCP3008();
        mcp3008.initialize();

        AWSUtils utils = new AWSUtils();

        DecimalFormat formater = new DecimalFormat(".##");

        PropertyFileReader reader = new PropertyFileReader("device.properties");
        int measurementInterval = Integer.parseInt(reader.getPropertyValue(reader.MEASUREMENT_INTERVAL));

        try {

            while (true) {

                // Reading Temperature (celsius) and Humidity  from htu21df
                double temperature = htu21df.getTemperature();
                String temperatureStr = formater.format(temperature);
                System.out.println("Temperature: " + temperatureStr + " C");

                double humidity = htu21df.getHumidity();
                String humidityStr = formater.format(humidity);
                System.out.println("Humidity: " + humidityStr + " %");

                // Reading pressure (hecto pascals hPa) from  mpl3115a2
                double pressure = mpl3115a2.getPressure();
                String presStr = formater.format(pressure);
                System.out.println("Pressure: " + presStr + " hPa");

                // Reading Luminosity (Lux) from TLS2561
                double lux = tsl2561.getLux();
                String luxStr = formater.format(lux);
                System.out.println("Luminosity: " + luxStr + " lx");

                // Reading Sound Pressure Level decibels (dBA) from MCP3008
                double spl = mcp3008.readSPL(0);
                String splStr = formater.format(spl);
                System.out.println("SPL: " + splStr + " dBA");

                // Send data to AWS
                utils.sendDataToAWS(temperature, humidity, pressure, humidity, spl);

                //Wait for next measurement 
                Thread.sleep(measurementInterval);

            }

        } catch (Exception e) {

            System.out.println(e.getMessage());
            e.printStackTrace();

        }

    }

}
