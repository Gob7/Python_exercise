#star pattern 6
while True:
    try:
        a=int(eval(input('\nEnter a natural number: ')))
        for i in range(a,0,-1):
                for j in range(1,a+1):
                      if i<=j:
                            print('*',end='\t')
                      else:       
                            print(' ',end='\t')
                print()
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
