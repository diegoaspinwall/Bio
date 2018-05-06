#Diego Aspinwall
#5-6-18
#cross.py

from ggame import *

print('This is a simulation that takes two flower parents, and calculates the probability of a color')
print("The flower's color exhibits incomplete dominance")
print('')

male = int(input('What is the male genotype? 1=Heterozygous, 2= Homo red, 3= Homo white '))
female = int(input('What is the female genotype? 1=Heterozygous, 2= Homo red, 3= Homo white '))

red = Color(0xFF0000,1)
pink = Color(0xFF80D5,1)
white = Color(0xFFFFFF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black) 

m=''
f=''

if male==1:
    m='Rr'
elif male==2:
    m='RR'
else:
    m='rr'

if female==1:
    f='Rr'
elif female==2:
    f='RR'
else:
    f='rr'

print('Male genotype =', m)
print('Female genotype =', f)

print('Combinations:')
for i in range(0,2):
    for j in range(0,2):
        print(m[i]+f[j])


#circle = CircleAsset(50,blackOutline,color)
