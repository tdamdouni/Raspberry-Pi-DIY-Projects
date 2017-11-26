import RPi.GPIO as GPIO
import time, sys, pygame

# Pin definitions
trigger_pin_left = 8
echo_pin_left = 7
trigger_pin_right = 18
echo_pin_right = 23

#Colour definitions
green = (0,255,0)
orange = (255,255,0)
red = (255,0,0)
white = (255,255,255)
black = (0, 0, 0)

#Initialise the GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger_pin_left, GPIO.OUT)
GPIO.setup(echo_pin_left, GPIO.IN)
GPIO.setup(trigger_pin_right, GPIO.OUT)
GPIO.setup(echo_pin_right, GPIO.IN)

# These three functions encapsulate SR-04 range finder use
# Send a trigger pulse, using the pin supplied as a parameter
# The pulse has a duration of 100 microseconds
def send_trigger_pulse(pin):
    GPIO.output(pin, True)
    time.sleep(0.0001)
    GPIO.output(pin, False)

# Wait for the echo pin (supplied as the first parameter) to
# change to high or low as specified in the value parameter
# The timeout parameter prevents the function from hanging, if
# for any reason this doesn't happen
def wait_for_echo(pin, value, timeout):
    count = timeout
    while GPIO.input(pin) != value and count > 0:
        count -= 1


# Measure the distance in cm, using a rangefinder attached
# to the two pins specified as parameters.
def get_distance(trigger_pin, echo_pin):
    send_trigger_pulse(trigger_pin)
    # Wait for the echo pin to become True indicating that
    # the pulse of ultrasound has finished sending.
    wait_for_echo(echo_pin, True, 10000)
    # make a note of the time
    start = time.time()
    # Wait for the echo to become False indicating that an
    # obstacle has been detected
    wait_for_echo(echo_pin, False, 10000)
    # See how long it took
    finish = time.time()
    pulse_len = finish - start
    # Calculate the dsatnce using the speed of sound
    distance_cm = pulse_len / 0.000058
    return (int(distance_cm))
    
    
# Chose a colour for the distance supplied as a parameter 
# - red for close, green for far away, orange for in the middle    
def colour_for_distance(distance):
    if distance < 30:
        return red
    if distance < 100:
        return orange
    else:
        return green
    
# Initialise PyGame window    
pygame.init()
# Specify the Window size
# change this to change window size
size = width, height = 800, 600 
offset = width / 8

# Create the screen and a font for the text
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont("monospace", 50)


while True:
    # Check for window close
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            GPIO.cleanup() # set GPIO pins to be inputs
            sys.exit() # quit the program entirely
            
    # Measure the distances from both rangefinders   
    left_distance = get_distance(trigger_pin_left, echo_pin_left)
    right_distance = get_distance(trigger_pin_right, echo_pin_right)
    
    # Display the rectangles
    screen.fill(white)
    pygame.draw.rect(screen, colour_for_distance(left_distance), (offset, 0, width / 4, left_distance*5))
    pygame.draw.rect(screen, colour_for_distance(right_distance), (width / 2 + offset, 0, width / 4, right_distance*5))
    
    # Display the labels
    left_label = myfont.render(str(left_distance)+" cm", 1, black)
    screen.blit(left_label, (offset + 10, height/2))
    right_label = myfont.render(str(right_distance)+" cm", 1, black)
    screen.blit(right_label, (width/2 + offset + 10, height/2))
    
    # Update the display and wait 1/10 second so that is doesn't refresh too fast
    # to read the numbers
    pygame.display.update()
    time.sleep(0.1)

