#num pattern 3
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        s=1
        for i in range (n,0,-1):
            for j in range (i,0,-1):
                print(s,end='\t')
            s+=1
            print()
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
