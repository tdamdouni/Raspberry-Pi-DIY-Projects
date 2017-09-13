################# Thingspeak Config #################
# You MUST update with YOUR key
THINGSPEAKKEY = 'xxxxxxxxxxxxxxxx'
THINGSPEAKURL = 'https://api.thingspeak.com/update'

################# User Preferences ##################
# Relate to retroScreen PCB and BMP180 sensor
INTERVAL      = 1    # Delay between each reading (mins)
AUTOSHUTDOWN  = 1    # Set to 1 to shutdown on switch
LCDCONTRAST   = 50   # Contrast setting
LCDSTYLE      = 1    # Default display mode

################# Hardware Constants ################
# Relate to retroScreen PCB and BMP180 sensor
DEVICE        = 0x77 # Default device I2C address
SMBUSID       = 1    # Rev 2 Pi uses 1, Rev 1 uses 0
SWITCH1       = 22   # GPIO for switch #1
SWITCH2       = 27   # GPIO for switch #2
SWITCH3       = 17   # GPIO for switch #3
DC            = 23   # SPI configuration
RST           = 24   # SPI configuration
SPI_PORT      = 0    # SPI configuration
SPI_DEVICE    = 0    # SPI configuration

################# System Constants #################
# These are used by the script
# and should not be changed
MINTEMP = 9999
MAXTEMP = 0
MINPRES = 9999
MAXPRES = 0
DISP = 0
IP   = '0.0.0.0'
#####################################################