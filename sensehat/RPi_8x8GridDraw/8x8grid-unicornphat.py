''' 8x4grid-unicornphat.py
Animation and single frame creation append
for Pimoroni UnicornPHat 8x8 LED matrix'''
import pygame
import sys
import math
from pygame.locals import *
from led import LED
from buttons import Button
import png # pypng
import unicornhat as uh
import copy, time
uh.set_layout(uh.PHAT)
saved = True
warning = False
pygame.display.init()
pygame.font.init()

screen = pygame.display.set_mode((530, 395), 0, 32)
pygame.display.set_caption('UnicornPHAT Grid editor')
pygame.mouse.set_visible(1)

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 51, 25))
colour = (255,0,0) # Set default colour to red
rotation = 0
#uh.rotation(rotation)
frame_number  = 1
fps = 4



def setColourRed():
    global colour
    colour = (255,0,0)

def setColourBlue():
    global colour
    colour = (0,0,255)

def setColourGreen():
    global colour
    colour = (0,255,0)

def setColourPurple():
    global colour
    colour = (102,0,204)

def setColourPink():
    global colour
    colour = (255,0,255)

def setColourYellow():
    global colour
    colour = (255,255,0)

def setColourOrange():
    global colour
    colour = (255,128,0)

def setColourWhite():
    global colour
    colour = (255,255,255)

def setColourCyan():
    global colour
    colour = (0,255,255)

def clearGrid(): # Clears the pygame LED grid and sets all the leds.lit back to False

    for led in leds:
        led.lit = False

def buildGrid(): # Takes a grid and builds versions for exporting (png and text)

    e = [0,0,0]
    e_png = (0,0,0)

    grid = [
    [e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e],
    [e,e,e,e,e,e,e,e],
    ]
    #png_grid =[]
    #print(grid)

    png_grid = ['blank','blank','blank','blank','blank','blank','blank','blank']
#   png_grid = ['blank','blank','blank','blank']
    for led in leds:
        if led.lit:
            grid[led.pos[1]][led.pos[0]] = [led.color[0], led.color[1], led.color[2]]
            grid[led.pos[1]+4][led.pos[0]] = [led.color[0], led.color[1], led.color[2]]
            if png_grid[led.pos[0]] == 'blank':
                png_grid[led.pos[0]] = (led.color[0], led.color[1], led.color[2])
            else:
                png_grid[led.pos[0]] = png_grid[led.pos[0]] + (led.color[0], led.color[1], led.color[2])
        else:
            if png_grid[led.pos[0]] == 'blank':
                png_grid[led.pos[0]] = (0,0,0)
            else:
                png_grid[led.pos[0]] = png_grid[led.pos[0]] + (0,0,0)
    return (grid, png_grid)

def piLoad(): # Loads image onto  matrix
    uh.off()
    for led in leds:
        if led.lit:
            uh.set_pixel(led.pos[0], led.pos[1], led.color[0], led.color[1], led.color[2])

            #print str(led.pos[0])+ ' ' +str(led.pos[1]) + ' ' + str(led.color[1])
    uh.show()


def exportGrid(): # Writes png to file

    global saved
    grid, png_grid = buildGrid()
    FILE=open('image8x4.png','wb')
    w = png.Writer(4,8)
    w.write(FILE,png_grid)
    FILE.close()
    saved = True

def exportCons(): # Writes raw list to console

    grid, png_grid = buildGrid()
    print(grid)


def rotate(): #Rotates image on AstroPi LED matrix
    global rotation
    if rotation == 180:
        rotation = 0
    else:
        rotation = rotation + 180
    #ap.set_rotation(rotation)
    uh.rotation(rotation)
    play()

def handleClick():

    global saved
    global warning
    pos = pygame.mouse.get_pos()
    led = findLED(pos, leds)
    if led:
        #print('led ' + str(led.pos_y) + ' clicked')
        led.clicked(colour)
        saved = False
    for butt in buttons:
        if butt.rect.collidepoint(pos):
            butt.click()
            #print 'button clicked'
    if warning:
        for butt in buttons_warn:
            if butt.rect.collidepoint(pos):
                butt.click()


