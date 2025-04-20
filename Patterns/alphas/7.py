#alpha pattern 7
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        y='A'
        for i in range (n,0,-1):
            for j in range (i):
                print(y,end='\t')
                y=chr(ord(y)+1)
            print()
    except:
        print('\nWrong number given.')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
