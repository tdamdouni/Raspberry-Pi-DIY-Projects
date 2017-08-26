## Writing the data to a CSV file

It would be useful if that data could be stored somewhere. A CSV (comma-separated values) file is ideal for this, as it can be used by applications like Excel and LibreOffice.

- You'll want to log the date and time while getting the CPU temperatures, so you'll need some extra libraries for this. Add this to your imports:

    ```python
    from time import sleep, strftime, time
    ```

    These extra methods let you pause your program (`sleep`), get today's date as a string (`strftime`), and get the exact time in what's known as [UNIX time](https://en.wikipedia.org/wiki/Unix_time) (`time`).

- To write to a file, you first need to create it. At the end of your file, add the following line:

    ```python
    with open("cpu_temp.csv", "a") as log:
    ```

    This creates a new file called `cpu_temp.csv` and opens it with the name `log`. It also opens it in **append** mode, so that lines are only written to the end of the file.

- Now, you'll need to start an infinite loop that will run until you kill the program with **Ctrl + C**:

    ```python
    with open("cpu_temp.csv", "a") as log:
        while True:
    ```

- Inside the loop, you can get the temperature and store it as a variable.

    ```python
    with open("cpu_temp.csv", "a") as log:
        while True:
            temp = cpu.temperature
    ```

- Now you want to write both the current date and time, plus the temperature, to the CSV file:

    ```python
    with open("cpu_temp.csv", "a") as log:
        while True:
            temp = cpu.temperature
            log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
    ```

- That line's a little complicated, so let's break it down a bit:

  - `log.write()` will write whatever string is in the brackets to the CSV file.
  - `"{0},{1}\n"` is a string containing two placeholders separated by a comma, and ending in a new line.
  - `strftime("%Y-%m-%d %H:%M:%S")` is inserted into the first placeholder. It's the current date and time as a string.
  - `str(temp)` is the CPU temperature converted to a string, which is written into the second placeholder after the comma.

- Lastly, you can add a single line to the end of your file to pause the script between writes. Here it's pausing for one second, but you can use any interval that you want:

    ```python
    sleep(1)
    ```

- The entire script should now look like this:

    ```python
	from gpiozero import CPUTemperature
    from time import sleep, strftime, time

    with open("cpu_temp.csv", "a") as log:
        while True:
            temp = cpu.temperature
            log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))
            sleep(1)
    ```

