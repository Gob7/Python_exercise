#calculating %age
while True:
    try:
        ma=int(eval(input('Enter your marks in Math: ')))
        sc=int(eval(input('Enter your marks in Science: ')))
        sst=int(eval(input('Enter your marks in Social Science: ')))
        eng=int(eval(input('Enter your marks in English: ')))
        hs=int(eval(input('Enter your marks in Hindi/Sanskrit: ')))
        fm=int(eval(input('Enter the full marks of a subject: ')))
        pg=(ma+sc+sst+eng+hs)/5/fm*100
        print('Your got',pg,'%age .')
        choice=input('\nEnter "n" to end the programme: ')
        if choice=='n':
            break
    except:
                print('You entered something wrong; SORRY.')
                break
print('\nThankyou!!!')
