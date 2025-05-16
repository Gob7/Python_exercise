#strong password
print('\nRULES: ')
print('\t> Password must contain 8 or more characters.')
print('\t> It should contain at least a digit, a capital letter, a small letter and a special character.')
while True:
      a=b=c=d=''
      p=input('\nEnter your password: ')
      for i in p:
            if ord(i) in range(65,91):
                  a+=i
            elif ord(i) in range(97,123):
                  b+=i
            elif ord(i) in range (48,58):
                  c+=i
            else:
                  d+=i
      if len(a)<1 or len(b)<1 or len(c)<1 or len(d)<1 or len(p)<8:
            print('\tInvalid password, please try again.')
      else:
            print('\tValid password')
            k=input('\nRe-enter the password: ')
            if p==k:
                  print('Password status:')
                  if len(p) in range(8,11) and len(d)<4:
                        print('\tWeak Password')
                  elif len(p)>25 or len(d)>7 or len(c)>10:
                        print('\tStrong Password')
                  else:
                        print('\tAverage Password')
                  print('\nPassword accepted.')
            else:
                  print('\nRe-entry was wrong, please try again.')
      choice=input('\nEnter "n" to end the programme: ')
      if choice=='n':
            break
print('\nThank you!!!')
                  
      
