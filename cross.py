#Diego Aspinwall
#5-6-18
#cross.py

from ggame import *
from random import randint

print('This is a simulation that takes two flower parents, and calculates the probability of a color')
print("The flower's color exhibits incomplete dominance")
print('')

male = int(input('What is the male genotype? 1=Heterozygous, 2= Homo red, 3= Homo white '))
female = int(input('What is the female genotype? 1=Heterozygous, 2= Homo red, 3= Homo white '))
print('')

red = Color(0xFF0000,1)
pink = Color(0xFF80D5,1)
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)
green= Color(0x00FF00,1)

blackOutline = LineStyle(1,black) 

m=''
f=''

if male==1:
    m='RW'
elif male==2:
    m='RR'
else:
    m='WW'

if female==1:
    f='RW'
elif female==2:
    f='RR'
else:
    f='WW'

print('Male genotype =', m)
print('Female genotype =', f)

print('Combinations:')
list=[]
for i in range(0,2):
    for j in range(0,2):
        list.append(m[i]+f[j])

for b in range(0,4):
    print(list[b])

print('This is a random possibility of flower color -->')

choice= list[randint(0,3)]
color=''

if choice == 'WW':
    color=white
elif choice == 'RR':
    color=red
else:
    color=pink

circle = CircleAsset(50,blackOutline,color)
Sprite(circle,(50,50))
App().run()
