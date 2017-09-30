# "Lead Paint"=Bad, "LED Paint"=Good (or it could be.....)

# A (very badly written) tool for 'painting' on the Raspberry Pi 'SenseHat' LED matrix
# You'll need a GUI to run this: it launches a 'Tkinter' Canvas of 8x8 squares: left-click to set an LED on, right-click to clear it.

# Note: bit buggy for instance, it is possible to generate errors when clicking on the extreme right/bottom of the canvas (out of range values for sensehat pixels generated).
# Initially: it loaded the current state of the sensehat LEDs ; but this got complicated quickly.
# Weird issue (could my fault) when using the 'rotation' flag; in that 'reloading' the values back gives the non-rotated values - so disabled that feature.
# Some other unused cruft lying around in the code.
# TBD: 
#	-There should be a palette to select different colours.(sort of done: space cycles through the colours now)
# 	-It should really load the current state of the sensehat matrix at startup (so you can 'load' other 'pictures' for editing).
#	-It should generate (python or just a text file?) that can be copied/saved to re-generate the pattern: perhaps in a separate window.
#	-It would be cool to be able to generate 'frames' and play them back as animations.....
#	-Refactor into nice code, rather than this unholy mess :-)
#
 
from Tkinter import *
from sense_hat import SenseHat


current_paint_brush=0
paint_brushes=[]
for b in range(0,2):
	for g in range(0,2):
		for r in range(0,2):
			if r==0 and g==0 and b==0:
				pass
			else:
				paint_brushes.append( (r*255,g*255,b*255) )

eraser=(0,0,0)

class Paint(object):

	def motion(self, event):
	#tbd: sense LED 'cursor'?
		x,y=self.scale_sense_pixels(event.x,event.y)
		old_value=self.sense.get_pixel(x,y)
		print value

	def key(self, event):
		global current_paint_brush
		if event.char==' ':
			current_paint_brush+=1
			if current_paint_brush==len(paint_brushes):
				current_paint_brush=0
				return
		if event.char=='i':
			pixels=self.sense.get_pixels()
			print pixels


	def scale_sense_pixels(self, canvas_x, canvas_y):
		x=canvas_x/self.x_step
		y=canvas_y/self.y_step
		if x<0:
			x=0
		if y<0:
			y=0
		if x>=self.sense_width:
			x=self.sense_width-1
		if y>=self.sense_height:
			y=self.sense_height-1
		return (x,y)


	# Clear the pixel
	def right_click(self,event):
		x,y=self.scale_sense_pixels(event.x, event.y)
		self.sense.set_pixel(x,y, eraser )
		w=event.widget.find_closest(event.x, event.y)
		self.canvas.itemconfigure(w, fill='black') # sort of cheating here
		
	# 'Paint' the pixel
	def left_click(self,event):
		global current_paint_brush
		global paint_brushes
		x,y=self.scale_sense_pixels(event.x, event.y)
		self.sense.set_pixel(x,y, paint_brushes[current_paint_brush] )
		w=event.widget.find_closest(event.x, event.y)
		self.canvas.itemconfigure(w, fill="#%02X%02X%02X"%(paint_brushes[current_paint_brush][0], paint_brushes[current_paint_brush][1], paint_brushes[current_paint_brush][2]))

	def __init__(self, width=200, height=200):
		self.sense=SenseHat()
		self.sense.set_rotation(180) # this actually messes up our 'get_pixels()' , since it doesn't seem to take into account the rot !
		self.sense.clear( (0,0,0))  # which is why we have to clear them each time  (I guess we should store the rotation value and compensate for each startup?)
		self.width=width
		self.height=height
		self.sense_width=8
		self.sense_height=8

		self.x_step=self.width/self.sense_width
		self.y_step=self.height/self.sense_height

		self.root=Tk()
		self.root.title('LED Painter')
		self.canvas=Canvas(self.root, width=self.width, height=self.height)
		self.mypixels=self.sense.get_pixels()
		pixel_counter=0

		for x in range(0, self.width, self.x_step):
			for y in range(0, self.height, self.y_step):
				fill_colour='black' # temporary hack, should really take the 'clear' off earlier and map FROM senseboard to Tkinter initially
				p=self.canvas.create_rectangle(x,y,x+self.x_step, y+self.y_step, outline='white', fill=fill_colour)
				pixel_counter+=1
				self.canvas.tag_bind(p, '<ButtonPress-1>',self.left_click)
				self.canvas.tag_bind(p, '<B1-Motion>',self.left_click)
				self.canvas.tag_bind(p, '<ButtonPress-3>',self.right_click)
				self.canvas.tag_bind(p, '<B3-Motion>',self.right_click)
		
				self.root.bind("<Key>", self.key)
	#			self.root.bind("<Motion>", self.motion)
		self.canvas.pack()	
		self.root.mainloop()


if __name__=='__main__':
	paint=Paint(width=400,height=400)
