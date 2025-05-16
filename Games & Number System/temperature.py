#temperature convertor
while True:
    try:
        choose=input('\nEnter unit of temperature, "c" for in centigrade/celsius, "f" for in fahrenheit and "k" for in kelvin: ')
        if choose in ('c','C'):
            c=float(eval(input('Enter temperature (in centigrade/celsius): ' )))
            k=c+273.15
            f=9/5*c+32
        elif choose in ('f','F'):
            f=float(eval(input('Enter temperature (in fahrenheit): ')))
            c=5/9*(f-32)
            k=c+273.15
        elif choose in ('k','K'):
            k=float(eval(input('Enter temperature (in kelvin): ')))
            c=k-273.15
            f=9/5*c+32
        print('\nGiven temperature in:',end='\n\n')
        print('\tcentigrade/celsius\t=   ',c)
        print('\tfahrenheit\t=   ',f)
        print('\tkelvin\t\t=   ',k,end='\n\n')
        if k<0:
            print('Invalid temperature is entered!!!')
        elif k==0:
            print('Given temperature is absolute zero.')
        elif k>0 and c<0:
            print('Given temperature is below freezing.')
        elif c==0:
            print('Given temperature is at the freezing point.')
        elif 20<c<40:
            print('Given temperature is in room temperature.')
        elif 0<c<100:
            print('Given temperature is in the normal range.')
        elif c==100:
            print('Given temperature is at the boiling point.')
        else:
            print('Given temperature is above the boiling point.')
    except:
                print('You entered something wrong; SORRY.')
    choice=input('\nPress "e" or "E" to exit: ')
    if choice in ('e','E'):
            break
print('\n\tThank You!!!')

