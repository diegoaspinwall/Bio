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

#keeps track of how many frames have passed
def step():
    data['drop']+=.1
    monkey.y += data['drop']
    data['frames'] += 1
    if data['frames']==100:
        wallspawn()

def wallspawn():
    print('hi')
    data['frames']=0


'''
def spriteflake():
    xpos = randint(0,COLS-1)
    data['flakes'].append(Sprite(snowBlock, (SIZE*xpos,-SIZE)))
    data['fallpos'][xpos] += 1
    data['stopflake'].append(data['fallpos'][xpos])
    print(data['stopflake'])
    

def step():
    data['frames'] += 1
    if data['frames'] == 10:
        spriteflake()
        data['frames'] = 0
    place = 0
    for flake in data['flakes']:
        flake.y += 1
        if flake.y == (COLS*SIZE-SIZE*(data['stopflake'][place])):
            data['flakes'].remove(flake)
            data['stopflake'].remove(data['stopflake'][place])
        place += 1
'''


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
    wall = RectangleAsset((CELL_SIZE,CELL_SIZE, LineStyle(1,brown), brown))
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox, (CELL_SIZE*(COLS/2-20),0))

    App().listenKeyEvent('keydown','space',moveUp)
    App().run(step)
