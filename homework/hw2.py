import sys, pygame
pygame.init()

size = width, height = # change the window size to 640x480
speed = # change the x speed to 4 and the y speed to 3
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
		# also increase the x speed every time it flips
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		# also increase the y speed every time it flips

	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()