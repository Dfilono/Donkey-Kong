import pygame
import sys
import random
from pygame.locals import *

# Define color calues (R, G, B)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (0, 200, 255)
YELLOW = (255, 255, 0)
PURPLE = (170, 0, 225)
colors = [GREEN, RED, LIGHTBLUE, YELLOW, PURPLE, BLACK]

# declaring glocal variables
# score
leaderboard = []
score = 0
highScore = 0
levelNum = 0
difficulty = 0

# screen bounds
leftBoundY = [541, 341]
rightBoundY = [638, 438, 244]

# booleans
replay = True
pressed = False
climbDone = False
introOver = False
startOver = False
startOutput = False
gameStart = False
throwBarrel = False
jumpLeft, jumpRight, jumpUp = False, False, False
hit = False
death = False
gameOver = False
winGame = False
winLevel = False
scoreWin = False
winGameOut = False
winGameDone = False

# strings
option = 'top'
direction = 'right'

# platform positions
platformsX = [55, 55, 51, 60, 56, 56, 56]
platformsY = [9, 10, 8, 9, 11, 9, 9, 11]
platformsNum = 0
platformsInclineX = [100, 140, 190, 240, 280, 330, 380, 430, 480, 530, 570, 620, 670, 720]
inclineCount = 0

# ladders
ladderX1 = [295, 605, 295, 345, 345, 150, 245, 385, 600, 600, 245, 150, 265, 265, 315, 555, 555, 600, 440, 320]
ladderX2 = [305, 610, 310, 350, 350, 160, 255, 400, 610, 610, 255, 160, 280, 280, 325, 565, 565, 610, 450, 335]
ladderY1 = [710, 635, 617, 610, 526, 538, 522, 423, 506, 435, 414, 338, 409, 332, 309, 314, 417, 241, 154, 232]
ladderY2 = [720, 705, 657, 620, 571, 608, 532, 523, 511, 475, 464, 408, 414, 382, 329, 369, 432, 311, 232, 272]
fullLadderUp = [False, True, True, False, True, True, False, True, False, True, True, True, False, True, False, True, False, True, True, True]
fullLadderDown = [True, True, False, True, False, True, True, True, True, False, False, True, True, False, True, False, True, True, True, False]

# donkey kong
dkClimb = 0
climbCount = 15
dkJumpX = 378
dkJumpY = 172
dkJumpYNum = 0

# player
playerX = 150
playerY = 720
addJump = -7
jumpCount = 0
jumpPoint = 0
deathCount = 0
lives = 2

# barrels
barrelX = []
barrelY = []
throwCountdown = 0
barrelDirection = []
fall = []
fallCount = []
barrelLeft = []
barrelRight = []
barrelLadderX = [320, 610, 560, 280, 160, 250, 400, 610, 350, 160, 300, 610]
barrelLadderY1 = [243, 252, 326, 270, 350, 428, 437, 449, 535, 547, 627, 645]
barrelLadderY2 = [343, 322, 446, 344, 420, 538, 527, 519, 625, 617, 727, 715]
barrelAdjust = [-2, 1, -1, 4, 2, 3, 5, 1, 5, 1, 4, 1]

# confetti
confettiX = []
confettiY = []
confettiRadius = []
confettiSpeed = []
confettiColor = []

# Define images
# menus
title = pygame.image.load("images/title-screen.png")
start = pygame.image.load("images/start.png")
winScreen = pygame.image.load("images/win-screen.png")
gameOverScreen = pygame.image.load("images/game-over-screen.png")
selectIcon = pygame.image.load("images/select-icon.png")

# UI
life = pygame.image.load("images/life.png")
brokenHeart = pygame.image.load("images/broken-heart.png")
fullHeart = pygame.image.load("images/full-heart.png")

