import pygame
# need to actually use pygame funcs
pygame.init()
#set up window
screen_width = 800
screen_height = 600
win_tit = "Hist 201: Historical Women in Computer Science - Josette Grinslade"
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(win_tit)

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

# Character Initialization


class character:

    width = 45
    speed = 0
    x_change = 0

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.x_change = 0

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

background_image = pygame.image.load("stars.png").convert()


def game_loop():
    screen.blit(background_image,  [0, 0])
    char = character((screen_width * 0.6), (screen_height * 0.93), pygame.image.load('rpgs2.png'))
    exit = False
    while not exit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                char.move_left()
            elif event.key == pygame.K_RIGHT:
                char.move_right()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                char.dont_move()

        char.move()

        screen.fill(white)
        char.draw()

        char.check_out_frame()

        pygame.display.update()
        clock.tick(60)


# actually running the game here
game_loop()
pygame.quit()
quit()
