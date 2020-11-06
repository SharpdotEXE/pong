import pygame
import random

#initializes the game
pygame.init()

width, height = 800, 600 #display width, height
x, y = 30, 250 #left paddle starting coordinates
a, b = 705, 250 #right paddle starting coordinates
p, q = 400, 268 #ball starting coordinates
y_speed = .225 #left paddle speed
b_speed = .225 #right paddle speed
ball_x_speed = .125 #ball horizontal speed    #These must add up to max_speed
ball_y_speed = .125 #ball vertical speed 	  #these must add up to max_speed
max_speed = .25 #combined x and y ball speed
white = (255, 255, 255) #test rect color
multiplier = .5

ls = [i * .001 for i in range(1, 250)] #sets up  variable x and y speeds 




#creates display
screen = pygame.display.set_mode((width, height))

#loads images
left_paddle = pygame.image.load('paddle.png')
right_paddle = pygame.image.load('paddle.png')
ball = pygame.image.load('pongball.png')

clock = pygame.time.Clock()


#creates paddles and ball
def leftpaddle(x,y):
	screen.blit(left_paddle, (x, y))

	global lp_hitbox
	lp_hitbox = [i for i in range(round(y), round(y) + 64)]
	

def rightpaddle(a, b):
	screen.blit(right_paddle, (a, b))

	global rp_hitbox
	rp_hitbox = [i for i in range(round(b), round(b) + 64)]
	

def pongball(p, q):
	screen.blit(ball, (p, q))

	global ball_hitbox
	ball_hitbox = [i for i in range(round(q), round(q) + 32)]
	


#begins game loop
running = True
while running:
	
	#sets background color
	screen.fill((50, 164, 168))

	#puts all 3 images on screen at abstract coordinates ()
	leftpaddle(x, y)
	rightpaddle(a, b)
	pongball(p, q)

	#hitbox stuff 
	#pygame.draw.rect(screen, white, (50,150,25,75))

	#initial ball movement
	p += ball_x_speed
	q += ball_y_speed
	
	#currently used for being able to exit the game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		#print(event) for debugging purposes mostly

		
		
	#sets a variable to the currently pressed key
	keys = pygame.key.get_pressed()
	
	#left paddle
	if keys[pygame.K_w]:
		y -= y_speed
	if keys[pygame.K_s]:
		y += y_speed

	#right paddle
	if keys[pygame.K_UP]:
		b -= b_speed
	if keys[pygame.K_DOWN]:
		b += b_speed


	#reset the game
	if keys[pygame.K_SPACE]:
		p = 400 #resets the ball at the middle
		q = 268
		
		x, y = 30, 250 #resets the paddles 
		a, b = 705, 250


		ball_x_speed = random.choice(ls) #picks a random float between .001 and .249
		ball_y_speed = max_speed - abs(ball_x_speed) #ball_y_speed is the remainder

		ball_x_speed *= random.choice([-1, 1]) #creates random up, down, side to side launch
		ball_y_speed *= random.choice([-1, 1])
		
		
	
	#left paddle boundaries
	if y < 0:
		y = 0
	if y > 536:
		y = 536

	#right paddle boundaries
	if b < 0:
		b = 0
	if b > 536:
		b = 536
	#boundaries, dwight
	
	"""

	#auto reset after goal
	if p < 0:
		p = 400 #resets the ball at the middle
		q = 268
		
		x, y = 30, 250 #resets the paddles 
		a, b = 705, 250


		ball_x_speed = random.choice(ls) #picks a random float between .001 and .249
		ball_y_speed = max_speed - abs(ball_x_speed) #ball_y_speed is the remainder

		ball_x_speed *= random.choice([-1, 1]) #creates random up, down, side to side launch
		ball_y_speed *= random.choice([-1, 1])		#ball_x_speed *= -1 

	if p > 768:
		p = 400 #resets the ball at the middle
		q = 268
		
		x, y = 30, 250 #resets the paddles 
		a, b = 705, 250


		ball_x_speed = random.choice(ls) #picks a random float between .001 and .249
		ball_y_speed = max_speed - abs(ball_x_speed) #ball_y_speed is the remainder

		ball_x_speed *= random.choice([-1, 1]) #creates random up, down, side to side launch
		ball_y_speed *= random.choice([-1, 1])
		#ball_x_speed *= -1
	
	"""

	#ball horizontal movement
	if p < 0:
		ball_x_speed *= -1 
	if p > 768:
		ball_x_speed *= -1


	#ball vertical movement
	#the -1 makes the ball bounce off the boundary
	if q < 0:
		ball_y_speed *= -1
	if q > 568:
		ball_y_speed *= -1
	



	#AI, will turn into function later
	#4 game modes? easy, medium, hard, unstoppable?
	
	
	#recentering
	if ball_x_speed > 0: #if ball is coming towards ai	
		if b < q:
			b += b_speed * multiplier 
		elif b > q:
			b -= b_speed * multiplier

	
	elif ball_x_speed < 0: #if ball is leaving ai
		if b > 250:
			b -= b_speed * multiplier
		elif b < 250:
			b += b_speed * multiplier
	

	if p == 75:
		for i in ball_hitbox:
			if i in lp_hitbox:
				ball_x_speed *= -1
				break

	if p == 693:
		for i in ball_hitbox:
			if i in rp_hitbox:
				ball_x_speed *= -1
				break

	
	
	
	

	pygame.display.update()
	clock.tick(2000)
	

	#debugging
	#print(clock)

	#print(ball_y_speed, y, b)

	#print(round(q))


	#print(round(y))

	#print(round(y))

	#print(round(p), round(y))

	#if round(p) == round(y):
		#print('collide')
	#print(0)