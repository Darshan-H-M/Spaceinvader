import pygame
import random
import math
from pygame import mixer

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# initialize pygame
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#

pygame.init()

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
screen = pygame.display.set_mode((1020, 900)) 

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
pygame.display.set_caption("Space Invaders") 
icon = pygame.image.load("images/chicken.png")  
pygame.display.set_icon(icon) 

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# background image
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
background = pygame.image.load("background Images/level1.jpg")
background2 = pygame.image.load("background Images/level2.jpg")
background3 = pygame.image.load("background Images/level4.jpg")
background4 = pygame.image.load("background Images/level1.jpg")
background5 = pygame.image.load("background Images/level3.jpg")

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
mixer.music.load("music/background.wav")
mixer.music.play(-1)  
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# player
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
playerimg = pygame.image.load("images/spaceship123.png")
playerimg2 = pygame.image.load("images/spaceship lvl2.png")
playerimg3 = pygame.image.load("images/spaceship lvl3.png")
playerimg4 = pygame.image.load("images/spaceship lvl4.png")
playerimg5 = pygame.image.load("images/spaceship lvl5.png")
playerx = 510
playery = 810
playerx_change = 0
playery_change = 0

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# enemy
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#

enemyimg = []
enemyx = []
enemyy = []
enemyx_change = []
enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load("images/alien.png"))
    enemyimg.append(pygame.image.load("images/enemy1.png"))
    enemyimg.append(pygame.image.load("images/enemy2.png"))
    enemyimg.append(pygame.image.load("images/silly.png"))
    enemyimg.append(pygame.image.load("images/space-ship.png"))
    enemyimg.append(pygame.image.load("images/shocked.png"))
    enemyx.append(random.randint(0, 956))  
    enemyy.append(random.randint(90, 180)) 
    enemyx_change.append(0.9)
    enemyy_change.append(45)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# bullet
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#

bulletimg = pygame.image.load("images/bullet_img2.png")
bulletimg2 = pygame.image.load("images/bullets.png")
bulletimg3 = pygame.image.load("images/rocket.png")
bulletimg4 = pygame.image.load("images/bullet4.png")
bulletimg5 = pygame.image.load("images/bullet5.png")
bulletx = 0
bullety = 810
bulletx_change = 0
bullety_change = 8
bullety_change2 = 8
bullety_change3 = 8
bullet_state = "ready"


# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
def game_over():
    gameOver = pygame.font.Font("freesansbold.ttf", 64)
    game = gameOver.render("GAME OVER", True, (0, 255, 0))  
    screen.blit(game, (325, 350))
    gameOver_sound = mixer.Sound("music/gameover.wav")  
    gameOver_sound.play(0)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
def player(a,x, y):
    screen.blit(a, (x, y))  



def enemy(x, y, i):
    screen.blit(enemyimg[i], (x, y))  


def fire_button(a,x, y):  
    global bullet_state
    bullet_state = "fire"
    screen.blit(a, (x + 16, y + 20))


def explosions(a,x,y):
    exp = pygame.image.load(a)
    screen.blit(exp,(x,y))

