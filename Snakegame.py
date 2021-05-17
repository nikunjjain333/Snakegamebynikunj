import pygame
import random
import os

pygame.mixer.init()
pygame.init()
# initializing Window size
s_w = 650
s_h = 600

# Creating game window
game_window = pygame.display.set_mode((s_w, s_h))
pygame.display.set_caption("Snake Game")

# Setting background Image

bimg1 = pygame.image.load("gameover.png")
bimg1 = pygame.transform.scale(bimg1,(s_w,s_h)).convert_alpha()

bimg2 = pygame.image.load("HeavenlyWanHornedviper-max-1mb.gif")
bimg2 = pygame.transform.scale(bimg2,(100,100)).convert_alpha()


pygame.display.update()

# Display score on the screen
font = pygame.font.SysFont(None,50)

def screentext(txt,color,x,y):
    scrtxt = font.render(txt, True, color)
    game_window.blit(scrtxt, [x,y])

def snake(game_window,color,snklst,size):
    for x,y in snklst:
        pygame.draw.circle(game_window, [51, 204, 51], [x,y], 7)

def welcome():
    game_exit = False
    while not game_exit:
        game_window.fill([0,0,0])
        game_window.blit(bimg2, (250,85))
        screentext("| Welcome to Snake Game |",[255,255,255],90,230)
        screentext("Press SpaceBar to Play", [255, 255, 255], 130, 290)
        screentext("Develop by: Nikunj", [255, 0, 0], 330, 563)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()

        pygame.display.update()
        clock.tick(60)

clock = pygame.time.Clock()
def gameloop():
    # game variables
    game_exit = False
    game_over = False
    fps = 60
    s_x = 100  # x position of snake
    s_y = 100  # y position of snake
    x_v = 0  # Initial velocity of snake in x direction
    y_v = 0  # initial velocity of snake in y direction
    fx = random.randint(10, s_w - 50)
    fy = random.randint(50, s_h - 50)
    score = 0
    snklst = []  # list of coordinates of snake
    snkln = 1  # initial length of snake


    if not os.path.exists("hiscore.txt"):
        with open("hiscore.txt", "w") as f:
            f.write("0")

    with open("hiscore.txt", "r") as f:
        high = f.read()
    while not game_exit:
        if game_over:
            with open("hiscore.txt", "w") as f:
                f.write(str(high))
            game_window.fill([230,255,238])
            game_window.blit(bimg1,(0,0))
            screentext("Press Enter To Continue..!",[255,255,255],100,430)
            screentext("HIGHSCORE: " + str(high),[255,255,255],185,350)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        x_v = 2
                        y_v = 0
                    if event.key == pygame.K_LEFT:
                        x_v = -2
                        y_v = 0
                    if event.key == pygame.K_UP:
                        y_v = -2
                        x_v = 0
                    if event.key == pygame.K_DOWN:
                        y_v = 2
                        x_v = 0
                    if event.key == pygame.K_a: # cheat code
                        score += 10
            s_x=s_x+x_v
            s_y=s_y+y_v
            if abs(s_x-fx)<6 and abs(s_y-fy)<6:
                pygame.mixer.music.load("game_boy_switch_on.mp3")
                pygame.mixer.music.play()
                score+=10
                fx = random.randint(20, s_w//2)
                fy = random.randint(20, s_h//2)
                snkln += 3
                if score > int(high):
                    high = score

            game_window.fill((230, 230, 230))

            snakehead = []
            snakehead.append(s_x)
            snakehead.append(s_y)
            snklst.append(snakehead)
            if len(snklst)>snkln:
                del snklst[0]

            if snakehead in snklst[:-1]:
                pygame.mixer.music.load("Windshield Hit With Bar.mp3")
                pygame.mixer.music.play()
                pygame.time.wait(500)
                game_over = True
                pygame.mixer.music.load("game_over_tune.mp3")
                pygame.mixer.music.play()


            if s_x < 0 or s_x > s_w or s_y < 40 or s_y > s_h:
                pygame.mixer.music.load("Windshield Hit With Bar.mp3")
                pygame.mixer.music.play()
                pygame.time.wait(500)
                game_over = True
                pygame.mixer.music.load("game_over_tune.mp3")
                pygame.mixer.music.play()

            snake(game_window,[0,0,0],snklst,7)
            pygame.draw.circle(game_window, [0,0,0], [fx, fy], 7)
            pygame.draw.line(game_window,[0,0,0],[0,20],[s_w,20],39)
            screentext("Score: " + str(score) + "                     HIGHSCORE: " + str(high), (255, 0, 0), 4, 4)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()