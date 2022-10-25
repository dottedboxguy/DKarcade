#TODO : finish YUMP

import pygame
def fruitTable(index):
    fruits=[100,200,350,500]
    return fruits[index]

class Player:
    def __init__(self):
        self.pos=[90,772]#à changer
        self.hp=5
        self.sprite=((pygame.image.load("sprites/mario-left.png"),pygame.image.load("sprites/run-left.png")),(pygame.image.load("sprites/mario-right.png"),pygame.image.load("sprites/run-right.png")),((pygame.image.load("sprites/marioClimb1.png"),pygame.image.load("sprites/marioClimb2.png"),)),((pygame.image.load("sprites/jump-left.png"),pygame.image.load("sprites/jump-right.png"))))# L U I G I, son nom c'est luigi, herewe here we go, c'est la fin de mario
        self.state=[1,0]#0 is left, 1 is right, 2 is climbing, animation state 0 or 1
        self.points=0
        self.hammerTime=0
        self.is_on_ladder=False
        self.hToGo=0
    def hasHammer(self):
        return not self.hammerTime==0
    def addPoints(self,fruit):
        self.points+=fruitTable(fruit)
    def reducePoints(self):
        self.points-=100
    def damage(self):
        self.hp-=1
    def get_x(self):
        return self.pos[0]
    def get_y(self):
        return self.pos[1]
    def get_stage(self):
        return self.pos[1]//2
    def move_horizontal(self,side):
        """
        side is 1 or -1
        """
        assert side==1 or side==-1, 'side must be 1 or -1, 1 is left, -1 is right'
        self.pos[0]+=9*side
    def move_vertical(self):
        if self.hToGo>0:
            self.pos[1]-=3
        self.hToGo-=3
    def got_hammer(self):
        self.hammerTime=300
    def update_hammer(self):
        self.hammerTime-=1
    def showSelf(self,screen):
        screen.blit(self.sprite[self.state[0]][self.state[1]],(self.pos[0],self.pos[1]-34))
    def switch_state(self,type):
        self.state[0]=type
    def switch_frame(self):
        self.state[1]=(self.state[1]+1)%2
    def update(self,ladder,keysDown,colors):
        is_on_ground = colors[1]==(255,6,64) or colors[1]==(166,6,6)
        if is_on_ground and (self.state[0]==3):
            self.switch_state(self.state[1])
        if (keysDown[4] or self.state[0]==3) and self.state[0]!=2:
            if self.hToGo<=0 and is_on_ground:
                self.hToGo=35
                self.switch_state(3)
            if self.state[0]!=2:
                if keysDown[3]:
                    self.move_horizontal(-1)
                    self.state[1]=0
                elif keysDown[2]:
                    self.move_horizontal(1)
                    self.state[1]=1
            if self.hToGo>0:
                self.move_vertical()
            else:
                self.fix_height(colors)
            
        else :
            if ladder[1] and keysDown[0] and self.hToGo<=0 and is_on_ground:
                self.switch_state(2)
                self.hToGo=ladder[2]+23
            elif self.hToGo>0:
                self.move_vertical()
                self.switch_frame()
            elif keysDown[3]:
                self.switch_state(0)
                self.move_horizontal(-1)
                self.switch_frame()
                self.fix_height(colors)
            elif keysDown[2]:
                self.switch_state(1)
                self.move_horizontal(1)
                self.switch_frame()
                self.fix_height(colors)
            else:
                self.state[1]=0
                self.fix_height(colors)

    def fix_height(self,colors):
        print(colors)
        if colors[0]==(255,6,64) or colors[0]==(166,6,6):
            self.pos[1]-=3
        elif colors[1]==(6,6,6) or colors[1]==(7,7,7) or colors[1]==(6,7,7) or colors[1]==(6,255,255):
            self.pos[1]+=3
        