def findLED(clicked_pos, leds): # reads leds and checks if clicked position is in one of them

    x = clicked_pos[0]
    y = clicked_pos[1]
    for led in leds:
        if math.hypot(led.pos_x - x, led.pos_y - y) <= led.radius:
            return led
            #print 'hit led'
    return None


def drawEverything():

    global warning
    screen.blit(background, (0, 0))
    #draw the leds
    for led in leds:
        led.draw()
        #print(led.pos_x,led.pos_y)
    for button in buttons:
        button.draw(screen)
    font = pygame.font.Font(None,16)

    frame_text = 'Frame '
    text = font.render(frame_text,1,(255,255,255))
    screen.blit(text, (5,5))
    frame_num_text = str(frame_number)
    text = font.render(frame_num_text,1,(255,255,255))
    screen.blit(text, (18,18))
    fps_text = 'Frame rate= ' + str(fps) +' fps'
    text = font.render(fps_text,1,(255,255,255))
    screen.blit(text, (175,10)) # done
    font = pygame.font.Font(None,18)
    export_text = 'Animation' # done
    text = font.render(export_text,1,(255,255,255))
    screen.blit(text, (445,15))  # done
    export_text = 'Single Frame'
    text = font.render(export_text,1,(255,255,255))
    screen.blit(text, (435,120)) # done
    pygame.draw.circle(screen,colour,(390,345),20,0)
    #flip the screen
    if warning:
        for button in buttons_warn:
            button.draw(screen)
    pygame.display.flip()

def load_leds_to_animation():

    global frame_number
    global leds
    for saved_led in animation[frame_number]:
                if saved_led.lit:
                    for led in leds:
                        if led.pos == saved_led.pos:
                            led.color = saved_led.color
                            led.lit = True

def nextFrame():

    global frame_number
    global leds
    #print(frame_number)
    animation[frame_number] = copy.deepcopy(leds)
    #clearGrid()
    frame_number+=1
    if frame_number in animation:
        leds =[]
        for x in range(0, 8):
            for y in range(0, 4):
                led = LED(radius=20,pos=(x, y))
                #print(' x= ' + str(led.pos_x) + ' y= ' + str(led.pos_y))
                leds.append(led)
        load_leds_to_animation()



def prevFrame():

    global frame_number
    global leds
    #print(frame_number)
    animation[frame_number] = copy.deepcopy(leds)
    clearGrid()
    if frame_number != 1:
        frame_number-=1
    if frame_number in animation:
        leds =[]
        for x in range(0, 8):
            for y in range(0, 4):
                led = LED(radius=20,pos=(x, y))
                leds.append(led)
        load_leds_to_animation()

def delFrame():
    global frame_number
    #print('ani length is ' + str(len(animation)) + ' frame is ' + str(frame_number))
    if len(animation) > 1:
        animation[frame_number] = copy.deepcopy(leds)
        del animation[frame_number]
        prevFrame()
        for shuffle_frame in range(frame_number+1,len(animation)):
            animation[shuffle_frame] = animation[shuffle_frame+1]
        del animation[len(animation)]



def getLitLEDs():

    points = []
    for led in leds:
        if led.lit:
            points.append(led.pos)
    return points

# Main program body - set up leds and buttons

leds = []
for x in range(0, 8):
    for y in range(0, 4):
        led = LED(radius=20,pos=(x, y))
        leds.append(led)
buttons = []
buttons_warn = []
animation={}
#global frame_number

def play():

    global leds
    global frame_number
    animation[frame_number] = copy.deepcopy(leds)
    #print 'length of ani is ' + str(len(animation))
    for playframe in range(1,(len(animation)+1)):
        #print(playframe)
        leds =[]
        for x in range(0, 8):
            for y in range(0, 4):
                led = LED(radius=20,pos=(x, y))
                leds.append(led)
            for saved_led in animation[playframe]:
                if saved_led.lit:
                    for led in leds:
                        if led.pos == saved_led.pos:
                            led.color = saved_led.color
                            led.lit = True
        piLoad()
        time.sleep(1.0/fps)
    frame_number = len(animation)

