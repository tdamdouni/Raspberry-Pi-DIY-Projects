_https://forums.pimoroni.com/t/sensehat-and-black-hat-hack3r/6046_

```python
t1 = sense.get_temperature_from_humidity ()
t2 = sense.get_temperature_from_pressure
t = (t1 -t2) /2
t_cpu = get_cpu_temp()
t_corr = t - ((t_cpu -t ) / 1.5)
t_corr = get_smooth(t-corr)
return t_corr
```
