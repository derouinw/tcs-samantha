import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [4,3]
#  speed limit to have separate x
# and y values, like speed
speed_limit = [8, 10] 
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
		# implement speed_limit's x component
		if abs(speed[0]) < speed_limit[0]: 
			if speed[0] < 0:
				speed[0] -= 1
			else:
				speed[0] += 1
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		# implement speed_limit's y component
		if abs(speed[1]) < speed_limit[1]:
			if speed[1] > 0:

				speed[1] += 1
			else:
				speed[1] -= 1


	screen.fill(black)
	screen.blit(ball, ballrect)
	pygame.display.flip()