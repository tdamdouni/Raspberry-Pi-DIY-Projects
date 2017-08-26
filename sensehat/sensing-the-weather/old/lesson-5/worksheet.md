# Weather Station Basic I/O - Combining our code

In this lesson you will:

- Review the code for the anemometer and rain gauge programs and understand how they work.
- Create one single program to log data from the anemometer and the rain gauge.
- Use comments to annotate your final code, and explain its function.

## Reviewing your existing code

Look back at the code you wrote for the anemometer and the rain gauge and review how they worked. What did each line do? To open your code you should open LXTerminal, change to the `weather_station` directory and open your previous code:

```bash
nano wind_final.py
```

or

```bash
nano rain_interrupt.py
```

## Creating a single solution

Having two programs, one for each sensor, can be helpful. However, ideally we would want to run one program that monitored all our sensors. Your task this lesson is to combine your code together to create one program to perform both jobs. To get you started, here a few things to think about:

1. Are you going to start a new program and write the program from scratch using the original two as guides?

    ```bash
  nano wind_rain.py
  ```

1. Or are you going to copy one of the originals and add to that?

    ```bash
    cp wind_final.py wind_rain.py
    nano wind_rain.py
    ```

1. Are there any lines of code appearing in both programs that only need to appear once? For example, the import line is only needed once at the beginning of our program

    ```python
    import RPi.GPIO as GPIO,time
    ```

1. What variable names are you going to use? In each program so far you have used the variable `count` which won't work if you are counting rain and wind signals.

1. Both programs contain a loop of some kind to display the current readings, so these will need to be combined.

## Code commenting

We haven't used comments much in our work so far but we should. Comments allow you to annotate and explain what your code is doing. This is useful both for yourself and others reading your code. Adding a comment is quite straightforward. In the example below, the line beginning with a `#` has been used; this is ignored by the computer but readable by humans.

```python
# The spin function is called whenever a spin is detected, it increments the count variable and prints it out
def spin(channel):
    global count
    count = count + 1
```

## Test and review

Once you have completed your code you should test it carefully to ensure it functions correctly, reliably and accurately.

If you are happy with your code and how it functions, spend some time comparing your code with others and consider the following:

- Is your code exactly the same or are there multiple solutions?
- How clear is their code, and have they used comments to explain it?
- What improvements could they make to their code?
- What ideas might you take from their code to improve yours?

## What's next?

- Congratulations! You are now able to deploy a basic version of the weather station, which displays data on rainfall and wind speed. (An example solution can be found [here](code/wind_rain.py))
- Consider what's missing from this solution. Clearly only two of the sensors have been covered but what else is missing?
- Is this the best way to display the data?
- Is data being saved? Could I look back at previous data?
