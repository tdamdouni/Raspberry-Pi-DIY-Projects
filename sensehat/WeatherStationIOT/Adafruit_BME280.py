# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Based on the BMP280 driver with BME280 changes provided by
# David J Taylor, Edinburgh (www.satsignal.eu)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import logging
import time


# BME280 default address.
BME280_I2CADDR = 0x77

# Operating Modes
BME280_OSAMPLE_1 = 1
BME280_OSAMPLE_2 = 2
BME280_OSAMPLE_4 = 3
BME280_OSAMPLE_8 = 4
BME280_OSAMPLE_16 = 5

# BME280 Registers

BME280_REGISTER_DIG_T1 = 0x88  # Trimming parameter registers
BME280_REGISTER_DIG_T2 = 0x8A
BME280_REGISTER_DIG_T3 = 0x8C

BME280_REGISTER_DIG_P1 = 0x8E
BME280_REGISTER_DIG_P2 = 0x90
BME280_REGISTER_DIG_P3 = 0x92
BME280_REGISTER_DIG_P4 = 0x94
BME280_REGISTER_DIG_P5 = 0x96
BME280_REGISTER_DIG_P6 = 0x98
BME280_REGISTER_DIG_P7 = 0x9A
BME280_REGISTER_DIG_P8 = 0x9C
BME280_REGISTER_DIG_P9 = 0x9E

BME280_REGISTER_DIG_H1 = 0xA1
BME280_REGISTER_DIG_H2 = 0xE1
BME280_REGISTER_DIG_H3 = 0xE3
BME280_REGISTER_DIG_H4 = 0xE4
BME280_REGISTER_DIG_H5 = 0xE5
BME280_REGISTER_DIG_H6 = 0xE6
BME280_REGISTER_DIG_H7 = 0xE7

BME280_REGISTER_CHIPID = 0xD0
BME280_REGISTER_VERSION = 0xD1
BME280_REGISTER_SOFTRESET = 0xE0

BME280_REGISTER_CONTROL_HUM = 0xF2
BME280_REGISTER_CONTROL = 0xF4
BME280_REGISTER_CONFIG = 0xF5
BME280_REGISTER_PRESSURE_DATA = 0xF7
BME280_REGISTER_TEMP_DATA = 0xFA
BME280_REGISTER_HUMIDITY_DATA = 0xFD


