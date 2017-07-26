from sense_hat import SenseHat
import time
import random

sense = SenseHat()

try:
    with open("score","r") as scorefile:
        highscore = int(scorefile.read())
except IOError:
    highscore = 0

#set up the colours (white,green,red,empty)
w = [150,150,150]
g = [0,255,0]
r = [255,0,0]
bl = [0,0,0]

#create images for three different coloured arrows
arrow_img = [0,0,0,1,1,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0,1,0,1,0,0,1,1,0,0,1,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0,0,0,0,1,1,0,0,0]
button_img = [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,1,0,1,0,0,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0]
shake_img =_img = [0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0]
breath_img =_img = [0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,0,0,0,1,1,0]

def plot_image(pattern,fg,bg):
    image = []
    for pixel in pattern:
        if pixel == 0:
            image.append(bg)
        else:
            image.append(fg)
    sense.set_pixels(image)

def shake_check():
    x,y,z = sense.get_accelerometer_raw().values()
    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x>1.2 or y>1.2 or z>1.2:
        return True
    else:
        return False

def get_angle():
    x,y,z = sense.get_accelerometer_raw().values()
    x=round(x,0)
    y=round(y,0)
    if x == -1:
        angle = 180
    elif x == 1:
        angle = 0
    elif y == -1:
        angle = 90
    else:
        angle = 270
    return angle

def orient_message(msg):
    time.sleep(0.5)
    sense.set_rotation(get_angle())
    sense.show_message(msg,scroll_speed=0.04,text_colour=w)


pause = 3
arrow = 0
play = True


#Main game loop, player shakes to start and is prompted
while True:
    orient_message("Shake Me")

    while shake_check() == False:
        time.sleep(0.1)

    play = True
    score = 0
    lives = 3

    pause = 2.5
    while play == True:
        last_arrow = arrow
        while arrow == last_arrow:
          arrow = random.choice([0,90,180,270])

        sense.set_rotation(arrow)

        num = random.random()
        print("humidity = " +str(sense.get_humidity()))
        if num < 0.1:
            plot_image(shake_img,w,bl)
            time.sleep(pause)
            if shake_check():
                plot_image(shake_img,g,bl)
                score = score + 1
            else:
                plot_image(shake_img,r,bl)
                lives = lives -1
        elif num > 0.9 and sense.get_humidity()<60:
            hum = sense.get_humidity()
            print(hum)
            plot_image(breath_img,w,bl)
            time.sleep(pause)
            if sense.get_humidity() > hum + 4:
                plot_image(breath_img,g,bl)
                score = score + 1
            else:
                plot_image(breath_img,r,bl)
                lives = lives - 1
        else:
            plot_image(arrow_img,w,bl)
            time.sleep(pause)
            if  get_angle() == arrow:
                plot_image(arrow_img,g,bl)
                score = score + 1
            else:
                plot_image(arrow_img,r,bl)
                lives = lives - 1
        print(lives)
        if lives <= 0:
            play=False
        if random.random() > 0.2:
            pause = pause * 0.95
        time.sleep(0.5)

    msg = "Your Score = %s" % (score)
    orient_message(msg)
    if score>highscore:
        highscore=score
        with open("score","w") as scorefile:
            scorefile.write(str(highscore))

    msg = "Highscore = %s" % (highscore)
    orient_message(msg)
