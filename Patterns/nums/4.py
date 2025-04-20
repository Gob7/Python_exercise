#num pattern 4
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        for i in range (n,0,-1):
            for j in range (i,0,-1):
                print(i,end='\t')
            print()
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
