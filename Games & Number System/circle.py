#area of circle
import math
while True:
        try:
            radius=float(eval(input('Enter the radius of the circle (in cm): ')))
            if radius>0:
                    area=math.pi*radius**2
                    circumference=math.pi*radius*2
                    print('Area and circumference of the circle of radius',radius,'cm is',area,'cm square and',circumference,'cm respectively.')
            else:
                    print('You entered something wrong; SORRY.')
        except:
                print('You entered something wrong; SORRY.')
        choice=input('\nEnter "n" to end the programme: ')
        if choice=='n':
                break
print('\nThank You!!!')
