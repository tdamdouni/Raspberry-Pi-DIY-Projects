package utils;

import java.io.FileInputStream;
import java.io.InputStream;
import java.util.Properties;

public class PropertyFileReader {

    // AWS IoT platform properties
    public final String KEY_PATH = "KEY_PATH";
    public final String CERT_PATH = "CERT_PATH";
    public final String CA_PATH = "CA_PATH";
    public final String CLIENT_ID = "CLIENT_ID";
    public final String REGION = "REGION";

    public final String MEASUREMENT_INTERVAL = "MEASUREMENT_INTERVAL";
    public final String AWS_SCRIPT = "AWS_SCRIPT";


    String propertyFile;

    public PropertyFileReader(String propertFile) {

        this.propertyFile = propertFile;

    }

    public String getPropertyValue(String propertyName) {

        String propertyValue;

        Properties prop = new Properties();
        InputStream input;

        try {

            input = new FileInputStream(propertyFile);

            prop.load(input);
            propertyValue = prop.getProperty(propertyName);

        } catch (Exception e) {

            return null;
        }

        return propertyValue;

    }
}
