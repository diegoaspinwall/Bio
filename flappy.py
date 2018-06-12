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
    #makes fall speed up
    monkey.y += data['drop']
    data['frames'] += 1
    if data['frames']%200 == 0:
        #print(data['hitspot'])
        wallspawn()
        #spawns wall
        #print(data['hitspot'])
    for indwall in data['walls']:
        indwall.x -= 3
        #moves walls
    for indwall in data['walls']:
        if len(data['hitspot']) > 2:
            data['hitspot'].remove(data['hitspot'][0])
            #deletes hitspots that passed from corresponding walls
        if indwall.x < (-2)*CELL_SIZE:
            data['walls'].remove(indwall)
            #deletes walls out of picture
    if data['frames'] > 450:
        if data['frames']%200 == 100:
            print('hi')

def wallspawn():
    height = randint(5,(ROWS-10))
    data['walls'].append(Sprite(RectangleAsset(2*CELL_SIZE,height*CELL_SIZE, LineStyle(1,brown), brown), (COLS*CELL_SIZE,0)))
    data['walls'].append(Sprite(RectangleAsset(2*CELL_SIZE,(ROWS-(height+5))*CELL_SIZE, LineStyle(1,brown), brown), (COLS*CELL_SIZE,(height+5)*CELL_SIZE)))
    data['hitspot'].append(height)
    #creates new wall with random hole


#runs the game
if __name__ == '__main__':
    
    data = {}
    data['frames'] = 0
    data['drop'] = 0
    data['walls'] = []
    data['hitspot'] = []
    
    blue = Color(0x99ccff,1)
    brown = Color(0x8B4513,1)
    white = Color(0xffffff,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE, LineStyle(1,blue),blue)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,white), white)
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox, (CELL_SIZE*(COLS/2-20),0))

    App().listenKeyEvent('keydown','space',moveUp)
    App().run(step)
