import pygame


class LED():
	def __init__(self, pos=(0, 0), radius=25, lit=False):

	   # Initializes the LED

		self.pos = pos
		self.lit = lit
		self.radius = radius
		self.screen = pygame.display.get_surface()
		self.color = (255, 255, 255)
		self.pos_x = int(self.pos[0] * (self.radius * 2 + 5)) + (self.radius)
		self.pos_y = int(self.pos[1] * (self.radius * 2 + 5)) + (self.radius) + 40

	def draw(self):

		#Draws a circle,
		w = []
		if self.lit: # has it been clicked?
			thickness = 0
		else:
			self.color = [255,255,255]
			thickness = 1

		pygame.draw.circle(self.screen, self.color, (self.pos_x, self.pos_y), self.radius, thickness)

		# Draws a square
		pygame.draw.rect(self.screen,self.color,(self.pos_x-self.radius, self.pos_y-self.radius, (2*self.radius),(2*self.radius)),thickness)

	def clicked(self, colour):

		# what to do when clicked
		self.color = colour
		if self.lit:
			self.lit = False
		else:
			self.lit = True
