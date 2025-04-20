#HCF and LCM
while True:
      try:
            a=int(eval(input('\nEnter the first natural number: ')))
            b=int(eval(input('Enter the second natural number: ')))
            if a>0 and b>0:
                  for i in range(a,0,-1):
                        if a%i==0 and b%i==0:
                              break
                  c=int(a*b/i)
                  print('\n\tHCF and LCM of',a,'and',b,'are',i,'and',c,'respectively.')
            else:
                  print('\nInvalid numbers entered.')
      except:
            print('\nInvalid numbers entered.')
      choice=input('\nPress "e" or "E" to exit: ')
      if choice in ('e','E'):
            break
print('\n\tThank You!!!')
