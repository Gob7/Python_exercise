#Star pattern 8
while True:
      try:
            a=int(eval(input('\nEnter a natural number: ')))
            for i in range(a):
                  for j in range(i+1):
                        if j==0 or j==i or i==a-1:
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
          
