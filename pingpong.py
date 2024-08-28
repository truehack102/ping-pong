from pygame import *
from random import *
init()

win = display.set_mode((700,500))
display.set_caption('Пинг-Понг')

bg = (255, 182, 193)
win.fill(bg)

clock = time.Clock()

FPS = 60
run = True
finish = False

font1 = font.SysFont('comic sans', 50)

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed_x, player_speed_y, width, heigth):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, heigth))
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self, key1, key2):
        keys_pressed = key.get_pressed()

        if keys_pressed[key1] and self.rect.y > 5:
            self.rect.y -= self.speed_y

        if keys_pressed[key2] and self.rect.y < 425:
            self.rect.y += self.speed_y
        

    #def start_pos(self):
        #angle = randint(1, 4)
        #if angle == 1:

        #if angle == 2:

        #if angle == 3:

        #if angle == 4:

platform1 = Player(r'C:\Users\User\OneDrive\Рабочий стол\VscProjects\Ping-Pong\racket.png', 5, 220, 8, 8, 22, 70)
platform2 = Player(r'C:\Users\User\OneDrive\Рабочий стол\VscProjects\Ping-Pong\racket.png', 670, 220, 8, 8, 22, 70)
ball = GameSprite(r'C:\Users\User\OneDrive\Рабочий стол\VscProjects\Ping-Pong\tenis_ball.png', 320, 250, 6, 6, 30, 30)

lose1 = font1.render('PLAYA 1 LOST', True, (230, 20, 20))
lose2 = font1.render('PLAYA 2 LOST', True, (230, 20, 20))
score1 = 0
score2 = 0
p = font1.render('<3', True, (230, 20, 20))
while run:
    if finish == False:
        win.fill(bg)
        platform1.reset()
        platform2.reset()
        platform1.update(K_w, K_s)
        platform2.update(K_UP, K_DOWN)
        ball.reset()
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y

        versus = str(score1) + ':' + str(score2)
        score_text = font1.render(versus, True, (0, 0, 0))
        win.blit(score_text, (310, 5))
        
        if ball.rect.y > 470 or ball.rect.y < 0:
            ball.speed_y *= -1

        if sprite.collide_rect(ball, platform1) or sprite.collide_rect(ball, platform2):
            ball.speed_x *= -1
        
        if ball.rect.x < 0:
            #win.blit(lose1, (180, 210))
            score2 += 1
            ball.rect.x = 320
            ball.rect.y = 250

        if ball.rect.x > 670:
            #win.blit(lose2, (180, 210))
            score1 += 1
            ball.rect.x = 320
            ball.rect.y = 250
            
        if score1 >= 3:
            win.blit(lose2, (180, 210))
            finish = True

        if score2 >= 3:
            win.blit(lose1, (180, 210))
            finish = True

    for e in event.get():
        if e.type == QUIT:
            run = False

    clock.tick(FPS)
    display.update()