import pygame
import random


class paddle:
	
	def __init__(self, x, y, hitbox, speed, top_boundary, bottom_boundary, picture):
		self.x = x
		self.y = y
		self.hitbox = hitbox
		self.speed = speed
		self.top_boundary = top_boundary
		self.bottom_boundary = bottom_boundary
		self.picture = picture
		

	def load_picture(self):
		
		screen.blit(pygame.image.load(self.picture), (self.x, self.y))


	def check_boundary(self):
		if self.y < top_boundary:
			self.y = top_boundary
		if self.y > bottom_boundary:
			self.y = bottom_boundary


	def moveup(self):
		self.y -= self.speed
		#self.hitbox = [i for i in range(round(self.y), round(self.y) + paddle_pixel_size)]

	def movedown(self):
		self.y += self.speed
		#self.hitbox = [i for i in range(round(self.y), round(self.y) + paddle_pixel_size)]



class Ball:

	def __init__(self, x, y, hitbox, x_speed, y_speed, image):
		self.x = x
		self.y = y
		self.hitbox = hitbox
		self.x_speed = x_speed
		self.y_speed = y_speed

	def y_bounce(self):
		self.y_speed *= -1

	def x_bounce(self):
		self.x_speed *= -1



width, height = 800, 600
screen = pygame.display.set_mode((width, height))

color = (50, 164, 168)

paddle_pixel_size = 64

leftpaddle_x, leftpaddle_y, leftpaddle_speed, top_boundary, bottom_boundary, leftpaddle_picture = 30, 250, .225, 0, 536, 'paddle.png'

leftpaddle = paddle(leftpaddle_x, leftpaddle_y, leftpaddle_speed, top_boundary, bottom_boundary, leftpaddle_picture, leftpaddle_picture)

rightpaddle_x, rightpaddle_y, rightpaddle_speed, top_boundary, bottom_boundary, rightpaddle_picture = 705, 250, .225, 0, 536, 'paddle.png'

rightpaddle = paddle(rightpaddle_x, rightpaddle_y, rightpaddle_speed, top_boundary, bottom_boundary, rightpaddle_picture, rightpaddle_picture)



pygame.init()

running = True
while running:

	
	screen.fill((color))

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

	#print(leftpaddle.hitbox)
	