from time import sleep
#from sense_hat import SenseHat
from sense_emu import SenseHat
sense = SenseHat()

y = 4
ball_position = [3, 3]
ball_velocity = [1, 1]

def draw_bat():
    sense.set_pixel(0, y, 255, 255, 255)
    sense.set_pixel(0, y+1, 255, 255, 255)
    sense.set_pixel(0, y-1, 255, 255, 255)
        
def move_up(event):
    global y
    if y > 1 and event.action=='pressed':
        y -= 1
    print(event)

def move_down(event):
    global y
    if y < 6 and event.action=='pressed':
        y += 1
    print(event)

def draw_ball():
    sense.set_pixel(ball_position[0], ball_position[1], 0, 0, 255)
    ball_position[0] += ball_velocity[0]
    ball_position[1] += ball_velocity[1]
    if ball_position[0] == 7:
        ball_velocity[0] = -ball_velocity[0]
    if ball_position[1] == 0 or ball_position[1] == 7:
        ball_velocity[1] = -ball_velocity[1]
    if ball_position[0] == 0:
        sense.show_message("You Lose", text_colour=(255, 0, 0))
        quit()
    if ball_position[0] == 1 and y - 1 <= ball_position[1] <= y+1:
        ball_velocity[0] = -ball_velocity[0]
        
sense.stick.direction_up = move_up
sense.stick.direction_down = move_down

while True:
    sense.clear(0, 0, 0)
    draw_bat()
    draw_ball()
    sleep(0.25)
