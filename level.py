import pygame
from random import randint
class Level():
    def __init__(self):
        self.sprite=pygame.image.load("sprites/level.png")
        self.ladders=(((294,False,60),(580,True,47)),((127,True,48),(246,False,60),(532,False,95)),((222,False,90),(365,True,72),(580,False,48)),((127,True,48),(318,False,71)),((270,False,80),(380,True,47)))
    def get_ladder(self,x,y):
        "takes x and y as screen coordinates, returns a tuple containing if the entity's pos is hitting a ladder, if the ladder is broken and the size of the ladder"
        etage=-((y-200)//100)
        for ladder in self.ladders[etage]:
            if x>ladder[0]-6 and x<ladder[0]+6 :
                return (True,ladder[1],ladder[2])
        return (False,False,0)
    def showSelf(self, screen):
        screen.blit(self.sprite,(0,0))