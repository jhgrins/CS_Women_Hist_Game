import pygame
import time
import random
# need to actually use pygame funcs
pygame.init()
#set up window
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

class game_stuff:


    def __init__(self, title):
        pygame.display.set_caption(title)
        self.background_image = pygame.image.load("stars.png").convert()
        self.lives = 3
        self.score = 0

    def message_display(self, phrase, color, x, y):
        basicfont = pygame.font.SysFont(None, 32)
        text = basicfont.render(phrase, True, color, (0, 0, 0))
        screen.blit(text, [x,y])

    def collision(self, bad_guy, heroin):
        if heroin.y < bad_guy.y+bad_guy.height:

           if heroin.x > bad_guy.x and heroin.x < bad_guy.x + bad_guy.width or heroin.x+heroin.width > bad_guy.x and heroin.x + heroin.width < bad_guy.x+bad_guy.width:
              self.message_display("ow!", red, screen_width/2 - 5, 5)
              #pygame.mixer.music.load('slap.mp3')
              #pygame.mixer.music.play(0)
              #self.lives -= 1

    def shot_bad_guy(self, bad_guy, heroin):
        if heroin.bullet_y < bad_guy.y+bad_guy.height:

           if heroin.bullet_x > bad_guy.x and heroin.bullet_x < bad_guy.x + bad_guy.width or heroin.bullet_x+heroin.bullet_w > bad_guy.x and heroin.bullet_x + heroin.bullet_w < bad_guy.x+bad_guy.width:
              heroin.bullet_fired = False
              self.score += 1
              bad_guy.move_back()
              bad_guy.draw()


# heroacter Initialization
class player():

    width = 45
    height = 50
    speed = 0
    x_change = 0
    bullet_fired = False
    bullet_w = 5
    bullet_h = 10

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.x_change = 0
        self.bullet_x = -1
        self.bullet_y = -1

    def draw(self):
        screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.x += self.x_change

    def move_left(self):
        self.x_change = -5

    def move_right(self):
        self.x_change = 5

    def dont_move(self):
        self.x_change = 0

    def check_out_frame(self):
        if self.x > screen_width - self.width:
            self.x = screen_width - self.width
        elif self.x < 0:
            self.x = 0

    def draw_bullet(self):
        pygame.draw.rect(screen, red, [self.bullet_x, self.bullet_y, self.bullet_w, self.bullet_h])
        if(self.bullet_y < 0):
            self.bullet_fired = False
            self.bullet_x = self.x
            self.bullet_y = self.y
        else:
            self.bullet_y -= 10

    def shoot_bullet(self):
        pygame.mixer.music.load('pewpew.mp3')
        pygame.mixer.music.play(0)
        self.bullet_fired = True
        self.bullet_x = self.x
        self.bullet_y = self.y

class enemy:

    def __init__(self, x, y, img, speed, w, h):
        self.x = x
        self.y = y
        self.speed = speed
        self.img = img
        self.width = w
        self.height = h

    def draw(self):
        screen.blit(self.img, (self.x, self.y))
        self.y += self.speed

    def move_back(self):
        self.y = 0 - screen_height
        self.x = random.randrange(0, screen_width)

    def check_off(self):
        if self.y > screen_height:
            self.move_back()


def game_loop():
    game = game_stuff("Hist 201: Historical Women in Computer Science - Josette Grinslade")

    hero = player(( screen_width* 0.6), (screen_height * 0.93), pygame.image.load('rpgs2.png'))

    mark = enemy(random.randrange(0, screen_width), -450, pygame.image.load('mark2.png'), 2,  130, 152)
    bill = enemy(random.randrange(0, screen_width), -150, pygame.image.load('billgates.png'), 1, 178, 155)
    elon = enemy(random.randrange(0, screen_width), -350, pygame.image.load('elon.png'), 3, 166, 194)

    exit = False
    gameOver = False
    #pygame.mixer.music.load('imperial.mp3')
    #pygame.mixer.music.play(0)
    while not exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hero.move_left()
            if event.key == pygame.K_RIGHT:
                hero.move_right()
            if event.key == pygame.K_SPACE:
                if(not hero.bullet_fired):
                    hero.shoot_bullet()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                hero.dont_move()

        hero.move()

        screen.fill(white)
        screen.blit(game.background_image, [0, 0])



        scoreStr = "Score: " + str(game.score)
        #livesStr = "Lives: " + ('x'*game.lives)

        game.message_display(scoreStr, blue, 5, 5)
        #game.message_display(livesStr, blue, screen_width-125, 5)

        hero.draw()
        if(not gameOver):
            mark.draw()
            bill.draw()
            elon.draw()

            if(hero.bullet_fired == True):
                hero.draw_bullet()


            hero.check_out_frame()

            mark.check_off()
            bill.check_off()
            elon.check_off()

            game.collision(mark, hero)
            game.collision(bill, hero)
            game.collision(elon, hero)

            game.shot_bad_guy(mark, hero)
            game.shot_bad_guy(bill, hero)
            game.shot_bad_guy(elon, hero)
        else:
            game.message_display("You win! Ada and Grace Congratulate you!!", green, screen_width/2 - 200, 250)
            screen.blit(pygame.image.load('ada.png'),[(screen_width* 0.6) - 350, screen_height - 200])
            screen.blit(pygame.image.load('grace.png'),[(screen_width* 0.6) + 85, screen_height-185])

        if(game.score == 5):
            gameOver = True

        pygame.display.update()
        clock.tick(60)


# actually running the game here
game_loop()
pygame.quit()
quit()
