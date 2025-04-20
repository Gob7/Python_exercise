#alpha pattern 6
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        y=chr(64)
        for k in range(1,n+1):
              y=chr(ord(y)+k)
        for i in range (n+1):
            for j in range (i):
                print(y,end='\t')
                y=chr(ord(y)-1)
            print()
    except:
        print('\nWrong number given.')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