# Level
withLadder = pygame.image.load("images/withLadder.png")
platform0 = pygame.image.load("images/platform0.png")
platform1 = pygame.image.load("images/platform1.png")
platform2 = pygame.image.load("images/platform2.png")
platform3 = pygame.image.load("images/platform3.png")
platform4 = pygame.image.load("images/platform4.png")
platform5 = pygame.image.load("images/platform5.png")
platform6 = pygame.image.load("images/platform6.png")
platforms = [platform0, platform1, platform2, platform3, platform4, platform5, platform6]
level = pygame.image.load("images/level.png")

# Numbers
blue0 = pygame.image.load("images/blue0.png")
blue1 = pygame.image.load("images/blue1.png")
blue2 = pygame.image.load("images/blue2.png")
blue3 = pygame.image.load("images/blue3.png")
blue4 = pygame.image.load("images/blue4.png")
blue5 = pygame.image.load("images/blue5.png")
blueNumbers = [blue0, blue1, blue2, blue3, blue4, blue5]
white0 = pygame.image.load("images/white0.png")
white1 = pygame.image.load("images/white1.png")
white2 = pygame.image.load("images/white2.png")
white3 = pygame.image.load("images/white3.png")
white4 = pygame.image.load("images/white4.png")
white5 = pygame.image.load("images/white5.png")
white6 = pygame.image.load("images/white6.png")
white7 = pygame.image.load("images/white7.png")
white8 = pygame.image.load("images/white8.png")
white9 = pygame.image.load("images/white9.png")
whiteNumbers = [white0, white1, white2, white3, white4, white5, white6, white7, white8, white9]

# Player
playerLeft = pygame.image.load("images/player-left.png")
playerRight = pygame.image.load("images/player-right.png")
playerRunLeft = pygame.image.load("images/run-left.png")
playerRunRight = pygame.image.load("images/run-right.png")
playerJumpLeft = pygame.image.load("images/jump-left.png")
playerJumpRight = pygame.image.load("images/jump-right.png")
playerClimb1 = pygame.image.load("images/playerClimb1.png")
playerClimb2 = pygame.image.load("images/playerClimb2.png")
dead = pygame.image.load("images/dead.png")
playerImage = playerRight

# Princess
pricnessHelp = pygame.image.load("images/princess-help.png")
princessStill = pygame.image.load("images/princess-still.png")

# Donkey Konh
dkUp1 = pygame.image.load("images/DK_up1.png")
dkUp2 = pygame.image.load("images/DK_up2.png")
dkEmptyClimb1 = pygame.image.load("images/dkClimbEmpty1.png")
dkEmptyClimb2 = pygame.image.load("images/dkClimbEmpty2.png")
dkForward = pygame.image.load("images/dkForward.png")
dkLeft = pygame.image.load("images/dkLeft.png")
dkRight = pygame.image.load("images/dkRight.png")
dkDefeat = pygame.image.load("images/dk-defeat.png")
dkImage = dkForward

# Barrels
barrelStack = pygame.image.load("images/barrel-stack.png")
barrelDown = pygame.image.load("images/barrel-down.png")
barrel1 = pygame.image.load("images/barrel1.png")
barrel2 = pygame.image.load("images/barrel2.png")
barrel3 = pygame.image.load("images/barrel3.png")
barrel4 = pygame.image.load("images/barrel4.png")
barrelSequence = [barrel1, barrel2, barrel3, barrel4]
barrelPic = []

# Frame Rate
clock = pygame.time.Clock()

# Declare 400 confetti pieces
for i in range(0, 400):
    # chooses rancom x value and appends it to list
    x = random.randint(0, 800)
    confettiX.append(x)

    # chooses rancom Y value and appends it to list
    y = random.randint(-500, -100)
    confettiY.append(y)

    # chooses random radius and appends it to list
    r = random.randint(1, 4)
    confettiRadius.append(r)

    # chooses random speed and appends it to list
    s = random.randint(5, 20)
    confettiSpeed.append(s)

    # chooses random color and appends it to list
    color = random.randint(0, 5)
    confettiColor.append(colors[color])


