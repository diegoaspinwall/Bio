#Diego Aspinwall
#4-21-18
#indepAssort.py

from ggame import *

red = Color(0xFF0000,1)
blue = Color(0x0000FF,1)

blueOutline = LineStyle(1,blue)
redOutline = LineStyle(1,red)

redRectangle = RectangleAsset(5,10,redOutline,red)
blueRectangle = RectangleAsset(5,10,blueOutline,blue)

Sprite(blueRectangle)
Sprite(redRectangle, (5,0))
App().run()
