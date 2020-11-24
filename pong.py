import pygame
import random


class paddle:
	
	def __init__(self, x, y, speed, top_boundary, bottom_boundary, hitbox, picture):
		self.x = x
		self.y = y
		self.speed = speed
		self.top_boundary = top_boundary
		self.bottom_boundary = bottom_boundary
		self.hitbox = hitbox
		self.picture = picture
		

	def load_picture(self):
		
		screen.blit(pygame.image.load(self.picture), (self.x, self.y))


	def check_boundary(self):
		if self.y < self.top_boundary:
			self.y = self.top_boundary
		if self.y > self.bottom_boundary:
			self.y = self.bottom_boundary


	def moveup(self):
		self.y -= self.speed

	def movedown(self):
		self.y += self.speed

	def move_hitbox(self):
		self.hitbox = [i for i in range(round(self.y), round(self.y) + 64)]
		

class Ball:

	def __init__(self, x, y, max_speed, x_speed, y_speed, top_boundary, bottom_boundary, left_boundary, right_boundary, hitbox, picture):
		self.x = x
		self.y = y
		self.max_speed = max_speed
		self.x_speed = x_speed
		self.y_speed = y_speed
		self.top_boundary = top_boundary
		self.bottom_boundary = bottom_boundary
		self.left_boundary = left_boundary
		self.right_boundary = right_boundary
		self.hitbox = hitbox
		self.picture = picture


	def load_picture(self):
		screen.blit(pygame.image.load(self.picture), (self.x, self.y))

	def move(self):
		self.x += self.x_speed
		self.y += self.y_speed


	def check_boundary(self):
		if self.y < self.top_boundary:
			self.y_speed *= -1
		if self.y > self.bottom_boundary:
			self.y_speed *= -1

		if self.x < self.left_boundary:
			self.x_speed *= -1
		if self.x > self.right_boundary:
			self.x_speed *= -1

	def move_hitbox(self):
		self.hitbox = [i for i in range(round(self.y), round(self.y) + 32)]

	def bounce(self):
		self.x_speed *= -1


def check_keys_pressed():

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_w]:
		leftpaddle.moveup()
	if keys[pygame.K_s]:
		leftpaddle.movedown()
		
	if keys[pygame.K_UP]:
		rightpaddle.moveup()
	if keys[pygame.K_DOWN]:
		rightpaddle.movedown()


def check_hitboxes():
	if round(ball.x) == 75: 	# left paddle x
			for i in ball.hitbox:
				if i in leftpaddle.hitbox:
					ball.x_speed *= -1
					break

	if round(ball.x) == 693: 	# right paddle x
		for i in ball.hitbox:
			if i in rightpaddle.hitbox:
				ball.x_speed *= -1
				break



width, height = 800, 600
screen = pygame.display.set_mode((width, height))

ball_max_speed = .250
ball_x_speed = random.choice([.01, .02, .03, .04, .05, .06, .07, .08, .09, .1, .11, .12, .13, .14, .15, .16, .17, .18, .19, .2, .21, .22, .23, .24])
ball_y_speed = ball_max_speed - ball_x_speed
ball_x_speed *= random.choice([-1, 1]) 
ball_y_speed *= random.choice([-1, 1])

ball = Ball(400, 268, .25, ball_x_speed, ball_y_speed, 0, 568, 0, 768, [i for i in range(round(400), round(400) + 32)], 'pongball.png')
leftpaddle = paddle(30, 250, .225, 0, 536, [i for i in range(round(250), round(250) + 64)], 'paddle.png')
rightpaddle = paddle(705, 250, .225, 0, 536, [i for i in range(round(250), round(250) + 64)], 'paddle.png')


pygame.init()

running = True
while running:

	screen.fill((50, 164, 168))

	leftpaddle.load_picture()
	rightpaddle.load_picture()
	ball.load_picture()

	ball.check_boundary()
	leftpaddle.check_boundary()
	rightpaddle.check_boundary()
	
	check_keys_pressed()
	leftpaddle.move_hitbox()
	rightpaddle.move_hitbox()
	ball.move()
	ball.move_hitbox()
	check_hitboxes()
	
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	

	pygame.display.update()
