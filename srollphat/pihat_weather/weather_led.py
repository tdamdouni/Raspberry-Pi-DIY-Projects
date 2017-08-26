import forecastio as f
import scrollphat as s
import time as t
from apikey import api_key

lat = 53.768983
lng = -2.764714

s.set_brightness(2)
s.set_rotate(True)
forecast = f.load_forecast(api_key, lat, lng, units='si')
current_forecast = forecast.currently()
start_time = t.time()

while True:
	try:
		temp =  str(int(round(current_forecast.d['apparentTemperature'])))
		temp_str = temp + '\'C '
		summary = current_forecast.d['summary'].upper()
		hour = t.strftime('%H')
		minute = t.strftime('%M')

		display_str = hour + ":" + minute + "  " + temp_str + summary

		# 'M' and 'W' take 6 spaces, rather than 4
		num_m = display_str.count('M')
		num_w = display_str.count('W')
		neg = display_str.count('-')
                # Each letter takes 4 LEDs to display (including trailing space)
                # -1 because the degree symbol only takes 2 LEDs
		# -1 because colon symbol only takes 2 LEDs
		# -2 for each space added to string
                # -11 because they are shown before we need to scroll
                # -1 because there's no trailing space after last letter
		scroll_len = len(display_str)*4 - 1 - 1 - 4 - 11 - 1 + 2*(num_m+num_w) - 1*neg

		s.clear()
		s.write_string(display_str)
		t.sleep(1)
		for i in range(scroll_len):
			t.sleep(0.08)
			s.scroll()
		t.sleep(0.5)

                # Update the weather forecast every 5 minutes
		if ((t.time() - start_time) > 5*60):
			try:
				forecast = f.load_forecast(api_key, lat, lng, units='si')
				current_forecast = forecast.currently()
			except:
				pass
			start_time = t.time()
			print(t.asctime()[11:-5], '\r')

	except KeyboardInterrupt:
		s.clear()
		break
