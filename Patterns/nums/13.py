#num pattern 13
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        for i in range (n):
                for j in range (2*n-1):
                        if j<n-i-1 or j>n+i-1:
                                print(end='\t')
                        else:
                                if j<n:
                                        print(2*i+j-n+2,end='\t')
                                else:
                                        print(2*i+n-j,end='\t')
                print()
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')
