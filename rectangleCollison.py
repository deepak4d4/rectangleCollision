import pygame
import random


pygame.init()
pygame.display.set_caption("Stree race")
gameWindow = pygame.display.set_mode((100,250))

white = [255,255,255]
black = [0,0,0]
player_x=0
player_y=230
size = 20

clock = pygame.time.Clock()
fps =30
sc=0

in_oppenent_one_x= random.randrange(0,100,20)
in_oppenent_one_y= random.randint(0,10)
in_oppenent_two_x= random.randrange(0,100,20)
in_oppenent_two_y= random.randint(0,10)
gameover = False


oppenent_one_x = in_oppenent_one_x
oppenent_one_y = in_oppenent_one_y
oppenent_two_x = in_oppenent_two_x
oppenent_two_y = in_oppenent_two_y

velocity_one =4
velocity_two=4
exit_game = False
font = pygame.font.SysFont(None,20)

def scores(score,x,y):
    screen_text=font.render(score,True,black)
    gameWindow.blit(screen_text,[x,y])

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if player_x>0:
                    player_x-=20
            if event.key == pygame.K_RIGHT:
                if player_x<80:
                    player_x +=20
            if event.key == pygame.K_SPACE:
                if gameover:
                    gameover =False
                    sc=0
                    fps=30
                    oppenent_one_x=in_oppenent_one_x
                    oppenent_one_y=in_oppenent_one_y
                    oppenent_two_x=in_oppenent_two_x
                    oppenent_two_y=in_oppenent_two_y
                    gameWindow.fill(white)
                    pygame.display.update()

    if not gameover:
        if oppenent_one_y<250:
            oppenent_one_y +=4

        else:
            oppenent_one_x = random.randrange(0, 100,20)
            oppenent_one_y = random.randint(0, 10)
            sc+=1

        if oppenent_two_y<250:
            oppenent_two_y +=6
        else:
            oppenent_two_x = random.randrange(0, 100, 20)
            oppenent_two_y = random.randint(0, 10)
            sc+=1
        
        if (sc+1)%20 == 0:
            fps+=1
        gameWindow.fill(white)
        player = pygame.draw.rect(gameWindow ,black,[player_x , player_y ,size,size])
        oppenent_one = pygame.draw.rect(gameWindow ,black,[oppenent_one_x,oppenent_one_y,size,size])
        oppenent_two = pygame.draw.rect(gameWindow, black, [oppenent_two_x, oppenent_two_y, size, size])
        scores(str(sc),5,5)
        # scores(sc)
        pygame.display.update()

        clock.tick(fps)
        if player.colliderect(oppenent_one) or player.colliderect(oppenent_two):
            gameover = True

    else :
        scores("GAME OVER",5,5)
        scores("PRESS SPACE", 5, 35)
        scores("TO RESTART", 5, 55)
        pygame.display.update()
        pass