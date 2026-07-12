#frequency of items
while True:
    try:
        a=list(eval(input('\nEnter a list: ')))
        print('There are total:')
        b=[]
        for i in a:
            if i not in b:
                b.append(i)
                print('\t',a.count(i),'number of',i)
        choice=input('\nEnter "n" to end the programme: ')
        if choice=='n':
            break
    except:
            print('You entered something wrong; SORRY.')
            choice=input('\nEnter "n" to end the programme: ')
            if choice=='n':
                break
print('\nThank you!!!')
