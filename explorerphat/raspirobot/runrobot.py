import sys, tty, termios, time
import explorerhat

# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	return ch

def forward():
	print("Going forward!")
	explorerhat.motor.one.forwards()
	explorerhat.motor.two.forwards()

def right():
	print("Going right!")
	explorerhat.motor.one.forwards()
	explorerhat.motor.two.backwards()

def left():
	print("Going left!")
	explorerhat.motor.one.backwards()
	explorerhat.motor.two.forwards()

def backwards():
	print("Going reverse!")
	explorerhat.motor.one.backwards()
	explorerhat.motor.two.backwards()

def stop():
	explorerhat.motor.one.stop()
	explorerhat.motor.two.stop()
	print("stopped")

while True:
	ch = getch()

	print(ch)
	if (ch == 'q'):
		break
	
	if (ch == 'w'):
		forward()
	
	if (ch == 's'):
		backwards()
	
	if (ch == 'a'):
		left()
	
	if (ch == 'd'):
		right()
	
	if (ch == ' '):
		stop()
	#time.sleep(0.2)
	#stop()