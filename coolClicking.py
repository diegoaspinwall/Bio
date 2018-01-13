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
        Sprite(LineAsset(0,40,blackOutline), (event.x,event.y-40))
        Sprite(CircleAsset(10,blackOutline,red),(event.x,event.y-50))

def printBoard():
    Sprite(testhole, (CIRCX,CIRCY))

if __name__ == '__main__':
    CIRCX = 300
    CIRCY = 200
    CIRCR = 200
    
    white = Color(0xffffff,1)
    red = Color(0xff0000,1)
    blue = Color(0x0000ff,1)
    black = Color(0x000000,1)
    blackOutline = LineStyle(1,black)
    
    redfill = CircleAsset(20,blackOutline,red)
    testhole = CircleAsset(CIRCR,blackOutline,white)
    
    printBoard()
    
    App().listenMouseEvent('click', placePiece)
    App().run()
