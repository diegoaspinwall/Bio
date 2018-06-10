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
    data['frames'] += 1
    if data['frames'] == 2000:
        print('hi)

#runs the game
if __name__ == '__main__':
    
    data = {}
    data['score'] = 0
    data['frames'] = 0
    
    blue = Color(0x000066,1)
    brown = Color(0x8B4513,1)
    yellow = Color(0xFFFF00,1)
    
    jungleBox = RectangleAsset(COLS*CELL_SIZE,ROWS*CELL_SIZE, LineStyle(1,blue),blue)
    monkeyBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,brown), brown)
    bananaBox = RectangleAsset(CELL_SIZE,CELL_SIZE,LineStyle(1,yellow), yellow)
    
    Sprite(jungleBox)
    banana = Sprite(bananaBox,((COLS*CELL_SIZE)/2,(ROWS*CELL_SIZE)/2))
    monkey = Sprite(monkeyBox)
    
    App().listenKeyEvent('keydown','right arrow',moveRight)
    App().listenKeyEvent('keydown','left arrow',moveLeft)
    App().listenKeyEvent('keydown','up arrow',moveUp)
    App().listenKeyEvent('keydown','down arrow',moveDown)
    App().run(step)
