# BME680 Air Quality low?

_Captured: 2017-11-15 at 14:00 from [forums.pimoroni.com](https://forums.pimoroni.com/t/bme680-air-quality-low/6293/10)_

_Fair warning! This is a long and somewhat rambling post, but it's to try to illustrate the complexity of this whole thing…_

The volatiles detected by the BME680 encompass a wide range of different compounds, everything from solvents to carbon monoxide. The trouble is that you can't be much more specific than that, i.e. it's not tuned, or not possible to tune it, to any one of these volatiles, so what you're detecting is the overall mix. Fortunately, most of what we deem to be "air pollution" will fall under the umbrella of volatile organic compounds.

The gas resistance readings can be very simply interpreted as higher resistance = higher air quality and lower resistance = lower air quality. The problem then becomes how to translate that into something more meaningful. Here's a bit of an aside about some of the issues we should bear in mind…

**In a perfect situation, how would we work out the 100% air quality point?**

There's a few options:

The first would be to have a completely bare room, lined with material that gives off no VOCs, like stainless steel, with absolutely nothing in it, and filled with pure air. Not a very realistic or achievable scenario.

More realistic would be a "normal" room, painted, with some furniture, and fixtures and fittings in it. All of those things will release an amount of VOCs that would be comparable to a "normal" environment.

A "normal" room would probably have some people in it, right? So we need to factor that in too. Humans breath out VOCs, so their presence will affect the air quality.

There are also a bunch of other things to factor in, like boilers and gas hobs and ovens that will emit VOCs too. So you probably don't want to set your baseline in a room that contains any of those.

If you live next to a busy road, then pollutants from passing vehicles will negatively affect the air quality in adjacent rooms, and air quality may actually drop when you open the windows. In more rural spots, the air quality should increase when you open the windows, because lack of ventilation is known to result in significant drops in indoor air quality.

Humidity is also part of indoor air quality. It's thought that optimal indoor humidity is around 40%, and anything either side of that point negatively affects air quality.

In terms of the BME680 sensor itself, there will be some variation between sensors, so the baseline should be calculated and set for each sensor separately. The gas readings also take some time to settle once set running, and require some burn-in time (possibly up to 24 hours according to Adafruit, but we've found anecdotally that about 20 minutes should suffice).

**Suggestions for setting your baseline**

  1. A room that isn't your kitchen (or attached to your kitchen) and doesn't contain a boiler. Your bathroom probably isn't ideal either due to the abnormal humidity levels. Perhaps a bedroom or living room?

  2. At a time when there are a "normal" number of people in the room in which you're calibrating.

  3. In a well-ventilated room, but not at a time when there are a lot of cars passing any windows, e.g. at rush hours, if you live in a busy area. If you do live in a busy area, then it might be best to calibrate it with the windows closed!

  4. Not too close to any radiators or heat sources that will affect the humidity in the immediate vicinity.

**So how does my example work?**

It assumes that indoor air quality is comprised of **25% relative humidity**, and **75% gas resistance** reading. The humidity is clamped to a baseline of 40% relative humidity, i.e. 40% RH will add 25% to the overall score, and 0% RH would add 0% to the overall score and 100% RH would also add 0% to the overall score (in other words, it's scaled differently either side of the 40% RH baseline).

Because the gas resistance is a somewhat arbitrary scale, it's much harder to set the baseline. The approach that I took was to take 5 minutes of readings every second or so (assuming that there had been an at least 20 minute burn-in run the first time that the sensor was used) and assume that the first chunk of those 5 minutes worth of readings would be unreliable because it would still be stabilising. An average of the last 50 values taken (so the last minute or so of the 5 minutes) would be the 100% air quality baseline, i.e. adding 75% to the overall score. Let's say that the baseline is set at 50,000 Ohms, for the sake of argument. A reading of 0 Ohms would then add 0% to the overall score, a reading of 50,000 Ohms would add 75%, a reading of 25,000 Ohms would add 36.5%, and so on… Any readings higher than 50,000 would still score 75%.

**Problems with calculating indoor air quality**

The first, and biggest issue, is that it's a completely arbitrary thing. It's like converting indoor air temperature to a fixed scale from 0 to 100%, it doesn't make much sense, and is incredibly awkward to do. I mean, you could do something like saying that the optimal temperature is 21 degrees Celsius and it's never going to go lower than 15 degrees or higher than 30 degrees, but they're all assumptions.

No two people's homes are the same, no two rooms within anyone's home will be the same, and a particular room's air quality will vary at different times of the day, on different days, and depending on outside variables like weather, traffic, and so on.

How should the air quality score be comprised? The 25/75% score that I came up with was completely arbitrary and probably not correct. I suppose to more correctly set that balance you would have to come up with a measure of the relative effects of humidity and VOCs on human health.

**Ways in which my example could be improved**

The baseline should probably change through time. In other words, if readings higher than the baseline are found for a period of time, then shift the baseline up to that new level.

To account for short transient spikes, a moving average might be a better way to score the air quality, to smooth out those spikes, although you lose a small amount of precision doing this.

Perhaps a nice way to set the baseline would be to take 5 minutes worth of readings in each room in your home and then use the aggregate of those readings to better set the baseline?

**Other approaches**

As humans, I think we like to assign numbers and scores to things, even if they're things that don't make sense when numbers are attached. We're trying to turn something that is inherently qualitative into something quantitative.

The much easier, but perhaps less easy to interpret, way to do all of this is just to plot the raw resistance readings and humidity readings and then look at the trends and interpret falls and rises. For instance, you look at a day's worth of readings and see that there was a rise in gas resistance readings when you came home in the evening and opened the bedroom window, or there was a rise in humidity during the night when you were lying in bed sweating and breathing, and so on… Less easy to instantly interpret, but probably more informative.

Perhaps the ultimate approach is to do both, and then compare the indoor air quality score through time to the raw readings and events, and see how much sense they make…?

Sorry for the long and rambling nature of that! I hope some of it might be useful though?
