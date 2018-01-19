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
IMAGES = {}
import pygame
from pygame.locals import *
from sys import exit #引入sys中exit函数
from itertools import cycle

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

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

  
    x = x + 3
    y = y - 2
    if x>SCREENWIDTH:
        x=0
    if y<0:
        y=SCREENHEIGHT
    # background
    SCREEN.blit(IMAGES['background'], (0,0))
    SCREEN.blit(IMAGES['pipe'][0], (0,0))
    SCREEN.blit(IMAGES['pipe'][1], (0,SCREENHEIGHT-PIPE_HEIGHT))
    SCREEN.blit(IMAGES['bird'][flap],(x,y))
    
    flap = flap+1            
    
    if flap % 3 == 0:
        flap = 0  #next(PLAYER_INDEX_GEN)
    
    
    pygame.display.update()
    FPSCLOCK.tick(FPS)

    #刷新一下画面

