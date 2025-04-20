#swapping adjacent elements
while True:
        try:
                l=list(eval(input('Enter a list: ')))
                for i in range(0,len(l)//2*2,2):
                    l[i],l[i+1]=l[i+1],l[i]
                print('The new list is',l)
                choice=input('\nEnter "n" to end the programme: ')
                if choice=='n':
                    break
        except:
                print('You entered something wrong; SORRY.')
                break
print('\nThankyou!!!')
