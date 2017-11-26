 /******************************
 * Copyright (C) 2017 by Tobias Wartzek  
 * @file	bme680_main.c
 * @date	07.10.2017
 * @version	1.0
 * @brief Interface to BME680 from Raspberry Pi
 * 
 * 
 * Read out temperature, pressure, humidity and gas sensor ohmic values 
 * via I²C and Raspberry Pi.
 * 
 * History
 * Version		Date		Detail
 * 1.0			07.10.2017 	Initial creation
 * 
 ******************************/



#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <linux/i2c-dev.h>
#include <fcntl.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include "bme680.h"

#define     DESTZONE    "TZ=Europe/Stockholm"       // Our destination time zone



// I2C Linux device handle
int g_i2cFid;

// open the Linux device
void i2cOpen()
{
	g_i2cFid = open("/dev/i2c-1", O_RDWR);
	if (g_i2cFid < 0) {
		perror("i2cOpen");
		exit(1);
	}
}

// close the Linux device
void i2cClose()
{
	close(g_i2cFid);
}

// set the I2C slave address for all subsequent I2C device transfers
void i2cSetAddress(int address)
{
	if (ioctl(g_i2cFid, I2C_SLAVE, address) < 0) {
		perror("i2cSetAddress");
		exit(1);
	}
}



void user_delay_ms(uint32_t period)
{

    sleep(period/1000);



}

int8_t user_i2c_read(uint8_t dev_id, uint8_t reg_addr, uint8_t *reg_data, uint16_t len)
{
    int8_t rslt = 0; /* Return 0 for Success, non-zero for failure */

    uint8_t reg[1];
	reg[0]=reg_addr;

 	if (write(g_i2cFid, reg, 1) != 1) {
		perror("user_i2c_read_reg");
		rslt = 1;
	}
	if (read(g_i2cFid, reg_data, len) != len) {
		perror("user_i2c_read_data");
		rslt = 1;
	}

    return rslt;
}

int8_t user_i2c_write(uint8_t dev_id, uint8_t reg_addr, uint8_t *reg_data, uint16_t len)
{
    int8_t rslt = 0; /* Return 0 for Success, non-zero for failure */


	uint8_t reg[16];
    reg[0]=reg_addr;
	
    for (int i=1; i<len+1; i++)
       reg[i] = reg_data[i-1];

    if (write(g_i2cFid, reg, len+1) != len+1) {
		perror("user_i2c_write");
		rslt = 1;
        exit(1);
	}

    return rslt;
}


void write2file(char *outputFile, struct tm tm, struct bme680_field_data data)
{
	// Write measurement to output file if specified.
	if(outputFile != NULL)
	{
		FILE *f = fopen(outputFile, "a");
		if (f == NULL)
		{
			printf("Error opening file!\n");
			//exit(1);
		}
		else
		{
			fprintf(f,"%d-%02d-%02d %02d:%02d:%02d ", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec);
			fprintf(f,"T: %.2f degC, P: %.2f hPa, H: %.2f %%rH", data.temperature / 100.0f,
					data.pressure / 100.0f, data.humidity / 1000.0f );
			fprintf(f,", G: %d Ohms", data.gas_resistance);
			fprintf(f,"\r\n");
			fclose(f);
		}
	
	}
}

int main(int argc, char *argv[] )
{
	// create lock file first
	FILE *f = fopen("~bme680i2c.lock", "w");
	if (f == NULL)
	{
		printf("Error opening file!\n");
		exit(1);
	}
	fprintf(f,"I2C locked by BME680 readout. \r\n");
	fclose(f);


	int delay = 3;
	int nMeas = 3;
	char *outputFile = NULL;

	// Input argument parser
	if( argc == 2 ) {
		delay = strtol(argv[1], NULL, 10);
	}
	else if( argc == 3 ) {
		delay = strtol(argv[1], NULL, 10);
		nMeas = strtol(argv[2], NULL, 10);
	}
	else if( argc == 4 ) {
		delay = strtol(argv[1], NULL, 10);
		nMeas = strtol(argv[2], NULL, 10);
		outputFile = argv[3]; 
	}
	else {
		
	}


	printf("**** BME680 start measurements  ****\n");

	time_t t = time(NULL);
    putenv(DESTZONE);               // Switch to destination time zone


    // open Linux I2C device
	i2cOpen();

	// set address of the BME680
	i2cSetAddress(BME680_I2C_ADDR_SECONDARY);

    // init device
	struct bme680_dev gas_sensor;

	gas_sensor.dev_id = BME680_I2C_ADDR_SECONDARY;
	gas_sensor.intf = BME680_I2C_INTF;
	gas_sensor.read = user_i2c_read;
	gas_sensor.write = user_i2c_write;
	gas_sensor.delay_ms = user_delay_ms;

	int8_t rslt = BME680_OK;
	rslt = bme680_init(&gas_sensor);

    uint8_t set_required_settings;

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
	user_delay_ms(meas_period + delay*1000); /* Delay till the measurement is ready */


    struct bme680_field_data data;

	struct tm tm = *localtime(&t);
	
	int i=0;
	int backupCounter = 0;

	while(i<nMeas && backupCounter < nMeas+5) {

		// Get sensor data
		rslt = bme680_get_sensor_data(&data, &gas_sensor);
		
		// Avoid using measurements from an unstable heating setup 
		if(data.status & BME680_HEAT_STAB_MSK)
		{
			t = time(NULL);
			tm = *localtime(&t);
			printf("%d-%02d-%02d %02d:%02d:%02d ", tm.tm_year + 1900, tm.tm_mon + 1, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec);
			printf("T: %.2f degC, P: %.2f hPa, H: %.2f %%rH", data.temperature / 100.0f,
					data.pressure / 100.0f, data.humidity / 1000.0f );
			printf(", G: %d Ohms", data.gas_resistance);
			printf("\r\n");
			write2file(outputFile, tm, data);
			i++;
		}

		// Trigger a meausurement
		rslt = bme680_set_sensor_mode(&gas_sensor); /* Trigger a measurement */

		// Wait for a measurement to complete
		user_delay_ms(meas_period + delay*1000); /* Wait for the measurement to complete */			

		backupCounter++;
	}


	printf("**** Measurement finished ****\n");



    // close Linux I2C device
	i2cClose();
	
	// delete lock file
	remove("~bme680i2c.lock");
	
	return 0;
}