def faster():
    global fps
    fps+=1

def slower():
    global fps
    if fps != 1:
        fps-=1

def exportAni():

    global saved
    FILE=open('animation8x4.py','w')
    FILE.write('import unicornhat as uh\n')
    FILE.write('uh.set_layout(uh.PHAT)\n')
    FILE.write('import time\n')
    FILE.write('FRAMES = [\n')
    global leds
    global frame_number
    animation[frame_number] = copy.deepcopy(leds)
    #print 'length of ani is ' + str(len(animation))
    for playframe in range(1,(len(animation)+1)):
        #print(playframe)
        leds =[]
        for x in range(0,8):
            for y in range(0,4):
                led = LED(radius=20,pos=(x, y))
                leds.append(led)
            for saved_led in animation[playframe]:
                if saved_led.lit:
                                        for led in leds:
                                            if led.pos == saved_led.pos:
                                                        led.color = saved_led.color
                                                        led.lit = True

        grid, png_grid = buildGrid()
        #grid = uh.get_pixels()

        FILE.write(str(grid))
        FILE.write(',\n')
    FILE.write(']\n')
    FILE.write('for x in FRAMES:\n')
    FILE.write('\t uh.set_pixels(x)\n')
    FILE.write('\t uh.show()\n')
    FILE.write('\t time.sleep('+ str(1.0/fps) + ')\n')
    FILE.close()
    saved = True

def prog_exit():
    print('exit clicked')
    global warning
    warning = False
    #clearGrid()
    pygame.quit()
    sys.exit(-1)

def save_it():
    print('save clicked')
    global warning
    exportAni()
    warning = False

def quit():
    global saved
    if saved == False:
        nosave_warn()
    else:
        prog_exit()

def importAni():
    global leds
    global frame_number
    with open('animation8x4.py') as ll:
        line_count = sum(1 for _ in ll)
    ll.close()

    #animation = {}
    frame_number = 1
    file = open('animation8x4.py')
    for r in range(4):
        file.readline()

    for frame  in range(line_count-9):
        buff = file.readline()

        load_frame = buff.split('], [')
        #print(load_frame)
        counter = 1
        uh_leds =[]
        for f in load_frame:

            if counter == 1:
                f = f[3:]
            elif counter == 64:
                f = f[:-5]
            elif counter%8 == 0 and counter != 64:
                f = f[:-1]
            elif (counter-1)%8 == 0:
                f = f[1:]

            y = int((counter-1)/8)
            x = int((counter-1)%8)
            #print(counter,x,y)


            led = LED(radius=20,pos=(x, y))
            #print(' x= ' + str(led.pos_x) + ' y= ' + str(led.pos_y))

            #print(f)
            if f == '0, 0, 0':
                led.lit = False

            else:
                led.lit = True
                f_colours = f.split(',')
                #print(f_colours)
                led.color = [int(f_colours[0]),int(f_colours[1]),int(f_colours[2])]
            uh_leds.append(led)

            counter+=1
        leds = []
        for pp in range(32):
                        leds.append(uh_leds[pp])

        animation[frame_number] = copy.deepcopy(leds)
        frame_number+=1
        counter+=1

    file.close()

    #drawEverything()

exportAniButton = Button('Export to py', action=exportAni,  pos=(425, 45), color=(153,0,0))  # done
buttons.append(exportAniButton)
importAniButton = Button('Import from file', action=importAni,  pos=(425, 80 ), color=(153,0,0)) # done
buttons.append(importAniButton)

exportConsButton = Button('Export to console', action=exportCons, pos=(425, 150), color=(160,160,160)) # done
buttons.append(exportConsButton)
exportPngButton = Button('Export to PNG', action=exportGrid, pos=(425, 185), color=(160,160,160)) # done
buttons.append(exportPngButton)