# instructions output into console
def instructions():
    print ("Donkey Kong has kidnapped the Princess!")
    print ("You must now save her by climbing all the way")
    print ("up the structure to the platform where she is being held.")
    print ("You will have three lives, and you get points by rescuing")
    print ("the Princess and jumping over barrels.")
    print ("To win, save her 5 times or get a score of 999999 or over.")
    print ("Use the arrow keys to move, and press the space to jump.")
    print ("In the menus, use the up and down keys to choose your option")
    print ("and the return key to select it.")
    print ("GOOD LUCK!")

# finds the high score and adds current user's score to leaderboard
def highestScore():
    # adds user's score
    leaderboard = score

    #orting the scores for least to most
    scores = leaderboard.values()

# collide checks whether or not the plaer has collided with a barrel
def collide() -> bool:
    global hit

    for i in range(len(barrelX)):
        if playerX + 20 >= barrelX[i] and playerX <= barrelX[i] + 26 and playerY + 30 >= barrelY[i] and playerY <= barrelY[i] + 20:
            hit = True

    return hit

# checks whether or not there is a ladder at location
def ladderCheck():
    global playerY

    upLadder = False
    downLadder = False
    moveSides = True

    for i in range(len(ladderX1)):
        if playerX >= ladderX1[i] and playerX <= ladderX2[i] and playerY >= ladderY1[i] and playerY <= ladderY2[i]:
            downLadder = True
            upLadder = True
            moveSides = False

            if playerY == ladderY1[i]:
                upLadder = False

                if fullLadderUp[i]:
                    moveSides = True

            if playerY == ladderY2[i]:
                downLadder = False

                if fullLadderDown[i]:
                    moveSides = True

        if upLadder or downLadder:
            break
    return upLadder, downLadder, moveSides

# moves player up incline when walking/jumping on platform
def incline(y, x, direction, object):
    global inclineCount

    if y <= 720 and y >= 657:
        startNum = 6
        endNum = len(platformsInclineX) - 1
        move = 3

    elif (y <= 638 and y >= 553) or (y <= 353 and y >= 438):
        startNum = 0
        endNum = len(platformsInclineX) - 2
        move = -3

    elif (y <= 541 and y >= 456) or (y <= 341 and y >= 256):
        startNum = 1
        endNum = len(platformsInclineX) - 1
        move = 3

    elif (y <= 245 and y >= 149):
        startNum = 8
        endNum = len(platformsInclineX) - 2
        move = -3

    else:
        startNum = 0
        endNum = 0
        move = 0

    for i in range(startNum, endNum):
        if x == platformsInclineX[i]:
            if (jumpLeft or jumpRight) and object == "player":
                inclineCount += 1
            else:
                if direction == "right":
                    y -= move
                elif direction =="left":
                    y += move

    if(jumpLeft or jumpRight) and object == "player":
        return move
    else:
        return y
    
# checks all of player's and barrel's bounds
def bounds(x, y):
    left = True
    right = True

    if x <= 105 and x>= 96:
        for i in range(len(leftBoundY)):
            if y <= leftBoundY[i] and y>= leftBoundY[i] - 49:
                left = False

    elif x>= 660 and x <= 669:
        for i in range(len(rightBoundY)):
            if y <= rightBoundY[i] and y >= rightBoundY[i] - 49:
                right = False

    return left, right

def introScene():
    if dkClimb <= 390:
        screen.blit(withLadder, (48,0))

        if dkClimb % 30 == 0:
            screen.blit(dkUp2, (350, 660 - dkClimb))

        else:
            screen.blit(dkUp1, (370, 660 - dkClimb))

    elif dkClimb > 390 and dkClimb <= 580:
        screen.blit(platform0, (55, 9))
        screen.blit(dkUp2, (350, 660 - dkClimb))

    if climbDone:
        screen.blit(platforms[platformsNum], (platformsX[platformsNum], platformsY[platformsNum]))
        princess(princessStill)
        screen.blit(dkForward, (dkJumpX, dkJumpY))

def startScreen():
    screen.blit(start, (48, 0))

