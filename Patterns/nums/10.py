#num pattern 10
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        for i in range (1,n+1):
            x=n
            for j in range (1,i+1):
                print(x,end='\t')
                x-=1
            print()
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
