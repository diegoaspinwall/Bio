#Diego Aspinwall
#1-13-18
#coolClicking.py - started with connect four

from ggame import *

def placePiece(event):
    #Sprite(redfill, (event.x,event.y))
    print('R =',((event.x-CIRCX)**2+(event.y-CIRCY)**2)**.5)
    print(event.x,event.y)
    if ((event.x-CIRCX)**2+(event.y-CIRCY)**2)**.5 <= CIRCR:
        print('Inside')
    else:
        print('Outside')
        Sprite(LineAsset(event.x-CIRCX,event.y-CIRCY,blackOutline), (CIRCX,CIRCY))

def printBoard():
    Sprite(testhole, (CIRCX,CIRCY))
    '''
    for row in range(0,6):
        for col in range(0,7):
            Sprite(hole, (90*col+50, 90*row+50))
    '''

if __name__ == '__main__':
    
    CIRCX = 300
    CIRCY = 200
    CIRCR = 200
    
    white = Color(0xffffff,1)
    red = Color(0xff0000,1)
    blue = Color(0x0000ff,1)
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)
    
    hole = CircleAsset(40,blackOutline,white)
    redfill = CircleAsset(40,blackOutline,red)
    bluefill = CircleAsset(40,blackOutline,blue)
    testhole = CircleAsset(CIRCR,blackOutline,white)
    
    printBoard()
    
    App().listenMouseEvent('click', placePiece)
    App().run()
