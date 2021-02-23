import pygame
import random

pygame.init()


class Paddle:

    def __init__(self, x, face):
        
        self.x = x
        self.y = 250
        self.width = 30
        self.height = 64
        self.speed = 2
        self.color = (52, 235, 195)
        self.top_boundary = 0
        self.bottom_boundary = 536
        self.face = face

        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)


    def render(self):

        pygame.draw.rect(screen, self.color, self.hit_box)


    def check_boundary(self):

        if self.y <= self.top_boundary:
            self.y = self.top_boundary

        if self.y >= self.bottom_boundary:
            self.y = self.bottom_boundary


    def move_up(self):

        self.y -= self.speed


    def move_down(self):

        self.y += self.speed


    def update_hitbox(self):

        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)


    def check_pressed_keys(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            left_paddle.move_up()
        if keys[pygame.K_s]:
            left_paddle.move_down()

        if keys[pygame.K_UP]:
            right_paddle.move_up()
        if keys[pygame.K_DOWN]:
            right_paddle.move_down()


    def update(self):

        self.render()
        self.update_hitbox()
        self.check_boundary()
        self.check_pressed_keys()



class Ball:

    def __init__(self):

        self.x = 400
        self.y = 268
        self.width = 32
        self.height = 32
        self.max_speed = 5
        self.x_speed = random.choice(range(4 * self.max_speed, 8 * self.max_speed)) / 10        
        self.y_speed = self.max_speed - self.x_speed
        self.color = (3, 123, 252)
        self.top_boundary = 0
        self.bottom_boundary = 568
        self.left_boundary = 0
        self.right_boundary = 800
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)


    def render(self):

        pygame.draw.rect(screen, self.color, self.hit_box)


    def move(self):

        self.x += self.x_speed
        self.y += self.y_speed


    def check_wall_collision(self):

        if self.y <= self.top_boundary:
            self.y_speed *= -1

        if self.y >= self.bottom_boundary:
            self.y_speed *= -1


    def update_geometry(self):

        self.x = round(self.x)
        self.y = round(self.y)
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)


    def check_paddle_collision(self):

        if pygame.Rect.colliderect(self.hit_box, left_paddle.hit_box):
            self.x_speed *= -1

        if pygame.Rect.colliderect(self.hit_box, right_paddle.hit_box):
            self.x_speed *= -1


    def new_speed(self):

        self.x_speed = random.choice(range(4 * self.max_speed, 8 * self.max_speed)) / 10
        self.x_speed = round(self.x_speed, 1)

        self.y_speed = self.max_speed - self.x_speed
        self.y_speed = round(self.y_speed, 1)

        self.x_speed *= random.choice([-1, 1])
        self.y_speed *= random.choice([-1, 1])


    def update(self):

        self.render()
        self.move()
        self.update_geometry()
        self.check_wall_collision()
        self.check_paddle_collision()


class Score_board:

    def __init__(self, x, y):
        
        self.x = x
        self.y = y
        self.font = pygame.font.SysFont('Times New Roman', 42)
        self.color = (0, 0, 0)
        self.str_score = '0'
        self.int_score = 0


    def convert_score_types(self):

        self.str_score = str(self.int_score)


    def render_score(self):

        self.convert_score_types()
        self.score = self.font.render(self.str_score, False, self.color)
        screen.blit(self.score, (self.x, self.y))


def render_field():

    pygame.draw.line(screen, 'black', (0, 600), (800, 600), 5)  # bottom line
    pygame.draw.line(screen, 'black', (400, 0), (400, 700), 2)  # mid line


def check_update_score():

    if ball.x < ball.left_boundary:
        right_score.int_score += 1

    if ball.x > ball.right_boundary:
        left_score.int_score += 1


def check_recenter():

    if ball.x < ball.left_boundary or ball.x > ball.right_boundary:

        ball.x = 400
        ball.y = 268
        left_paddle.y, right_paddle.y = 250, 250

        ball.new_speed()


# creating variables and objects


fpsClock = pygame.time.Clock()
fps = 60
color = (50, 164, 168)
width, height = 800, 700
screen = pygame.display.set_mode((width, height))

ball = Ball()
ball.new_speed()

left_paddle = Paddle(50, 80)
right_paddle = Paddle(720, 720)

left_score = Score_board(150, 625)
right_score = Score_board(650, 625)

# game loop
running = True
while running:

    screen.fill(color)

    left_score.render_score()
    right_score.render_score()

    check_update_score()
    check_recenter()
    render_field()

    ball.update()
    left_paddle.update()
    right_paddle.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    fpsClock.tick(fps)

    print(ball.x_speed, ball.y_speed)
