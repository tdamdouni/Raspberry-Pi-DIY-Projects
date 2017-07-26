from sense_hat import SenseHat
from random import choice
from copy import deepcopy
import curses


sense = SenseHat()

sense.clear(0,0,0)
mine = (80,0,0)
clear = (40,40,40)
marked = (255,0,0)
free = (255,255,255)
touching = (0,0,255)
x = 0
y = 0
ratios = [mine,clear,clear,clear]

original_board=[]
for i in range(8):
    original_board.append([choice(ratios) for i in range(8)]) 

player_board = deepcopy(original_board)

screen = curses.initscr()
screen.keypad(True)
curses.cbreak()
#curses.noecho()

def flattened():
    flat = [i for j in player_board for i in j]
    return flat

def check_position(x,y):
    global game_over
    if player_board[y][x] == marked:
        if original_board[y][x] == mine:
            screen.addstr(12,12,'That was a mine')
            game_over = True
        if original_board[y][x] == clear:
            player_board[y][x] = clear
            find_clear(x,y)
    elif player_board[y][x] == free:
        pass
    else:
        player_board[y][x] = marked
        screen.addstr(12,12,'Marked')
    
def find_clear(x,y):
    checked = []
    cascade = []
    cascade.append((x,y))
    while len(cascade) != 0:
        check = cascade.pop(0)
        adjacent = 0
        surrounding = get_surrounding(check[0],check[1])
        adjacent, no_mines, checked = check_surrounding(surrounding,checked)
        for square in no_mines:
            if square not in checked:
                cascade.append(square)
        checked.append(check)
        if adjacent == 0:
            player_board[check[1]][check[0]] = free
        else:
            player_board[check[1]][check[0]] = touching

def get_surrounding(x,y):
    surrounding = []
    for i in range(x-1,x+1):
        for j in range(y-1,y+1):
            if (i,j) != (x,y):
                surrounding.append((i,j))
    return surrounding

def check_surrounding(surrounding,checked):
    adjacent = 0
    no_mines = []
    for square in surrounding:
        if square not in checked:
            checked.append(square)
        try:
            if original_board[square[1]][square[0]] == mine:
                adjacent += 1
            elif original_board[square[1]][square[0]] == clear:
                no_mines.append(square)
        except IndexError:
            pass
    return adjacent, no_mines, checked
        


game_over = False

while not game_over:

    sense.set_pixels(flattened())
    sense.set_pixel(x,y,0,255,0)

    key = screen.getch()
    
    if key == curses.KEY_LEFT:
        if x > 0:
            x -= 1

    if key == curses.KEY_RIGHT:
        if x < 7:
            x += 1
            
    if key == curses.KEY_UP:
        if y > 0:
            y -= 1

    if key == curses.KEY_DOWN:
        if y < 7:
            y += 1

    if key == ord('\n'):
        check_position(x,y)

