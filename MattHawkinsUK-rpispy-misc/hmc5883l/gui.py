import pygame
import math
import hmc5883l as compass

pygame.init()

RED = (255,0,0)

size = [600,600]
needle_length = 235

screen = pygame.display.set_mode(size)

pygame.display.set_caption("RPiSpy Digital Compass")

background_image = pygame.image.load("compass.png").convert()

prev_bearing = 0
done = False

compass.configure()

while not done:

  # Get compass data
  x,y,z = compass.read_values()
  bearing_rad = compass.calc_bearing(x,y,0)
  bearing = compass.calc_bearing(x,y,1)
  
  # Update if change is more than 2 degrees
  if abs(bearing-prev_bearing)>2:
  
    x1 = needle_length * math.sin(bearing_rad)
    y1 = needle_length * math.cos(bearing_rad)

    x2 = 300 + x1
    y2 = 300 - y1
    
    print "Bearing : {:.2f}  x1:{:.2f}  y1:{:.2f}".format(bearing,x1,y1)
    
    screen.blit(background_image,[0,0])
    pygame.draw.line(screen,RED,[300,300],[x2,y2],8)
    pygame.display.flip()
    prev_bearing = bearing
  
  # Check for ESC key
  event = pygame.event.wait ()
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        done = True
  
  pygame.time.wait(1000)

pygame.quit()