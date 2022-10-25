#TODO : YUMP

import pygame
import random
from level import Level
from player import Player
from ennemies import Ennemies

running=True
stage=Level()
player=Player()
screen=pygame.display.set_mode((715,813))
keysDown=[False,False,False,False,False]

temps=0
barrel=[Ennemies(0)]

while running:
    pygame.time.Clock().tick(30)
    temps+=1

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
    
    
    for i in barrel:
        i.is_falling()

        i.move(screen)

        i.fall(screen)

        if i.etage%2==0:
            if temps%2==0:
                i.nb+=1
            if i.nb==5:
                i.nb=1

        else:
            if temps%2==0:
                i.nb-=1
            if i.nb==0:
                i.nb=4
        i.afficher(screen,temps)

        if i.etage==5 and i.x<=52:
            barrel.remove(i)

    pygame.display.update()
    
    if temps%60==0 and random.randint(0,1)==0:

        barrel.append(Ennemies(0))
        
