# 基本的元素
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

#初始化pygame,为使用硬件做准备
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
    pygame.transform.rotate(
        pygame.image.load(PIPE_PATH).convert_alpha(), 180),
    pygame.image.load(PIPE_PATH).convert_alpha(),
)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
        if event.type == KEYDOWN:
            if event.key == pygame.K_q:
                exit()

    # background
    SCREEN.blit(IMAGES['background'], (0,0))
    SCREEN.blit(IMAGES['pipe'][0], (0,0))


    pygame.display.update()
    #刷新一下画面
