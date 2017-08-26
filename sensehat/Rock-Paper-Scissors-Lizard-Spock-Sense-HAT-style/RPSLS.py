#PRODUCED BY TeCoEd (@dan_aldred)
#RPSLS
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import pygame
from pygame.locals import *
from sense_hat import SenseHat
import random
import time

global playersChoice
global count
global computer_choice
gameRunning = True

###Set up PyGame Screen###
pygame.init()
pygame.display.set_mode((140, 180))

###Prepare Sense Hat###
sense = SenseHat()
sense.load_image("0.png")
sense.low_light = True #save your eyes!

playersChoice = 0

'''Converts the Number into the choice i.e. lizard, spocks etc '''
def number_to_name(number):
    if number == 0:
        return "Rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "Paper"
    elif number == 3:
        return "Lizard"
    elif number == -1: ### because value is 5 so re-sets to 0, zero - 1 = -1 ###
        return "Scissors"
    elif number == 4: ### because value is 5 so re-sets to 0, zero - 1 = -1 ###
        return "Scissors" ### for the computer
           
def mainGame():
    ###PLAYER SELECTION###
    ###Loops while running variable is True###
    running = True
    global playersChoice
    global computer_choice
    while running == True:
        sense.set_rotation(90)
        for event in pygame.event.get():
            
            if event.type == KEYDOWN and playersChoice < 5:
                if event.key == K_UP:
                    print (playersChoice)
                    sense.load_image(str(playersChoice) + ".png")
                    playersChoice = playersChoice + 1
            if playersChoice == 5:
                playersChoice = 0     
            
            '''Checks for a 'select / Enter' Choice ''' 
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    running = False
                    break
                    '''Ends loop and moves onto main game'''  
       
    '''Message for player about their choice'''
    #print ("Your Choice is", playersChoice) #test
    number = playersChoice - 1
    playerMessage = number_to_name(number)
    print playerMessage
    sense.set_rotation(0)
    #sense.show_message("You = ", text_colour=[0, 255, 255], scroll_speed = 0.08)
    #sense.show_message(playerMessage, text_colour=[0, 0, 255], scroll_speed = 0.08) 

    ###COMPUTER SELECTION
    '''Computer selects a random choice from the options'''
    count = random.randrange(5,50)
    sense.set_rotation(90)
    while count > 1:
        computer_choice = random.randrange(0,5)
        print computer_choice
        time.sleep(0.1)
        sense.load_image(str(computer_choice) + ".png")
        count = count - 1

	#time.sleep(1)
    '''Message for player about the computer's choice'''
    print ("The computers choice is", computer_choice)
    number = computer_choice
    computerMessage = number_to_name(number)
    print computerMessage ##test
    sense.set_rotation(0)
    sense.show_message("Computer = ", text_colour=[0, 150, 255], scroll_speed = 0.06)
    #sense.show_message(computerMessage, text_colour=[0, 0, 255], scroll_speed = 0.08)
    sense.load_image(str(computer_choice) + ".png")
    
    print computerMessage
    
    time.sleep(1)
    
    ###WINNER CALCULATED###
    '''Calculates the Winner'''
    result = (int(computer_choice - (playersChoice-1))) % 5 
        #print result
    if result == 0:
            sense.show_message("Player and Computer Tie!", text_colour=[0, 0, 255], scroll_speed = 0.08)
            #print "tie"
    elif result >=3:
            sense.show_message("Player Wins!", text_colour=[0, 255, 0], scroll_speed = 0.08)
            #print "Player wins!"
    else:
            time.sleep(1)
            sense.show_message("Computer Wins!", text_colour=[255, 0, 0], scroll_speed = 0.08)##??
            #print "Computer wins!"
    print " "        
     
###START THE GAME##
sense.show_message("Welcome to R.P.S.L.S!", text_colour=[155, 100, 30], scroll_speed = 0.08)
sense.show_message("Pleases use 'Up' to select", text_colour=[155, 255, 255], scroll_speed = 0.05)
sense.load_image("0.png")

while gameRunning == True:
    play_again = 1
    
    mainGame()
    sense.show_message("Play Again?", text_colour=[255, 255, 255], scroll_speed = 0.08)
    while play_again == 1:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                        if event.key == K_UP:
                            play_again = 0
                            
            if event.type == KEYDOWN:
                        if event.key == K_DOWN:
                            print("Bye")
                            sense.show_message("Bye Bye", text_colour=[255, 255, 255], scroll_speed = 0.08)
                            play_again = 0
                            gameRunning = False
