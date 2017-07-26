# Sense HAT: first program

Open Python 3 using `Menu > Programming > Python 3`. This will cause a Python Shell window to appear. Select `File > New File`, and type in the following code:

```python
from sense_hat import SenseHat
sense = SenseHat()
sense.show_message("Hello my name is Tim Peake")
```

Select `File > Save` and choose a file name for your program, then select `Run > Run module`. Your message should then scroll across the LED matrix in white text.


<iframe src="https://trinket.io/embed/python/9a14c1319e" width="100%" height="600" frameborder="0" marginwidth="0" marginheight="0" allowfullscreen></iframe>


Why not try changing the message between the double quotation marks and running your code again?
