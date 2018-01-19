# 基本的元素
#FPS = 30
playerIndex=0

BACKGROUND_PATH = './assets/sprites/background-black.png'
PIPE_PATH = './assets/sprites/pipe-green.png'
BASE_PATH = './assets/sprites/base.png'
PLAYER_PATH = (
        './assets/sprites/redbird-upflap.png',
        './assets/sprites/redbird-midflap.png',
        './assets/sprites/redbird-downflap.png'
)
SCREENWIDTH  = 288
SCREENHEIGHT = 512
BASEY = SCREENHEIGHT * 0.79
PIPEGAPSIZE = 100
PIPE_WIDTH = 10
PLAYER_HEIGHT = 5
IMAGES = {}
import pygame
from pygame.locals import *
from sys import exit #引入sys中exit函数
from itertools import cycle
import random

FPS = 30
FPSCLOCK = pygame.time.Clock()
PLAYER_INDEX_GEN = cycle([0, 1, 2, 1])

#初始化pygame
pygame.init()

#创建了窗口
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))

#设置窗口标题
pygame.display.set_caption("Flappy Bird")

#load图像，convert vs convert_alpha!
IMAGES['background'] = pygame.image.load(BACKGROUND_PATH).convert()
IMAGES['base'] = pygame.image.load(BASE_PATH).convert_alpha()
IMAGES['bird'] = (
    pygame.image.load(PLAYER_PATH[0]).convert_alpha(),
    pygame.image.load(PLAYER_PATH[1]).convert_alpha(),
    pygame.image.load(PLAYER_PATH[2]).convert_alpha(),
)
IMAGES['pipe'] = (
    pygame.transform.rotate(pygame.image.load(PIPE_PATH).convert_alpha(), 180),
    pygame.image.load(PIPE_PATH).convert_alpha()
)

PIPE_WIDTH = IMAGES['pipe'][0].get_width()
PIPE_HEIGHT = IMAGES['pipe'][0].get_height()

# 小鸟坐标初始化
x = 1/2 * SCREENWIDTH
y = 1/2 * SCREENHEIGHT
move_x = 0
move_y = 0
flap  = 0 # 扑腾的状态


def getRandomPipe():
    """returns a generated pipe"""
    # y of gap between upper and lower pipe
    gapYs = [10, 40, 60, 90, 120, 150, 190, 240]
    index = random.randint(0, len(gapYs)-1)
    gapY = gapYs[index]

    gapY += int(BASEY * 0.2)
    pipeX = SCREENWIDTH + 10

    return [
        {'x': pipeX, 'y': gapY - PIPE_HEIGHT},  # upper pipe
        {'x': pipeX, 'y': gapY + PIPEGAPSIZE},  # lower pipe
    ]


pipeVelX = -4
playerVelY    =  0    # player's velocity along Y, default same as playerFlapped
playerMaxVelY =  10   # max vel along Y, max descend speed
playerMinVelY =  -8   # min vel along Y, max ascend speed
playerAccY    =   2   # 1   # players downward accleration
playerFlapAcc =  -3   # -8   # players speed on flapping
playerFlapped = False # True when player flaps
playery = int((SCREENHEIGHT - PLAYER_HEIGHT) / 2)

newPipe1 = getRandomPipe()
upperPipes = [
            {'x': SCREENWIDTH, 'y': newPipe1[0]['y']},
        ]
lowerPipes = [
            {'x': SCREENWIDTH, 'y': newPipe1[1]['y']},
        ]

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # 让水管从右往左移动
    # 上下两根水管
    for uPipe, lPipe in zip(upperPipes, lowerPipes):
        uPipe['x'] += pipeVelX
        lPipe['x'] += pipeVelX



    # 按需生成新的水管，添加在队列的末尾
    if 0 < upperPipes[0]['x'] < 5:
        newPipe = getRandomPipe()
        upperPipes.append(newPipe[0])
        lowerPipes.append(newPipe[1])

    # 按需消灭水管，并从队列头排除
    if upperPipes[0]['x'] < -PIPE_WIDTH:
        upperPipes.pop(0)
        lowerPipes.pop(0)



    input_actions = random.randint(0,6)
    if input_actions % 3==0:
        playerVelY = playerFlapAcc
        playerFlapped = True


    # player's movement

    if playerVelY < playerMaxVelY and not playerFlapped:
        playerVelY += playerAccY
    if playerFlapped:
        playerFlapped = False
    
    playery += min(playerVelY, BASEY - playery - PLAYER_HEIGHT)

    if playery < 0:
        playery = 0


    x = 1/2*SCREENWIDTH
    #y = y - 2
    #if x>SCREENWIDTH:
    #    x=0
    #if y<0:
    #    y=SCREENHEIGHT
    # background
    SCREEN.blit(IMAGES['background'], (0,0))
    

    # 显示水管
    for uPipe, lPipe in zip(upperPipes, lowerPipes):
        SCREEN.blit(IMAGES['pipe'][0], (uPipe['x'],uPipe['y']))
        SCREEN.blit(IMAGES['pipe'][1], (lPipe['x'],lPipe['y']))
    
    SCREEN.blit(IMAGES['bird'][flap],(x,playery))
    
    flap = flap+1            
    
    if flap % 3 == 0:
        flap = 0  #next(PLAYER_INDEX_GEN)
    
    
    pygame.display.update()
    FPSCLOCK.tick(FPS)


