#Diego Aspinwall
#4-21-18
#indepAssort.py

from ggame import *

red = Color(0xFF0000,1)
blue = Color(0x00FF00,1)

blueOutline = LineStyle(1,blue)
redOutline = LineStyle(1,red)

redRectangle = RectangleAsset(200,75,redOutline,red)
blueRectangle = RectangleAsset(200,75,blueOutline,blue)

Sprite(blueRectangle)
Sprite(redRectangle, (0,75))
App().run()
