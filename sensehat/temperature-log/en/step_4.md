## Creating a Python script to monitor temperature

- Open a new Python 3 shell by going to **Menu** > **Programming** > **Python 3 (IDLE)**.

- Now create a new Python script by clicking on **File** > **New File**.

- You can use the GPIO Zero module to find the CPU temperature. First you'll need to import the `CPUTemperature` class:

	```python
	from gpiozero import CPUTemperature
	```
- Then you can create a `cpu` object:

	```python
	cpu = CPUTemperature()
	```
- Save and run this program (press **Ctrl + S** and then **F5**) and then swap over into the shell. Here, you can easily query the CPU temperature.

```python
>>> cpu.temperature
32.552
```


