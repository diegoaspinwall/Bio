#Diego Aspinwall
#12-17-17
#SurfAVol.py

while True:
    print('Enter "quit" to quit')
    print('Enter "s" for Sphere')
    print('Enter "c" for Cube')
    print('Enter "t" for Tetrahedron')
    print('Enter "i" for Icosahedron (20 sides)')
    
    shape = input('What shape do you want to look at? ')
    
    if shape == 'quit':
        break
    elif shape == 'c':
        thing = int(input('Enter side: '))
        print('Surface Area =', 6*thing**2)
        print('Volume =', thing**3)
        print('Surface Area/Volume =', (6*thing**2)/(thing**3))
    elif shape == 's':
        thing = int(input('Enter radius: '))
        print('Surface Area =', 4*3.1415926*(thing**2))
        print('Volume =', (4*3.1415926*(thing**3))/3)
        print('Surface Area/Volume =',3/thing)
    elif shape == 't':
        thing = int(input('Enter side: '))
        print('Surface Area =', ((3)**.5)*(thing**2))
        print('Volume =', ((((2)**.5)*(thing**3))/12))
        print('Surface Area/Volume =', (((3)**.5)*(thing**2))/((((2)**.5)*(thing**3))/12))
    elif shape == 'i':
        thing = int(input('Enter side: '))
        print('Surface Area =', )
        print('Volume =', )
        print('Surface Area/Volume =', )
    else:
        print('Invalid command, please repeat')
    
    print('')
