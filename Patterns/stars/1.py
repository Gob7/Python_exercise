#star pattern 1
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        for i in range (0,n):
            for j in range (0,i+1):
                print('*',end='\t')
            print()
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
