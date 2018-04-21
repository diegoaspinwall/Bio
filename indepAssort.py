#Diego Aspinwall
#4-21-18
#indepAssort.py

from ggame import *
from random import randint

n = int(input('What is n? '))

red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(10,20,blackOutline,red)
blueRectangle = RectangleAsset(10,20,blackOutline,blue)

for i in range(0,n):
    num = randint(0,1)
    if num==1:
        Sprite(blueRectangle, (0,20*i))
        Sprite(redRectangle, (10,20*i))
    if num==0:
        Sprite(blueRectangle, (10,20*i))
        Sprite(redRectangle, (0,20*i))

App().run()