def background():
    screen.blit(level, (31, -14))
    screen.blit(barrelStack, (60, 188))

def dk():
    screen.blit(dkImage, (130, 176))

def player():
    screen.blit(playerImage, (playerX, playerY))

def princess(princessImg):
    screen.blit(princessImg, (335, 133))

def barrel():
    for i in range(len(barrelPic)):
        screen.blit(barrelPic[i], (barrelX[i], barrelY[i]))

def playerLives():
    for i in range(lives):
        screen.blit(life, (60 + i * 20, 100))

def levelNumber():
    for i in range(len(blueNumbers)):
        if levelNum / 10 == i:
            screen.blit(blueNumbers[i], (611, 86))

        if levelNum % 10 == i:
            screen.blit(blueNumbers[i], (635, 86))

def playerScores(scoreType, scoreX, scoreY):
    tempScore = str(scoreType)
    numZero = 6 - len(tempScore)

    for i in range(numZero):
        screen.blit(whiteNumbers[0], (scoreX, scoreY))
        scoreX += 24

def win():
    background()
    screen.blit(playerLeft, (440, 150))

    if dkClimb <= 30:
        princess(princessStill)
        screen.blit(fullHeart, (386, 130))
    else:
        screen.blit(brokenHeart, (387, 130))

    
    if winGame == False:
        if dkClimb % 30 == 0:
            screen.blit(dkImage1, (240 - moveOver1, 160 - dkClimb))
        else:
            screen.blit(dkImage2, (240 - moveOver2, 160 - dkClimb))
    else:
        dk()

def end(endScreen):
    screen.blit(endScreen, (0, 30))

    if option == "bottom":
        screen.blit(selectIcon, (270, 640))
    else:
        screen.blit(selectIcon, (270, 575))

def confetti():
    for i in range(0, 400):
        pygame.draw.cricle(screen, confettiColor[i], (confettiX[i], confettiY[i]), confettiRadius[i], 0)

def redraw_screen():
    global climbDone
    global gameStart
    global gameOver
    global winGameDone
    global startOver
    global startOutput

    screen.fill(BLACK)

    if gameOver:
        end(gameOverScreen)
        playerScores(score, 388, 387)
        playerScores(highScore, 485, 445)

    elif winGame:
        if winGameOut:
            win()
            playerLives()
            levelNumber()

            playerScores(score, 88, 48)
            playerScores(highScore, 327, 40)

        elif winGameDone:
            end(winScreen)
            confetti()
            playerScores(score, 388, 387)
            playerScores(highScore, 485, 445)

    else:
        if pressed == False:
            screen.blit(title, (54, 18))
        
        elif pressed and introOver == False:
            introScene()
            playerLives()

        elif introOver == True and gameStart == False:
            startScreen()
            playerLives()
            startOutput = True
            startOver = True

        elif (gameStart and winLevel == False) or death:
            background()
            dk()
            player()
            princess(pricnessHelp)
            playerLives()

            if scoreWin == False and death == False:
                barrel()

        elif winLevel:
            win()
            playerLives()

        levelNumber()
        playerScores(score, 88, 40)
        playerScores(highScore, 327, 40)

    pygame.display.update()

instructions()

pygame.init()
walk = pygame.mixer.Sound("sounds/walking.wav")
jump = pygame.mixer.Sound("sounds/jump.wav")
intro = pygame.mixer.Sound("sounds/intro1.wav")
deathSound = pygame.mixer.Sound("sounds/death.wav")
bac = pygame.mixer.music.load("sounds/bacmusic.wav")

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Donkey Kong')

inPlay = True
pygame.mixer.music.play(-1)

