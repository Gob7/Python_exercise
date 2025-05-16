#height convertor
while True:
    try:
        choose=input('Enter unit of your height "cm" for in centimeters and "fi" for in feet & inches: ')
        if choose=='cm':
            cm=float(eval(input('Enter your height (in cm): ' )))
            feet=int(cm/2.54//12)
            inches=cm/2.54%12
            print('Your height is',feet,'feet and',inches,'inches .')
        elif choose=='fi':
            foot=int(eval(input('Enter your height:   feet = ')))
            inch=float(input('                   inches = '))
            cm=(foot*12+inch)*2.54
            print('Your height is',cm,'cm .')
        choice=input('\nEnter "n" to end the programme: ')
        if choice=='n':
            break
    except:
                print('You entered something wrong; SORRY.')
                break
print('\nThank you!!!')
