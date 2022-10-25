#TODO : YUMP

import pygame
from level import Level
from player import Player

running=True
stage=Level()
player=Player()
screen=pygame.display.set_mode((715,813))
keysDown=[False,False,False,False,False]
while running:
    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
            pygame.quit()
        if event.type==pygame.KEYDOWN or event.type==pygame.KEYUP:
            if event.key==pygame.K_UP:
                keysDown[0]=not keysDown[0]
            if event.key==pygame.K_DOWN:
                keysDown[1]=not keysDown[1]
            if event.key==pygame.K_RIGHT:
                keysDown[2]=not keysDown[2]
            if event.key==pygame.K_LEFT:
                keysDown[3]=not keysDown[3]
            if event.key==pygame.K_SPACE:
                keysDown[4]=not keysDown[4]
    player.update(stage.get_ladder(player.pos[0],player.pos[1]),keysDown,(screen.get_at((player.pos[0],player.pos[1])),screen.get_at((player.pos[0],player.pos[1]+3))))
    print(stage.get_ladder(player.pos[0],player.pos[1]))

    stage.showSelf(screen)
    player.showSelf(screen)
    pygame.display.update()