while replay:
    while inPlay:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        if pressed == True and climbDone == False:
            if dkClimb == 0:
                levelNum += 1
            
            if dkClimb == 390:
                pygame.time.delay(500)

            if dkClimb >= 560:
                climbCount = -20

            if dkClimb != 510 or climbCount != -20:
                dkClimb += climbCount

            else:
                climbDone = True

        elif climbDone and introOver == False:
            if platformsNum <= 6:
                if dkJumpY == 152:
                    dkJumpYNum = 10

                if dkJumpY == 172:
                    dkJumpYNum = -10

                    platformsNum += 1

                dkJumpX -= 12

                if platformsNum != 6:
                    dkJumpY += dkJumpYNum
                else:
                    introOver = True
                    pygame.time.delay(1000)

        if gameStart:
            if scoreWin == False and winLevel == False:
                hit = collide()

            moveLeft, moveRight = bounds(playerX, playerY)

            if hit == False:
                upLadder, downLadder, moveSides = ladderCheck()

                if playerY <= 154:
                    winLevel = True
                    dkClimb = -15
                    climbCount = 15
                    playerX = 150
                    playerY = 720
                    playerImage = playerRight

                if jumpLeft or jumpRight or jumpUp:
                    jumpCount += 1
                    playerY += addJump

                    if jumpCount == 7:
                        addJump = 7

                    if jumpCount == 14:
                        if jumpPoint == 1:
                            score += 100

                        if direction == "right":
                            playerImage = playerRight
                            playerY += move*inclineCount
                        else:
                            playerImage == playerLeft
                            playerY += move*inclineCount

                        addJump = -7
                        jumpCount = 0
                        jumpPoint = 0
                        inclineCount = 0
                            
                        jumpLeft = False
                        jumpRight = False
                        jumpUp = False

                    if playerX != 60 and playerX != 710 and (playerX != 320 or playerY >= 232):
                        move = incline(playerY, playerX, direction, "player")

                        if jumpLeft and moveLeft:
                            playerX -= 5
                        elif jumpRight and moveRight:
                            playerX += 5

                    for i in range(len(barrelX)):
                        if playerX >= barrelX[i] and playerX <= barrelX[i] + 28 and playerY <= barrelY[i] - 23 and playerY >= barrelY - 65:
                            jumpPoint = 1

                if scoreWin == False:
                    for i in range(len(barrelPic)):
                        if barrelX[i] <= 31:
                            barrelX[i] = -30
                            barrelY[i] = -30

                        if fall[i] == False:
                            barrelLeft[i], barrelRight[i] = bounds([barrelX[i], barrelY[i] - 15])

                            if barrelLeft[i] == False or barrelRight[i] == False:
                                fall[i] = True

                        if (barrelY[i] <= 353 and barrelY[i] >= 317) or (barrelY[i] <= 452 and barrelY[i] >= 415) or (barrelY[i] <= 648 and barrelY[i] >= 611):
                            barrelDirection[i] = 'right'

                        elif (barrelY[i] <= 353 and barrelY[i] >= 317) or (barrelY[i] <= 550 and barrelY[i] >= 513) or (barrelY[i] <= 731 and barrelY[i] >= 709):
                            barrelDirection[i] = "left"

                        if barrelPic[i] != barrelDown:
                            if fall[i] == False:
                                if barrelDirection[i] == "right":
                                    barrelX[i] += 10
                                else:
                                    barrelX[i] -= 10

                                barrelY[i] = incline(barrelY[i] - 11, barrelX[i], barrelDirection[i], 'barrel')
                                barrelY[i] += 11

                            else:
                                fallCount[i] += 1

                                if barrelLeft[i] == False:
                                    barrelX[i] -= 5

                                elif barrelRight[i] == False:
                                    barrelX[i] += 5

                                barrelY[i] += 7

                                if fallCount[i] == 8:
                                    barrelY[i] += 6

                                    fallCount[i] = 0
                                    fall[i] = False
                                    barrelLeft[i] = True
                                    barrelRight[i] = True

                                if barrelPic[i] == barrelSequence[3]:
                                    barrelPic[i] = barrelSequence[0]

                                else:
                                    for j in range(len(barrelSequence) -1):
                                        if barrelPic[i] == barrelSequence[j]:
                                            barrelPic[i] = barrelSequence[j + 1]

                        else:
                            barrelY[i] += 10

                        for j in range(len(barrelLadderX)):
                            if barrelX[i] == barrelLadderX[j] and barrelY[i] == barrelLadderY1[j]:
                                barrelChoice = random.randint(0, 1)

                                if barrelChoice == 0:
                                    barrelPic[i] = barrelDown
                                    barrelX[i] -= 2

                            if barrelX[i] + 2 == barrelLadderX[j] and barrelY[i] == barrelLadderY2[j]:
                                barrelPic[i] = barrelSequence[0]
                                barrelX[i] += 2
                                barrelY[i] += barrelAdjust[j]

                        if throwBarrel == False:
                            dkChoice = random.randint(0, 50 - difficulty)

                            if dkChoice == 0:
                                dkImage = dkLeft
                                throwBarrel = True
                            else:
                                dkImage = dkForward
                                throwBarrel = False

                        if throwBarrel:
                            throwCountdown += 1

                            if throwCountdown == 20:
                                dkImage = dkRight
                                barrelX.append(250)
                                barrelY.append(243)
                                barrelDirection.append("right")
                                barrelPic.append(barrel1)
                                fall.append(False)
                                fallCount.append(0)
                                barrelLeft.append(True)
                                barrelRight.append(True)

                            if throwCountdown == 40:
                                throwCountdown = 0
                                dkImage = dkForward
                                throwBarrel = False

            else:
                if not pygame.mixer.get_busy():
                    pygame.mixer.Sound.play(deathSound)

                if death == False:
                    if deathCount == 0:
                        playerY += 10

                    deathCount += 1

                    if deathCount == 60:
                        death == True
                        deathCount = 0
                        lives -= 1

                    playerImage = dead

                else:
                    startOver = False
                    gameStart = False
                    throwBarrel = False
                    death = False
                    hit = False
                    jumpLeft = False
                    jumpRight = False
                    jumpUp = False
                    barrelX = []
                    barrelY = []
                    barrelPic = []
                    throwCountdown = 0
                    barrelDirection = []
                    fall - []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []
                    inclineCount = 0
                    jumpPoint = 0
                    playerX = 150
                    playerY = 720
                    addJump = -7
                    jumpCount = 0
                    direction = 'right'
                    playerImage = playerRight

                if lives < 0:
                    gameOver = True
                    highScore = highestScore()

        if score >= 999999:
            score = 999999
            scoreWin = True
            dkImage = dkDefeat

        if winLevel:
            if levelNum == 5 or scoreWin:
                if winGameDone == False:
                    dkImage = dkDefeat
                    winGameOut = True

                else:
                    for i in range(0, 400):
                        confettiY[i] += confettiSpeed[i]
                    highScore = highestScore()
                
                gameStart = False
                winGame = True

            else:
                dkClimb += climbCount

                if dkClimb == 15:
                    score += 250
                    pygame.time.delay(1000)

                if dkClimb <= 30:
                    dkImage1 = dkEmptyClimb1
                    dkImage2 = dkEmptyClimb2
                    moveOver1 = 0
                    moveOver2 = 0

                else:
                    dkImage1 = dkUp1
                    dkImage2 = dkUp2
                    moveOver1 = 13
                    moveOver2 = 35

                if dkClimb == 150:
                    winLevel = False
                    climbDone = False
                    introOver = False
                    startOver = False
                    gameStart = False
                    throwBarrel = False
                    hit = False
                    jumpLeft = False
                    jumpRight = False
                    jumpUp = False
                    barrelX = []
                    barrelY = []
                    barrelPic = []
                    barrelDirection = []
                    fall = []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []
                    dkClimb = 0
                    platformsNum = 0
                    climbCount = 15
                    inclineCount = 0
                    dkJumpX = 378
                    dkJumpY = 172
                    dkJumpYNum = 0
                    addJump = -7
                    jumpCount = 0
                    direction = 'right'

                    difficulty += 8

        pygame.event.get()
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            highScore = highestScore()
            inPlay = False
            replay = False

        if keys[pygame.K_SPACE]:
            pressed = True

            if not pygame.mixer.get_busy():
                pygame.mixer.Sound.play(intro)


        if (gameStart and jumpLeft == False and jumpRight == False and jumpUp == False and winLevel == False and hit == False) or gameOver or winGame:
            if keys[pygame.K_LEFT] and moveSides and (playerX != 320 or playerY > 232) and moveLeft and playerX != 60:
                playerY = incline(playerY, playerX, direction, 'player')

                if direction == 'left':
                    playerX -= 5

                if playerImage == playerLeft:
                    playerImage = playerRunLeft
                    
                    if not pygame.mixer.get_busy():
                        pygame.mixer.Sound.play(walk)

                else:
                    playerImage = playerLeft

                if keys[pygame.K_SPACE]:
                    jumpLeft = True
                    playerImage = playerJumpLeft
                    pygame.mixer.Sound.stop(walk)
                    pygame.mixer.Sound.play(jump)

                direction = 'left'

            elif keys[pygame.K_RIGHT] and moveSides and moveRight and playerX != 710:
                playerY = incline(playerY, playerX, direction, 'player')

                if direction == 'right':
                    playerX += 5
                
                if playerImage == playerRight:
                    playerImage = playerRunRight

                    if not pygame.mixer.get_busy():
                        pygame.mixer.Sound.play(walk)

                else:
                    playerImage = playerRight

                if keys[pygame.K_SPACE]:
                    jumpRight = True
                    playerImage = playerJumpRight
                    pygame.mixer.Sound.stop(walk)
                    pygame.mixer.Sound.play(jump)

                direction = 'right'

            elif not keys[pygame.K_LEFT] or not keys[pygame.K_RIGHT]:
                pygame.mixer.Sound.stop(walk)

            if keys[pygame.K_UP] and (upLadder or gameOver or winGame):
                if upLadder:
                    playerY -= 5

                    if playerImage == playerClimb1:
                        playerImage == playerClimb2

                    else:
                        playerImage = playerClimb1

                if gameOver or winGame:
                    option = 'top'

            if keys[pygame.K_DOWN] and (downLadder or gameOver or winGame):
                if upLadder:
                    playerY += 5

                    if playerImage == playerClimb1:
                        playerImage == playerClimb2

                    else:
                        playerImage = playerClimb1

                if gameOver or winGame:
                    option = 'bottom'

            if keys[pygame.K_SPACE] and jumpLeft == False and jumpRight == False and moveSides:
                jumpUp = True

                if direction == "right":
                    playerImage = playerJumpRight

                else:
                    playerImage = playerJumpLeft

            if keys[pygame.K_RETURN] and (gameOver or winGame):
                if option == 'top':
                    inPlay = False
                    winLevel = False
                    pressed = False
                    climbDone = False
                    introOver = False
                    gameStart = False
                    startOver = False
                    gameOver = False
                    throwBarrel = False
                    jumpLeft = False
                    jumpRight = False
                    jumpUp = False
                    winGame = False
                    winLevel = False
                    death = False
                    scoreWin = False
                    winGameDone = False
                    score = 0
                    levelNum = 0
                    dkClimb = 0
                    climbCount = 15
                    platformsNum = 0
                    dkJumpX = 378
                    dkJumpY = 172
                    dkJumpYNum = 0
                    playerX = 150
                    playerY = 720
                    addJump = -7
                    playerJumpCount = 0
                    lives = 2
                    difficulty = 0
                    barrelX = []
                    barrelY = []    
                    barrelPic = []
                    throwCountdown = 0
                    barrelDirection = []
                    fall = []
                    fallCount = []
                    barrelLeft = []
                    barrelRight = []

                elif option == 'bottom':
                    inPlay = False
                    replay = False
                
        clock.tick(30)
        pygame.display.update()

        if inPlay:
            redraw_screen()

        if startOutput:
            startOutput = False
            gameStart = True

        if winGameOut:
            winGameOut = False
            winGameDone = True

    pygame.quit()
pygame.quit
