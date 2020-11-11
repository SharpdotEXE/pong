import pygame
import random


class paddle:
	
	def __init__(self, x, y, speed, top_boundary, bottom_boundary, picture):
		self.x = x
		self.y = y
		
		self.speed = speed
		self.top_boundary = top_boundary
		self.bottom_boundary = bottom_boundary
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
		

class Ball:

	def __init__(self, x, y, max_speed, x_speed, y_speed, picture):
		self.x = x
		self.y = y
		self.max_speed = max_speed
		self.x_speed = x_speed
		self.y_speed = y_speed

	def y_bounce(self):
		self.y_speed *= -1

	def x_bounce(self):
		self.x_speed *= -1



width, height = 800, 600
screen = pygame.display.set_mode((width, height))

color = (50, 164, 168)

leftpaddle_x = 30
leftpaddle_y = 250
leftpaddle_speed = .225
left_top_boundary = 0
left_bottom_boundary = 536
leftpaddle_picture = 'paddle.png'
leftpaddle = paddle(leftpaddle_x, leftpaddle_y, leftpaddle_speed, left_top_boundary, left_bottom_boundary, leftpaddle_picture)

rightpaddle_x = 705
rightpaddle_y = 250
rightpaddle_speed = .225
right_top_boundary = 0
right_bottom_boundary = 536
rightpaddle_picture = 'paddle.png'
rightpaddle = paddle(rightpaddle_x, rightpaddle_y, rightpaddle_speed, right_top_boundary, right_bottom_boundary, rightpaddle_picture)


pygame.init()

running = True
while running:

	
	screen.fill(color)

	leftpaddle.load_picture()
	rightpaddle.load_picture()
	

	keys = pygame.key.get_pressed()
	
	
	if keys[pygame.K_w]:
		leftpaddle.moveup()
		
	if keys[pygame.K_s]:
		leftpaddle.movedown()
		

	if keys[pygame.K_UP]:
		rightpaddle.moveup()
	if keys[pygame.K_DOWN]:
		rightpaddle.movedown()

	
	leftpaddle.check_boundary()
	rightpaddle.check_boundary()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	pygame.display.update()