RotateButton = Button('Rotate LEDs', action=rotate,  pos=(425, 255), color=(205,255,255)) # done
buttons.append(RotateButton)
clearButton = Button('Clear Grid', action=clearGrid,  pos=(425, 220), color=(204,255,255))# done
buttons.append(clearButton)

quitButton = Button('Quit', action=quit,  pos=(425, 290), color=(96,96,96))
buttons.append(quitButton)

FasterButton = Button('+', action=faster, size=(40,30), pos=(270, 5), color=(184,138,0)) # done
buttons.append(FasterButton)
SlowerButton = Button('-', action=slower, size=(40,30), pos=(315, 5), color=(184,138,0))# done
buttons.append(SlowerButton)

PlayButton = Button('Play on LEDs', action=play,  pos=(425, 340), color=(184,138,0)) # done
buttons.append(PlayButton)

RedButton = Button('', action=setColourRed, size=(50,30), pos=(365, 10),hilight=(0, 200, 200),color=(255,0,0)) # done
buttons.append(RedButton)
OrangeButton = Button('', action=setColourOrange, size=(50,30), pos=(365, 45),hilight=(0, 200, 200),color=(255,128,0)) # done
buttons.append(OrangeButton)
YellowButton = Button('', action=setColourYellow, size=(50,30), pos=(365, 80),hilight=(0, 200, 200),color=(255,255,0)) # done
buttons.append(YellowButton)
GreenButton = Button('', action=setColourGreen, size=(50,30), pos=(365, 115),hilight=(0, 200, 200),color=(0,255,0)) # done
buttons.append(GreenButton)
CyanButton = Button('', action=setColourCyan, size=(50,30), pos=(365, 150),hilight=(0, 200, 200),color=(0,255,255)) # done
buttons.append(CyanButton)
BlueButton = Button('', action=setColourBlue, size=(50,30), pos=(365, 185),hilight=(0, 200, 200),color=(0,0,255)) # done
buttons.append(BlueButton)
PurpleButton = Button('', action=setColourPurple, size=(50,30), pos=(365, 220),hilight=(0, 200, 200),color=(102,0,204)) # done
buttons.append(PurpleButton)
PinkButton = Button('', action=setColourPink, size=(50,30), pos=(365, 255),hilight=(0, 200, 200),color=(255,0,255)) # done
buttons.append(PinkButton)
WhiteButton = Button('', action=setColourWhite, size=(50,30), pos=(365, 290),hilight=(0, 200, 200),color=(255,255,255)) # done
buttons.append(WhiteButton)

PrevFrameButton = Button('<-', action=prevFrame, size=(25,30), pos=(50, 5), color=(184,138,0)) # done
buttons.append(PrevFrameButton)
NextFrameButton = Button('->', action=nextFrame, size=(25,30), pos=(80, 5), color=(184,138,0)) # done
buttons.append(NextFrameButton)

DelFrame = Button('Delete', action=delFrame, size=(45,25), pos=(115, 7), color=(184,138,0)) # done
buttons.append(DelFrame)

saveButton = Button('Save', action=save_it, size=(60,50), pos=(150, 250),hilight=(200, 0, 0),color=(255,255,0)) # done
buttons_warn.append(saveButton)
QuitButton = Button('Quit', action=prog_exit, size=(60,50), pos=(260, 250),hilight=(200, 0, 0),color=(255,255,0)) # done
buttons_warn.append(QuitButton)


def nosave_warn():
    global warning
    warning = True
    font = pygame.font.Font(None,48)
    frame_text = 'Unsaved Frames '

    for d in range(5):
        text = font.render(frame_text,1,(255,0,0))
        screen.blit(text, (100,100))
        pygame.display.flip()
        time.sleep(0.1)
        text = font.render(frame_text,1,(0,255,0))
        screen.blit(text, (100,100))
        pygame.display.flip()
        time.sleep(0.1)
    drawEverything()
# Main prog loop


while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            if saved == False:
                nosave_warn()
            else:
                prog_exit()

        if event.type == MOUSEBUTTONDOWN:
            handleClick()

    #update the display
    drawEverything()
