import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [4,3]
speed_move = [0,0]
speed_limit = 10
black = 0,0,0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.gif")
ballrect = ball.get_rect()

ball_move = pygame.image.load("ball.gif")
ballrect_move = ball_move.get_rect()

while 1:

	# event queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

		# user input
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				speed_move[0] = 5
			elif event.key == pygame.K_DOWN:
				speed_move[1] = 5
			elif event.key == pygame.K_LEFT:
				speed_move[0] = -5
			elif event.key == pygame.K_UP:
				speed_move[1] = -5
			''' TODO: exit the game if the escape key is pressed '''
			''' Note: may need to look online for what key escape is '''
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				speed_move[0] = 0
			elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
				speed_move[1] = 0

	# check wall collision
	if ballrect_move.left < 0:
		ballrect_move = ballrect_move.move([5,0])
	if ballrect_move.right > width:
		ballrect_move = ballrect_move.move([-5,0])
	if ballrect_move.top < 0:
		ballrect_move = ballrect_move.move([0,5])
	if ballrect_move.bottom > height:
		ballrect_move = ballrect_move.move([0,-5])

	ballrect_move = ballrect_move.move(speed_move)

	# bouncing ball
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
		if abs(speed[0]) < speed_limit: 
			if speed[0] < 0:
				speed[0] -= 1
			else:
				speed[0] += 1
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]
		if abs(speed[1]) < speed_limit:
			if speed[1] > 0:
				speed[1] += 1
			else:
				speed[1] -= 1


	# drawing code
	''' TOOO: draw the user-controlled ball (ball_move) on top if '''
	''' its moving right or down, and the bouncing ball on top if '''
	''' ball_move is moving left or up. '''
	screen.fill(black)
	screen.blit(ball, ballrect)
	screen.blit(ball_move, ballrect_move)
	pygame.display.flip()