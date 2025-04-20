#Star pattern 7
while True:
      try:
            a=int(eval(input('\nEnter a natural number: ')))
            for i in range(a):
                  for j in range(a):
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