class BME280(object):
    def __init__(self, mode=BME280_OSAMPLE_1, address=BME280_I2CADDR, i2c=None,
                 **kwargs):
        self._logger = logging.getLogger('Adafruit_BMP.BMP085')
        # Check that mode is valid.
        if mode not in [BME280_OSAMPLE_1, BME280_OSAMPLE_2, BME280_OSAMPLE_4,
                        BME280_OSAMPLE_8, BME280_OSAMPLE_16]:
            raise ValueError(
                'Unexpected mode value {0}.  Set mode to one of BME280_ULTRALOWPOWER, BME280_STANDARD, BME280_HIGHRES, or BME280_ULTRAHIGHRES'.format(mode))
        self._mode = mode
        # Create I2C device.
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        self._device = i2c.get_i2c_device(address, **kwargs)
        # Load calibration values.
        self._load_calibration()
        self._device.write8(BME280_REGISTER_CONTROL, 0x3F)
        self.t_fine = 0.0

    def _load_calibration(self):

        self.dig_T1 = self._device.readU16LE(BME280_REGISTER_DIG_T1)
        self.dig_T2 = self._device.readS16LE(BME280_REGISTER_DIG_T2)
        self.dig_T3 = self._device.readS16LE(BME280_REGISTER_DIG_T3)

        self.dig_P1 = self._device.readU16LE(BME280_REGISTER_DIG_P1)
        self.dig_P2 = self._device.readS16LE(BME280_REGISTER_DIG_P2)
        self.dig_P3 = self._device.readS16LE(BME280_REGISTER_DIG_P3)
        self.dig_P4 = self._device.readS16LE(BME280_REGISTER_DIG_P4)
        self.dig_P5 = self._device.readS16LE(BME280_REGISTER_DIG_P5)
        self.dig_P6 = self._device.readS16LE(BME280_REGISTER_DIG_P6)
        self.dig_P7 = self._device.readS16LE(BME280_REGISTER_DIG_P7)
        self.dig_P8 = self._device.readS16LE(BME280_REGISTER_DIG_P8)
        self.dig_P9 = self._device.readS16LE(BME280_REGISTER_DIG_P9)

        self.dig_H1 = self._device.readU8(BME280_REGISTER_DIG_H1)
        self.dig_H2 = self._device.readS16LE(BME280_REGISTER_DIG_H2)
        self.dig_H3 = self._device.readU8(BME280_REGISTER_DIG_H3)
        self.dig_H6 = self._device.readS8(BME280_REGISTER_DIG_H7)

        h4 = self._device.readS8(BME280_REGISTER_DIG_H4)
        h4 = (h4 << 24) >> 20
        self.dig_H4 = h4 | (self._device.readU8(BME280_REGISTER_DIG_H5) & 0x0F)

        h5 = self._device.readS8(BME280_REGISTER_DIG_H6)
        h5 = (h5 << 24) >> 20
        self.dig_H5 = h5 | (
        self._device.readU8(BME280_REGISTER_DIG_H5) >> 4 & 0x0F)

        '''
        print '0xE4 = {0:2x}'.format (self._device.readU8 (BME280_REGISTER_DIG_H4))
        print '0xE5 = {0:2x}'.format (self._device.readU8 (BME280_REGISTER_DIG_H5))
        print '0xE6 = {0:2x}'.format (self._device.readU8 (BME280_REGISTER_DIG_H6))
        print 'dig_H1 = {0:d}'.format (self.dig_H1)
        print 'dig_H2 = {0:d}'.format (self.dig_H2)
        print 'dig_H3 = {0:d}'.format (self.dig_H3)
        print 'dig_H4 = {0:d}'.format (self.dig_H4)
        print 'dig_H5 = {0:d}'.format (self.dig_H5)
        print 'dig_H6 = {0:d}'.format (self.dig_H6)
        '''

    def read_raw_temp(self):
        """Reads the raw (uncompensated) temperature from the sensor."""
        meas = self._mode
        self._device.write8(BME280_REGISTER_CONTROL_HUM, meas)
        meas = self._mode << 5 | self._mode << 2 | 1
        self._device.write8(BME280_REGISTER_CONTROL, meas)
        sleep_time = 0.00125 + 0.0023 * (1 << self._mode)
        sleep_time = sleep_time + 0.0023 * (1 << self._mode) + 0.000575
        sleep_time = sleep_time + 0.0023 * (1 << self._mode) + 0.000575
        time.sleep(sleep_time)  # Wait the required time
        msb = self._device.readU8(BME280_REGISTER_TEMP_DATA)
        lsb = self._device.readU8(BME280_REGISTER_TEMP_DATA + 1)
        xlsb = self._device.readU8(BME280_REGISTER_TEMP_DATA + 2)
        raw = ((msb << 16) | (lsb << 8) | xlsb) >> 4
        return raw

    def read_raw_pressure(self):
        """Reads the raw (uncompensated) pressure level from the sensor."""
        """Assumes that the temperature has already been read """
        """i.e. that enough delay has been provided"""
        msb = self._device.readU8(BME280_REGISTER_PRESSURE_DATA)
        lsb = self._device.readU8(BME280_REGISTER_PRESSURE_DATA + 1)
        xlsb = self._device.readU8(BME280_REGISTER_PRESSURE_DATA + 2)
        raw = ((msb << 16) | (lsb << 8) | xlsb) >> 4
        return raw

    def read_raw_humidity(self):
        """Assumes that the temperature has already been read """
        """i.e. that enough delay has been provided"""
        msb = self._device.readU8(BME280_REGISTER_HUMIDITY_DATA)
        lsb = self._device.readU8(BME280_REGISTER_HUMIDITY_DATA + 1)
        raw = (msb << 8) | lsb
        return raw

    def read_temperature(self):
        """Gets the compensated temperature in degrees celsius."""
        # float in Python is double precision
        UT = float(self.read_raw_temp())
        var1 = (UT / 16384.0 - self.dig_T1 / 1024.0) * float(self.dig_T2)
        var2 = ((UT / 131072.0 - self.dig_T1 / 8192.0) * (
        UT / 131072.0 - self.dig_T1 / 8192.0)) * float(self.dig_T3)
        self.t_fine = int(var1 + var2)
        temp = (var1 + var2) / 5120.0
        return temp

    def read_pressure(self):
        """Gets the compensated pressure in Pascals."""
        adc = self.read_raw_pressure()
        var1 = self.t_fine / 2.0 - 64000.0
        var2 = var1 * var1 * self.dig_P6 / 32768.0
        var2 = var2 + var1 * self.dig_P5 * 2.0
        var2 = var2 / 4.0 + self.dig_P4 * 65536.0
        var1 = (
               self.dig_P3 * var1 * var1 / 524288.0 + self.dig_P2 * var1) / 524288.0
        var1 = (1.0 + var1 / 32768.0) * self.dig_P1
        if var1 == 0:
            return 0
        p = 1048576.0 - adc
        p = ((p - var2 / 4096.0) * 6250.0) / var1
        var1 = self.dig_P9 * p * p / 2147483648.0
        var2 = p * self.dig_P8 / 32768.0
        p = p + (var1 + var2 + self.dig_P7) / 16.0
        return p

    def read_humidity(self):
        adc = self.read_raw_humidity()
        # print 'Raw humidity = {0:d}'.format (adc)
        h = self.t_fine - 76800.0
        h = (adc - (self.dig_H4 * 64.0 + self.dig_H5 / 16384.8 * h)) * (
        self.dig_H2 / 65536.0 * (1.0 + self.dig_H6 / 67108864.0 * h * (
        1.0 + self.dig_H3 / 67108864.0 * h)))
        h = h * (1.0 - self.dig_H1 * h / 524288.0)
        if h > 100:
            h = 100
        elif h < 0:
            h = 0
        return h
