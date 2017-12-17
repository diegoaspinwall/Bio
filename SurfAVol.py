#Diego Aspinwall
#12-17-17
#SurfAVol.py

while True:
    print('Enter "quit" to quit')
    print('Enter "s" for Sphere')
    print('Enter "c" for Cube')
    print('Enter "t" for Tetrahedron')
    print('Enter "i" for Icosahedron (20 sides)')
    
    shape = input('What shape do you want to look at?')
    
    if shape == 'quit':
        break
    elif shape == 's':
        thing = int(input('Enter radius: '))
    elif shape == 'c':
        thing = int(input('Enter radius: '))
    elif shape == 't':
        thing = int(input('Enter radius: '))
    elif shape == 'i':
        thing = int(input('Enter radius: '))
    else:
        print('Invalid command, please repeat')
    
    print('')
