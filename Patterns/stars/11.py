#star pattern 11
while True:
      try:
            a=int(eval(input('\nEnter a natural number: ')))
            for i in range(1,2*a):
                  for j in range (1,2*a):
                        if i<=a:
                              if j==a-i+1 or j==a+i-1:
                                    print('*',end='\t')
                              else:
                                    print(' ',end='\t')
                        else:
                              if j==i-a+1 or j==3*a-i-1:
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
                  
