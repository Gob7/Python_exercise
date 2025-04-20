#star pattern 3
while True:
        try:
                a=int(eval(input('\nEnter a natural number: ')))
                for i in range(a*3):
                        for j in range(a*3):
                                if i<a and j<a or i<a and j>a*2-1 or i>a*2-1 and j<a or i>a*2-1 and j>a*2-1:
                                        print('*',end='\t')
                                elif a*2>i>a-1 and a*2>j>a-1:
                                        print('*',end='\t')
                                else:
                                        print('',end='\t')
                        print()
        except:
                print('\nWrong input given!')
        choice=input('\nEnter "n" to end the programme: ')
        if choice=='n':
                break
print('\nThank You!!!')   

