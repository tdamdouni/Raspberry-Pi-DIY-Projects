# Sense HAT Data Logger - Part 2

In the first part of this activity, you built a data logger that logs all data from the Sense HAT as often as it can and starts when your Raspberry Pi starts. If you follow this worksheet, you'll be able to extend your data logger to add some optional features such as:

  - Being able to select which data your program logs from the Sense-HAT
  - Adding the ability to log data at a fixed interval (every ten seconds for example)

## Choosing which pieces of data to log.
Sometimes you may not want to log data from every sensor on the Sense HAT depending on what you are investigating. To just capture some of the sensor data you need to make a few changes to your code. Firstly, you'll need to add some variables to our settings section so that you can specify which data to log. Then, your `file_setup` function will need to be adapted in order to add only the headers you want. Finally, you will have to adapt your `get_sense_data` function to only capture the required data.

1. For each piece of data you want to log you will need a **Boolean** (one that can either be **True** or **False**) variable to your settings section. In the code below, these have been capitalised to make them stand out. For now, they have been set to `True`.

  ```python3
  ## Logging Settings
  TEMP_H=True
  TEMP_P=False
  HUMIDITY=True
  PRESSURE=True
  ORIENTATION=True
  ACCELERATION=True
  MAG=True
  GYRO=True

  FILENAME = "Fall"
  WRITE_FREQUENCY = 1
  ```