def is_collision(enemyx, enemyy, bulletx, bullety):
    distance = math.sqrt((math.pow(enemyx - bulletx, 2)) + (math.pow(enemyy - bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# GAME LOOP
# -------------------------------------------------------------------------------------------------------------------------------------------------------------#

running = True

# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
# scoreboard
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textx = 10
texty = 10


# -------------------------------------------------------------------------------------------------------------------------------------------------------------#
def showscore(x, y):
    score1 = font.render("Score: " + str(score), True, (0, 255, 0))  
    screen.blit(score1, (x, y))
def levels(x, y):
    level = 1
    if score > 100:
        level += 4
        level = font.render(f"Level: {level} ", True, (0, 255, 0)) 
        screen.blit(level, (x, y))
    elif score >= 50 and score < 100:
        level += 3
        level = font.render(f"Level: {level} ", True, (0, 255, 0))  
        screen.blit(level, (x, y))
    elif score > 30 and score <= 50:
        level += 2
        level = font.render(f"Level: {level} ", True, (0, 255, 0)) 
        screen.blit(level, (x, y))
    elif score > 10 and score <= 30:
        level += 1
        level = font.render(f"Level: {level} ", True, (0, 255, 0)) 
        screen.blit(level, (x, y))
    else:
        if score >= 0 and score <= 10:
            level = font.render(f"Level: {level} ", True, (0, 255, 0)) 
            screen.blit(level, (x, y))



while running:
    screen.fill((0, 0, 0))
    if score >= 0 and score <=10:
        screen.blit(background, (0, 0))
        player(playerimg,playerx, playery)  
    elif score > 10 and score <= 30:
        screen.blit(background2, (0, 0))
        player(playerimg2,playerx, playery)
    elif score>30 and score <= 50:
            screen.blit(background3, (0, 0))
            player(playerimg3,playerx, playery)
    elif score>50 and score <= 100:
            screen.blit(background4, (0, 0))
            player(playerimg4,playerx, playery)
    else:
        if score > 100:
            screen.blit(background5, (0, 0))
            player(playerimg5,playerx, playery)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            running = False
        # directions------
        if event.type == pygame.KEYDOWN:
            # print("key activated")
            if event.key == pygame.K_LEFT:
                # print("left key")
                playerx_change = -1.5
                if score >= 10 and score < 30:
                    playerx_change = -2.0
                elif score >= 30:
                    playerx_change = -2.5


            if event.key == pygame.K_RIGHT:
                # print("Right key")
                playerx_change = 1.5
                if score >= 10 and score < 30:
                    playerx_change = 2.0
                elif score >= 30:
                    playerx_change = 2.5




            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound("music/bullet.wav")
                    bullet_sound.play()
                    bulletx = playerx
                    fire_button(bulletimg,bulletx, bullety)

                    if score >= 10 and score <= 30:
                        bulletx = playerx
                        fire_button(bulletimg2,bulletx, bullety)
                        bullet_sound = mixer.Sound("music/bullet3.wav")
                        bullet_sound.play()

                    elif score > 30 and score<= 50:
                        bulletx = playerx
                        fire_button(bulletimg3,bulletx, bullety)
                        bullet_sound = mixer.Sound("music/bullet2.wav")
                        bullet_sound.play()
                    elif score > 50 and score<= 100:
                        bulletx = playerx
                        fire_button(bulletimg4,bulletx, bullety)
                        bullet_sound = mixer.Sound("music/bullet2.wav")
                        bullet_sound.play()
                    else:
                        if score > 100:
                            bulletx = playerx
                            fire_button(bulletimg3, bulletx, bullety)
                            bullet_sound = mixer.Sound("music/bullet2.wav")
                            bullet_sound.play()

        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # player movement
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
    playerx += playerx_change
    if playerx <= 0:
        playerx = 0
    elif playerx >= 956:
        playerx = 956

    playery -= playery_change
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # enemy movement
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
    for i in range(num_of_enemies):
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
        # game over
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
        if enemyy[i] > 710:
            for j in range(num_of_enemies):
                enemyy[j] = 1000
            game_over()
            break

        enemyx[i] += enemyx_change[i]
        if enemyx[i] <= 0:
            enemyx_change[i] = 0.9
            enemyy[i] += enemyy_change[i]
        elif enemyx[i] >= 956:
            enemyx_change[i] = -0.9
            enemyy[i] += enemyy_change[i]
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
        # collision
        # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
        collision = is_collision(enemyx[i], enemyy[i], bulletx, bullety)
        if collision:
            bullet_sound = mixer.Sound("music/explosion.wav")
            bullet_sound.play()
            if score > 100:
                explosions("images/explosion 3.png", enemyx[i], enemyy[i])
            elif score > 50 and score <=100:
                explosions("images/explosion2.png",enemyx[i], enemyy[i])
            else:
                if score > 30 and score <= 50:
                    explosions("images/explosion img.png", enemyx[i], enemyy[i])

            bullety = 810
            bullet_state = "ready"
            enemyx[i] = random.randint(0, 956)
            enemyy[i] = random.randint(90, 180)
            score += 1

        if collision:
            if score > 100:
                score += 4
            elif score > 50 and score <=100:
                score += 3
            elif score > 30 and score <= 50:
                score += 2
            else:
                if score >= 10 and score <= 30:
                    score += 1


        enemy(enemyx[i], enemyy[i], i)
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
    # bullet movement
    # -------------------------------------------------------------------------------------------------------------------------------------------------------------#
    if bullet_state == "fire":
        if score > 100:
            fire_button(bulletimg5, bulletx, bullety)
            bullety -= bullety_change3
        elif score > 50 and score <= 100:
            fire_button(bulletimg4, bulletx, bullety)
            bullety -= bullety_change3
        elif score > 30 and score <= 50:
            fire_button(bulletimg3, bulletx, bullety)
            bullety -= bullety_change3
        elif score >= 10 and score <= 30:
            fire_button(bulletimg2,bulletx, bullety)
            bullety -= bullety_change2
        if score < 10:
            fire_button(bulletimg,bulletx, bullety)
            bullety -= bullety_change
        if bullety <= 0:
            bullety = 810
            bullet_state = "ready"

    showscore(textx, texty)
    levels(890,10)
    pygame.display.update()  
