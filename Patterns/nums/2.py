#num pattern 2
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        s=n
        for i in range (1,n+1):
            for j in range (1,i+1):
                print(s,end='\t')
            s-=1
            print()
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