1. You then need to update your `file_setup` function to only append the headings that are set to `True`

  ```python3
  def file_setup(filename):
      header =[]
      if TEMP_H:
          header.append("temp_h")
      if TEMP_P:
          header.append("temp_p")
      if HUMIDITY:
          header.append("humidity")
      if PRESSURE:
          header.append("pressure")
      if ORIENTATION:
          header.extend(["pitch","roll","yaw"])
      if MAG:
          header.extend(["mag_x","mag_y","mag_z"])
      if ACCELERATION:
          header.extend(["accel_x","accel_y","accel_z"])
      if GYRO:
          header.extend(["gyro_x","gyro_y","gyro_z"])
      header.append("timestamp")

      with open(filename,"w") as f:
          f.write(",".join(str(value) for value in header)+ "\n")
  ```

  In this new version of the function you start with an empty list for the header
    ```python3
    header =[]
    ```
  Then each setting is checked and if that setting is set to `True` then the related data is either appended (if it's a item).
    ```python3
    if TEMP_H:
        header.append("temp_h")
    ```
  Or extended if it involves multiple items of data.
    ```python3
    if ORIENTATION:
        header.extend(["pitch","roll","yaw"])
    ```

1. The final change to make is to the `get_sense_data` function, which is a similar change to the one made to the `file_setup` function. Your code which did look like this:

  ```python3
  def get_sense_data():
      sense_data=[]

      sense_data.append(sense.get_temperature_from_humidity())
      sense_data.append(sense.get_temperature_from_pressure())
      sense_data.append(sense.get_humidity())
      sense_data.append(sense.get_pressure())

      yaw,pitch,roll = sense.get_orientation().values()
      sense_data.extend([pitch,roll,yaw])

      mag_x,mag_y,mag_z = sense.get_compass_raw().values()
      sense_data.extend([mag_x,mag_y,mag_z])

      x,y,z = sense.get_accelerometer_raw().values()
      sense_data.extend([x,y,z])

      gyro_x,gyro_y,gyro_z = sense.get_gyroscope_raw().values()
      sense_data.extend([gyro_x,gyro_y,gyro_z])

      sense_data.append(datetime.now())

      return sense_data
    ```
  This will need to be adapted to have each piece of Sense HAT data wrapped in a `if` statement which will check whether the corresponding setting is set to `True`

    ```python3
    def get_sense_data():
        sense_data=[]

        if TEMP_H:
            sense_data.append(sense.get_temperature_from_humidity())

        if TEMP_P:
            sense_data.append(sense.get_temperature_from_pressure())

        if HUMIDITY:
            sense_data.append(sense.get_humidity())

        if PRESSURE:
            sense_data.append(sense.get_pressure())

        if ORIENTATION:
            yaw,pitch,roll = sense.get_orientation().values()
            sense_data.extend([pitch,roll,yaw])

        if MAG:
            mag_x,mag_y,mag_z = sense.get_compass_raw().values()
            sense_data.extend([mag_x,mag_y,mag_z])

        if ACCELERATION:
            x,y,z = sense.get_accelerometer_raw().values()
            sense_data.extend([x,y,z])

        if GYRO:
            gyro_x,gyro_y,gyro_z = sense.get_gyroscope_raw().values()
            sense_data.extend([gyro_x,gyro_y,gyro_z])

        sense_data.append(datetime.now())

        return sense_data
    ```

  You can find a complete code listing [here](code/Sense_Logger_v3.py).

  Now when you run your code you should be able to switch the collection of different pieces of data **on/off** by changing the settings at the top to **True/Flase**

## Logging data at a fixed interval

Currently the data logger you have written will collect data as fast as it can (multiple times a second). This is great for many situations, particularly when the environment is changing rapidly. However, you may sometimes want to collect data less frequently, when change is more gradual. To make this work, you will need to develop your code in a few ways.

  - Add some libraries to your code to enable extra functionality.
  - Set the interval between logging events
  - Write a function which will be run at the start of the program, before the loop, to log data and then wait for the specified interval.
  - Amend part of the code inside the `while` loop so that the loop skips logging there if an interval has been set.

1. The first step is to import the two library elements at the top of your code:
  - The **sleep** function from the **time** library allows you code to pause between lines of code.
  - A **Thread**, from the **threading** library allows a separate chunk of code to be run at the same time as another. We need one thread to continually check the sensors, and another to log the data every so many seconds.

  Your import section should now look like this:

    ```python3
    from datetime import datetime
    from sense_hat import SenseHat
    from time import sleep
    from threading import Thread
    ```

1. With these libraries imported you can now add a setting to your setting section which will set the DELAY between logging. If you set it to zero the program will behave as it has so far and log as often as possible. Anything higher than zero will use a separate `timed_log` function which you'll write in the set step.

  Add the line `DELAY=5` to you settings section for a five second delay, as shown below.

    ```python3
    ##### Logging Settings #####
    FILENAME = ""
    WRITE_FREQUENCY = 100
    TEMP_H=True
    TEMP_P=False
    HUMIDITY=True
    PRESSURE=True
    ORIENTATION=True
    ACCELERATION=True
    MAG=True
    GYRO=True
    DELAY=5
    ```

2. You'll now need to add a function for handling the `timed_log`, this will run in the background and call `log_data` every 5 seconds. Add the following definition to your `functions` section.

    ```python3
    def timed_log():
        while True:
          log_data()
          sleep(DELAY)
    ```

3. Now that your imports, settings, and functions have been added you'll now need to adjust your main program to include them.

  First add these two lines above the `while True:` line:

  ```python3
  if DELAY > 0:
      sense_data = get_sense_data()
      Thread(target= timed_log).start()
  ```

  This checks whether a delay has been set and, if so, starts a separate thread which launches the `timed_log` function in the background.

4. The final step is to adjust a line inside the `while True:` loop so that if a delay is set then the loop doesn't log any data and simply handles the writing out of data to the file. Find the line that says `log_data` and replace it with:

    ```python3
    if DELAY == 0:
      log_data()
    ```

  This only logs data inside the while loop if the value of DELAY is 0.

  With these changes made you should be able specify the delay between logging events and log data at whatever interval you want. You can see the full code [here](code/Sense_Logger_v4.py)

## Collect your data

Use your Python code to record data over a long period of time at an interval of your choice, such as:
- Measure the temperature, humidity and pressure of a room in your house every five minutes (i.e. every 300 seconds) over the period of a week.
- Monitoring conditions for plant growth inside a propagator or greenhouse: measure conditions which may impact on the health of the plants.

##What next
  - Use your data logging code to explore conditions on the ISS following our [Sensing Science](https://github.com/raspberrypilearning/sensing-space) activity.
