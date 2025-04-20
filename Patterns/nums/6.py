#num pattern 6
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        y=0
        for z in range(1,n+1):
            y+=z
        for i in range (1,n+1):
            for j in range (1,i+1):
                print(y,end='\t')
                y-=1
            print()
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
