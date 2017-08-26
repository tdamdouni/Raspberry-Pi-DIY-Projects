from PIL import Image, ImageDraw, ImageFont, ImageOps
from datetime import datetime

from io import BytesIO
from matplotlib import pyplot as plt
from math import floor, ceil

temperature_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 34)
text_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf', 20)
small_font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', 14)

def drawImage_forecast(forecast):
	"""Build image for default display. 
	The top left corner shows location.
	The top two-thirds of the display shows the current temperature and weather icon.
	The bottom third of the display switches between weather summary, and time and date.

	INPUTS
	--------
	forecast: 		forecast object 
					returned from forecastio.load_forecast()
	show_datetime:	bool
					determine whether to display datetime (True) or summary (False)

	RETURNS
	--------
	image:			PIL.Image
					image to be displayed on the eink screen
	"""
	# Prep data
	current_forecast = forecast.currently()
	summary = current_forecast.d['summary']
	icon = current_forecast.d['icon']
	temperature = current_forecast.d['apparentTemperature']
	now = datetime.today()
	# Set up image
	image = Image.new('1', (200, 96), 1)
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, image.width, image.height), fill=1, outline=1)
	# Draw temperature
	draw.text( (16, 20), "{temp}'C".format(temp=round(temperature, 1)), font=temperature_font)
	# Draw icon
	icon = Image.open('./icons/{}.bmp'.format(icon))
	draw.bitmap((image.width - icon.width, 4), icon, fill=0)

	# Draw either summary or date and time
	time_date = '{h:02d}:{m:02d} {date}'.format(h=now.hour, m=now.minute, date=now.strftime('%d %b'))
	x_pix = (200 - draw.textsize(time_date, font=text_font)[0])/2
	draw.text((x_pix, 72), time_date, fill=0, font=text_font)

	# Draw symbol is weather alert
	if forecast.alerts() == []:
		# Draw location
		draw.text( (0,0), "Cowes", font=small_font)
	else:
		# Draw location
		draw.text( (23,0), "Cowes", font=small_font)
		alert = Image.open('./icons/Alert.bmp')
		draw.bitmap( (0,0), alert, fill=0)

	return image

def drawImage_sunInfo(forecast):
	"""Build image for secondary display: sunrise and sunset information. 
	Dispays the sunrise and sunset time of the current day

	INPUTS
	--------
	forecast: 		forecast object 
					returned from forecastio.load_forecast()

	RETURNS
	--------
	image:			PIL.Image
					image to be displayed on the eink screen
	"""
	# Prep data
	today = forecast.daily().data[0]
	sunrise = today.sunriseTime
	sunset = today.sunsetTime
	# Set up image
	image = Image.new('1', (200, 96), 1)
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, image.width, image.height), fill=1, outline=1)
	# Draw data
	sunrise_icon = Image.open('./icons/sunrise.bmp')
	sunset_icon = Image.open('./icons/sunset.bmp')
	draw.bitmap((40,5), sunrise_icon, fill=0)
	draw.bitmap((40,54), sunset_icon, fill=0)
	draw.text( (100, 10), "{h:02d}:{m:02d}".format(h=sunrise.hour, m=sunrise.minute), font=text_font)
	draw.text( (100, 58), "{h:02d}:{m:02d}".format(h=sunset.hour, m=sunset.minute), font=text_font)
	
	return image

