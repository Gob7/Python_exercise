#alpha pattern 10
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        for i in range (n+1):
            y=64+n
            for j in range (i):
                print(chr(y),end='\t')
                y-=1
            print()
    except:
        print('\nWrong number given.')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
