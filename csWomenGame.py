import pygame
# need to actually use pygame funcs
pygame.init()
#set up window
width = 800
height = 600
win_tit = "Hist 201: Historical Women in Computer Science - Josette Grinslade"
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption(win_tit)

black = (0,0,0)
white = (255,255,255)

clock = pygame.time.Clock()
# Character Initialization
char_img = pygame.image.load('kirby.png')
char_width = 73
char_speed = 0
def character(x,y):
    screen.blit(char_img, (x,y))
    #screen.blit(pygame.transform.scale(villager_img, (800,600)), (0,0))
'''
x = (width * 0.45)
y = (height * 0.8)
'''



def game_loop():

    x = (width * 0.25)
    y = (height * 0.6)
    x_change = 0

    exit = False

    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
        x += x_change

        screen.fill(white)
        character(x,y)

        if x > width - char_width or x < 0:
            exit = True

        pygame.display.update()
        clock.tick(60)

# actually running the game here
game_loop()
pygame.quit()
quit()