def drawImage_next2Days(forecast):
	"""Build image for secondary display: weather forecast for next 2 days. 
	Displays the weather forecast (icon, max temperature and min temperature) for the next 2 days.

	INPUTS
	--------
	forecast: 		forecast object 
					returned from forecastio.load_forecast()

	RETURNS
	--------
	image:			PIL.Image
					image to be displayed on the eink screen
	"""
	days = forecast.daily()

	# Set up image
	image = Image.new('1', (200, 96), 1)
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, image.width, image.height), fill=1, outline=1)
	draw.line((100,0)+(100,96), fill=0)
	# Prep data for next day
	tomorrow = days.data[1]
	tmrw_icon = Image.open('./icons/{}.bmp'.format(tomorrow.d['icon']))
	tmrw_max_temp = str(round(tomorrow.d['apparentTemperatureMax'], 1)) + "'C"
	tmrw_min_temp = str(round(tomorrow.d['apparentTemperatureMin'], 1)) + "'C"
	# Draw data
	draw.bitmap((18,0), tmrw_icon, fill=0)
	x = int((100 - draw.textsize(tmrw_max_temp, font=small_font)[0])/2)
	draw.text( (x,55), tmrw_max_temp, font=small_font)
	x = int((100 - draw.textsize(tmrw_min_temp, font=small_font)[0])/2)
	draw.text( (x,66), tmrw_min_temp, font=small_font)
	x = int((100 - draw.textsize("Tomorrow", font=small_font)[0])/2)
	draw.text( (x,82), "Tomorrow", font=small_font)
	# Prep data for next day + 1
	day_2 = days.data[2]
	day_2_name = datetime.fromtimestamp(day_2.d['time']).strftime('%A')
	day_2_icon = Image.open('./icons/{}.bmp'.format(day_2.d['icon']))
	day_2_max_temp = str(round(day_2.d['apparentTemperatureMax'], 1)) + "'C"
	day_2_min_temp = str(round(day_2.d['apparentTemperatureMin'], 1)) + "'C"
	# Draw data
	draw.bitmap((118,0), tmrw_icon, fill=0)
	x = int((100 - draw.textsize(day_2_max_temp, font=small_font)[0])/2)
	draw.text( (100+x,55), day_2_max_temp, font=small_font)
	x = int((100 - draw.textsize(day_2_min_temp, font=small_font)[0])/2)
	draw.text( (100+x,66), day_2_min_temp, font=small_font)
	x = int((100 - draw.textsize(day_2_name, font=small_font)[0])/2)
	draw.text( (100+x,82), day_2_name, font=small_font)	

	return image

def drawImage_tempGraph(forecast):
	"""Build image for secondary display: graph showing temperature change for next 24 hours. 
	
	INPUTS
	--------
	forecast: 		forecast object 
					returned from forecastio.load_forecast()

	RETURNS
	--------
	image:			PIL.Image
					image to be displayed on the eink screen
	"""
	hourly = forecast.hourly()

	tempData = []
	for hour in hourly.data[:24]:
		tempData.append(hour.d['apparentTemperature'])

	fig,ax = plt.subplots(figsize=(2.3, 1), dpi=100)
	ax.plot(tempData, lw=2, color='k')
	ax.plot([0,24], [0,0], 'k--')
	ax.set_ylim([floor(min(tempData)), ceil(max(tempData))])
	ax.set_yticks([floor(min(tempData)), ceil(max(tempData))])
	ax.set_yticklabels([])
	ax.set_xticks([0,6,12,18,24])
	ax.set_xticklabels([])
	ax.spines['top'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.spines['bottom'].set_linewidth(1.25)
	ax.spines['left'].set_linewidth(1.25)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	# Save graph to open with PIL
	buffer_ = BytesIO()
	fig.savefig(buffer_, format='png')

	buffer_.seek(0)

	# Set up image
	image = Image.new('1', (200, 96), 1)
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, image.width, image.height), fill=1, outline=1)
	# Draw graph
	graph = ImageOps.invert(Image.open(buffer_).convert('L'))
	draw.bitmap((-8,2), graph, fill=0)
	x = draw.textsize(str(int(ceil(max(tempData)))), font=small_font)[0]
	draw.text((17-x,5), str(int(ceil(max(tempData)))), font=small_font)
	x = draw.textsize(str(int(floor(min(tempData)))), font=small_font)[0]
	draw.text((17-x,80), str(int(floor(min(tempData)))), font=small_font)
	draw.text((36,0), "Temp ('C) 24 hrs", font=small_font)

	return image

def drawImage_weatherAlert(forecast):
	"""Build image for secondary display: Information about weather alerts. 
	
	INPUTS
	--------
	forecast: 		forecast object 
					returned from forecastio.load_forecast()

	RETURNS
	--------
	image:			PIL.Image
					image to be displayed on the eink screen
	"""
	alert = forecast.alerts()

	# Set up image
	image = Image.new('1', (200, 96), 1)
	draw = ImageDraw.Draw(image)
	draw.rectangle((0, 0, image.width, image.height), fill=1, outline=1)
	
	if alert == []:
		# No weather alert
		draw.text((50, 5), "Alert", font=temperature_font)
		# No alerts
		draw.text((34, 50), "No warnings", font=text_font)
	else:
		# Weather alert
		draw.text((50, 5), "Alert", font=temperature_font)
		# Alert title
		x = int((200 - draw.textsize(alert[0].json['title'].split(" for ")[0], font=text_font)[0])/2)
		draw.text((x, 50), alert[0].json['title'].split(" for ")[0], font=text_font)
		# Alert expiry
		expiry_date = datetime.fromtimestamp(alert[0].json['expires']).strftime('%A %H:%m')
		x = int((200 - draw.textsize("Expires: {}".format(expiry_date), font=small_font)[0])/2)
		draw.text((x, 77), "Expires: {}".format(expiry_date), font=small_font)

	return image
