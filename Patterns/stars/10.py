#star pattern 10
while True:
      try:
            a=int(eval(input('\nEnter a natural number: ')))
            for i in range(1,2*a):
                  for j in range (1,2*a):
                        if i<=a:
                              if j in range (a-i+1, a+i):
                                    print('*',end='\t')
                              else:
                                    print(' ',end='\t')
                        else:
                              if j in range (i-a+1 , 3*a-i):
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
