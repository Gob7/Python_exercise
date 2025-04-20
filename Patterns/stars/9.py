#star pattern 9
while True:
      try:
            a=int(eval(input('\nEnter a natural number: ')))
            for i in range(a):
                  for j in range(a):
                        if i==0 or j==a-1 or j==i:
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
