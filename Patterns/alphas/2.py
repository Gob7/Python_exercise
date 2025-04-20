#alpha pattern 2
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        y=chr(64+n)
        for i in range (n):
            for j in range (i+1):
                print(y,end='\t')
            print()
            y=chr(ord(y)-1)
    except:
        print('\nWrong number given.')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
