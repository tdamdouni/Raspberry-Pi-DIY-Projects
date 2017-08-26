# Publishing weather data with Oracle

One of the big ideas with the weather station is to allow users to upload their data to a shared Oracle database. Schools data can then compare their data with other schools data and carry out comparison, test hypotheses and get a biiger picture of global weather.

## Register for an Remote database
1. You can register your Weather Station with a cloud based **Oracle** database so that your data can be used by other schools.

  [Oracle Apex Database](https://apex.oracle.com/pls/apex/f?p=84942:LOGIN_DESKTOP:9427101834476:&tz=0:00)
  
  You will need to complete a form whereupon you must wait for a Raspberry Pi admin to approve your school in the database. Once approved an activation email will be sent to you containing a verification code. Log in using your **school name** for the username and the password that you chose. You will then be prompted for the verification code from the email.
  
  Many weather stations can belong to one school. Once you have logged in you'll need to create a new weather station under your school. The *latitude* and *longitude* of the weather station will be required for this. Once you have created a weather station it will have its own password automatically generated, this is used by the weather station itself when it uploads the measurements to Oracle and is separate to your school login.
  
  *Note:* There is a known bug here where the *Add Weather Station* screen does not show a `Create` button, but only a `Return` button on the right. If you experience this just log out and back in and that should fix it.
  
## Update you local setup
1. Add the weather station name and password to the local Oracle credentials file. This allows the code that uploads to Oracle to know what credentials to use.

  `cd ~/weather-station`
  
  `nano credentials.oracle.template`
  
  Replace the `name` and `key` parameters with the `Weather Station Name` and `Passcode` of the weather station as specified in Oracle (under *Home > Weather Stations*). The double quotes `"` enclosing these values in this file are important so take care not to remove them by mistake.
  
  Press `Ctrl - O` then `Enter` to save and `Ctrl - X` to quit nano.
  
1. Rename the Oracle credentials template file to enable it.

  `mv credentials.oracle.template credentials.oracle`
  
## Checking that data is received
