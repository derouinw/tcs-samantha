import sys, pygame

# check collisions
def check_x_collision(b1, b2):
	if (b2.left<b1.right and b2.left >b1.left) or (b2.right>b1.left and b2.right<b1.right):
		return True
	else: 
		return False

def check_y_collision(b1, b2):
	if (b2.top>b1.top and b2.top< b1.bottom) or (b2.bottom<b1.bottom and b2.bottom >b1.top):
		return True
	else:
		return False

def is_collision(b1, b2):
	return check_x_collision(b1, b2) and check_y_collision(b1, b2)

def left_collision(b1, b2, b2_old):
	return b2_old.right < b1.left and b2.right >= b1.left

def right_collision(b1, b2, b2_old):
	return b2_old.left>b1.right and b2.left<=b1.right

def bottom_collision(b1, b2, b2_old):
	return b2_old.top>b1.bottom and b2.top<= b1.bottom

def top_collision(b1, b2, b2_old):
	return b2_old.bottom< b1.top and b2.bottom>= b1.top


# init
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
ballrect_move = ball_move.get_rect().move([500,50])

while 1:

	# event queue
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()

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
			elif event.key == pygame.K_ESCAPE:
				sys.exit()
			elif event.key ==pygame.K_SPACE:
				speed[0] = -speed[0]
			elif event.key == pygame.K_BACKSPACE:
				speed[1] = -speed[1]

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

	# check collision side
	if is_collision(ballrect_move, ballrect):
		x_collision = left_collision(ballrect_move, ballrect, ballrect_old) or right_collision(ballrect_move, ballrect, ballrect_old)
		y_collision = bottom_collision(ballrect_move, ballrect, ballrect_old) or top_collision(ballrect_move, ballrect, ballrect_old)
	else:
		x_collision = y_collision = False

	# bouncing ball
	ballrect_old = ballrect
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width or x_collision:
		speed[0] = -speed[0]
		ballrect = ballrect.move(speed[0], 0)
		if abs(speed[0]) < speed_limit: 
			if speed[0] < 0:
				speed[0] -= 1
			else:
				speed[0] += 1
	if ballrect.top < 0 or ballrect.bottom > height or y_collision:
		speed[1] = -speed[1]
		ballrect = ballrect.move(0, speed[1])
		if abs(speed[1]) < speed_limit:
			if speed[1] > 0:
				speed[1] += 1
			else:
				speed[1] -= 1

	# drawing code
	screen.fill(black)

	if speed_move[0] == 5 or speed_move[1] == 5:
		screen.blit(ball, ballrect)
		screen.blit(ball_move, ballrect_move)
	else:
		screen.blit(ball_move, ballrect_move)
		screen.blit(ball, ballrect)
	
	pygame.display.flip()
	
	