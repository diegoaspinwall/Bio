#Diego Aspinwall
#6-10-18
#flappy.py

from ggame import *
from random import *

#constants
ROWS = 30
COLS = 40
CELL_SIZE = 20

#moves monkey up
def moveUp(event):
    if monkey.y > 0:
        monkey.y -= CELL_SIZE

#keeps track of how many frames have passed
def step():
    data['drop']+=.2
    monkey.y += data['drop']
    data['frames'] += 1
    if data['frames'] == 50:
        print('hi')
        data['drop']=0
        data['frames']=0

#runs the game
if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    data['frames'] = 0
    data['drop'] = 0
    
    blue = Color(0x6666ff,1)
    brown = Color(0x8B4513,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE, LineStyle(1,blue),blue)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown), brown)
    
    Sprite(jungleBox)
    monkey = Sprite(monkeyBox, (CELL_SIZE*(COLS/2),0))

    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().run(step)
