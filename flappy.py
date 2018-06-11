#Diego Aspinwall
#6-10-18
#flappy.py

from ggame import *
from random import *

#constants
ROWS = 30
COLS = 55
CELL_SIZE = 20

#moves monkey up
def moveUp(event):
    if monkey.y > 10:
        data['drop'] = -5

def step():
    data['drop']+=.1
    #makes fall quicker
    monkey.y += data['drop']
    data['frames'] += 1
    if data['frames']==200:
        wallspawn()
        #spawns wall
        #print(data['walls'])
    for indwall in data['walls']:
        indwall.x -= 3
        #moves walls
        if indwall.x< (-2)*CELL_SIZE:
            data['walls'].remove(indwall)
        #deletes walls out of picture

def wallspawn():
    data['frames']=0
    height = randint(5,(ROWS-10))
    data['walls'].append(Sprite(RectangleAsset(2*CELL_SIZE,height*CELL_SIZE, LineStyle(1,brown), brown), (COLS*CELL_SIZE,0)))
    data['walls'].append(Sprite(RectangleAsset(2*CELL_SIZE,(ROWS-(height+5))*CELL_SIZE, LineStyle(1,brown), brown), (COLS*CELL_SIZE,(height+5)*CELL_SIZE)))
    #creates new wall


#runs the game
if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    data['frames'] = 0
    data['drop'] = 0
    data['walls'] = []
    
    blue = Color(0x6666ff,1)
    brown = Color(0x8B4513,1)
    white = Color(0xffffff,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE, LineStyle(1,blue),blue)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,white), white)
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox, (CELL_SIZE*(COLS/2-20),0))

    App().listenKeyEvent('keydown','space',moveUp)
    App().run(step)
