#include <bme680.h>
#include <bme680.c>
#include <linux/i2c-dev.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int8_t user_i2c_read(uint8_t dev_id, uint8_t reg_addr, uint8_t *reg_data, uint16_t len)
{
    int8_t rslt = 0; /* Return 0 for Success, non-zero for failure */


    char *path = "/dev/i2c-1";

    int file = open(path, O_RDWR);

    ioctl(file, I2C_SLAVE, dev_id);

    rslt = i2c_smbus_read_i2c_block_data(file,
					  reg_addr, len, reg_data);

    close(file);
//    printf("Read %i bytes: %x from device %x from address %x with result: %i\n", len, *reg_data, dev_id,reg_addr, rslt);

    if (rslt >= 0) {return 0;} else {return -1;};
}

int8_t user_i2c_write(uint8_t dev_id, uint8_t reg_addr, uint8_t *reg_data, uint16_t len)
{

    char *path = "/dev/i2c-1";

    int file = open(path, O_RDWR);

    ioctl(file, I2C_SLAVE, dev_id);

    int8_t rslt = 0; /* Return 0 for Success, non-zero for failure */

    rslt = i2c_smbus_write_i2c_block_data(file,
                                          reg_addr, len, reg_data);
    close(file);
    if (rslt >= 0) {return 0;} else {return -1;};
}

void user_delay_ms(unsigned ms) {
    sleep(ms/1000);
}


int main() {
        struct bme680_dev gas_sensor;

	gas_sensor.dev_id = BME680_I2C_ADDR_PRIMARY;
	gas_sensor.intf = BME680_I2C_INTF;
	gas_sensor.read = user_i2c_read;
	gas_sensor.write = user_i2c_write;
	gas_sensor.delay_ms = user_delay_ms;

	int8_t rslt = BME680_OK;

	rslt = bme680_init(&gas_sensor);

        int8_t set_required_settings;

	/* Set the temperature, pressure and humidity settings */
	gas_sensor.tph_sett.os_hum = BME680_OS_2X;
	gas_sensor.tph_sett.os_pres = BME680_OS_4X;
	gas_sensor.tph_sett.os_temp = BME680_OS_8X;
	gas_sensor.tph_sett.filter = BME680_FILTER_SIZE_3;

	/* Set the remaining gas sensor settings and link the heating profile */
	gas_sensor.gas_sett.run_gas = BME680_ENABLE_GAS_MEAS;
	/* Create a ramp heat waveform in 3 steps */
	gas_sensor.gas_sett.heatr_temp = 320; /* degree Celsius */
	gas_sensor.gas_sett.heatr_dur = 150; /* milliseconds */

	/* Select the power mode */
	/* Must be set before writing the sensor configuration */
	gas_sensor.power_mode = BME680_FORCED_MODE; 

	/* Set the required sensor settings needed */
	set_required_settings = BME680_OST_SEL | BME680_OSP_SEL | BME680_OSH_SEL | BME680_FILTER_SEL 
		| BME680_GAS_SENSOR_SEL;
		
	/* Set the desired sensor configuration */
	rslt = bme680_set_sensor_settings(set_required_settings,&gas_sensor);

	/* Set the power mode */
	rslt = bme680_set_sensor_mode(&gas_sensor);

	/* Get the total measurement duration so as to sleep or wait till the
	 * measurement is complete */
	uint16_t meas_period;
	bme680_get_profile_dur(&meas_period, &gas_sensor);
	user_delay_ms(meas_period); /* Delay till the measurement is ready */

        struct bme680_field_data data;
	
	while(1) 
	{
		rslt = bme680_set_sensor_mode(&gas_sensor);
                rslt = bme680_get_sensor_data(&data, &gas_sensor);
                if ( rslt == 0 ) {
			printf("result: %i, T: %.2f degC, P: %.2f hPa, H %.2f %%rH ", rslt, data.temperature / 100.0f,
				data.pressure / 100.0f, data.humidity / 1000.0f );
			/* Avoid using measurements from an unstable heating setup */
			if(data.status & BME680_GASM_VALID_MSK)
				printf(", G: %d ohms", data.gas_resistance);
			printf("\r\n");
		sleep(5);
		}
	}
}