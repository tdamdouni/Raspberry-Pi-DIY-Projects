# http://forums.pimoroni.com/t/display-temperature-in-colours-on-unicorn-phat/4317/3

dateString = "%A %b %-d %-I:%M %p"
msg = "It is %s" % (datetime.datetime.now().strftime(dateString))
sense.show_message(msg, scroll_speed=s, text_colour=(w, 255, 255))

t = sense.get_temperature()
t = round(t)
      
if t <= 0: 
    tc = [0, 0, 255]  # blue
elif t > 0 and t < 13:
    tc = [255, 255, 0]  # yellow
elif t >= 13 and t <= 27:
    tc = [0, 255, 0]  # green
elif t > 27:
    tc = [255, 0, 0]  # red                 
msg = "and %sc" % (t)
sense.show_message(msg, scroll_speed=s, text_colour=tc)