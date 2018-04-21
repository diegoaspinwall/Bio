#Diego Aspinwall
#4-21-18
#indepAssort.py

from ggame import *

red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)

blueOutline = LineStyle(1,blue)
redOutline = LineStyle(1,red)

redRectangle = RectangleAsset(10,20,redOutline,red)
blueRectangle = RectangleAsset(10,20,blueOutline,blue)

for i in range(0,23):
    print(i)
    Sprite(blueRectangle, (0,20*i))
    Sprite(redRectangle, (10,20*i))

App().run()
