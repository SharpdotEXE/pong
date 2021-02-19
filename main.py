import pygame
import random

pygame.init()


class Paddle:

    def __init__(self, x, y, face):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 64
        self.speed = 2
        self.color = (52, 235, 195)
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)
        self.face = face


    def render(self):

        pygame.draw.rect(screen, self.color, self.hit_box)


    def check_boundary(self):

        if self.y <= top_boundary:
            self.y = top_boundary

        if self.y >= bottom_boundary:
            self.y = bottom_boundary


    def move_up(self):

        self.y -= self.speed


    def move_down(self):

        self.y += self.speed


    def update_hit_box(self):

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
        self.update_hit_box()
        self.check_boundary()
        self.check_pressed_keys()


class Ball:

    def __init__(self):

        self.x = 400
        self.y = 268
        self.width = 32
        self.height = 32
        self.max_speed = 5
        self.x_speed = random.choice(range(5, 40)) / 10
        self.y_speed = self.max_speed - self.x_speed
        self.color = (3, 123, 252)
        self.top_boundary = 0
        self.bottom_boundary = 568
        self.left_boundary = left_boundary
        self.right_boundary = right_boundary
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)


    def render(self):

        pygame.draw.circle(screen, self.color, [self.x + .5 * self.width, self.y + .5 * self.height], 16)

 
    def move(self):

        self.x += self.x_speed
        self.y += self.y_speed


    def check_wall_bounce(self):

        if self.y <= self.top_boundary:
            self.y_speed *= -1

        if self.y >= self.bottom_boundary:
            self.y_speed *= -1


    def bounce_off_paddle(self):
        pass
        #if self.x



    def update_hit_box(self):

        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)


    def check_paddle_collision(self):

        if pygame.Rect.colliderect(self.hit_box, left_paddle.hit_box):
            self.bounce_off_paddle()

        if pygame.Rect.colliderect(self.hit_box, right_paddle.hit_box):
            self.bounce_off_paddle()
 

    def new_speed(self):

        self.x_speed = random.choice(range(10, 45)) / 10
        self.y_speed = self.max_speed - self.x_speed

        self.x_speed *= random.choice([-1, 1])
        self.y_speed *= random.choice([-1, 1])


    def update(self):

        self.render()
        self.move()
        self.update_hit_box()
        self.check_wall_bounce()
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


def render_score_board():
        pygame.draw.line(screen, 'black', (0, 600), (800, 600), 5)


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
top_boundary = 0
bottom_boundary = 536
left_boundary = 0
right_boundary = 768

ball = Ball()
ball.new_speed()

copy_x = ball.x_speed
copy_y = ball.y_speed

left_paddle = Paddle(50, 250, 80)
right_paddle = Paddle(720, 250, 720)

left_score = Score_board(150, 625)
right_score = Score_board(650, 625)


# game loop
running = True
while running:

    screen.fill(color)

    pygame.draw.line(screen, 'black', (left_paddle.face, 0), (left_paddle.face, height))
    pygame.draw.line(screen, 'black', (right_paddle.face, 0), (right_paddle.face, height))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:

        ball.x_speed, ball.y_speed = 0, 0

    keys = pygame.key.get_pressed()

    if keys[pygame.K_b]:

        ball.x_speed, ball.y_speed = copy_x, copy_y


    left_score.render_score()

    right_score.render_score()


    ball.update()
    left_paddle.update()
    right_paddle.update()


    check_update_score()
    check_recenter()
    render_score_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    fpsClock.tick(fps)

    print(ball.hit_box, right_paddle.hit_box)
    #print(round(ball.x), round(ball.y))
