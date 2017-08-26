## Live-graphing the data

You can produce a graph of CPU temperatures which will update as the data is recorded. For this, you'll need the **matplotlib** library. The instructions for installing this are [here](https://github.com/raspberrypilearning/temperature-log/blob/master/software.md).

- First of all, import the matplotlib library where your other imports are:

    ```python
    import matplotlib.pyplot as plt
    ```

- The next three lines can go after your imports. They tell matplotlib that you'll be doing interactive plotting, and also create the two lists that will hold the data to be plotted:

    ```python
    plt.ion()
    x = []
    y = []
    ```

- The next lines all go into your `while True` loop, before the CSV is written, but after the `temp = get_temp()` line. Firstly, you add the current temperature to the end of the `y` list, and the time to the end of the `x` list:

    ```python
    y.append(temp)
    x.append(time())
    ```

- Next, the plot needs to be cleared, and then the points and lines calculated:

    ```python
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    ```

- Lastly, the plot can be drawn:

    ```python
    plt.draw()
    ```

- Run your program and you should see the graph being interactively drawn. Open up some programs, such as Minecraft or Mathematica, and watch the CPU temperature increase.

