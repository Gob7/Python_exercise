#any to any
print('\nNOTE: The base of your number must be a natural number between 2 and 36 (both inclusive).')
print('\tThis program is only able to convert natural numbers.')
while True:
      try:
            a,b,c=int(input('\nEnter the base of your number: \t\t')),input('Enter your number to convert: \t\t\t'),int(input('Enter the base to which you want to convert: \t'))
            if a in range (2,37) and c in range (2,37):
                  d,e,g=b[::-1].upper(),0,''
                  for j in d:
                        try:
                              if not(ord(j) in range(65,55+a) or int(j) in range(a)):
                                    print('\nInvalid number with base',a)
                                    break
                        except:
                                    print('\nInvalid number with base',a)
                                    break
                  else:
                        for i in range (len(d)):
                              if ord(d[i]) in range(65,91):
                                    f=ord(d[i])-55
                              else:
                                    f=int(d[i]) 
                              e+=f*a**i
                        while e:
                              h,e=e%c,e//c
                              if h>9:
                                    h=chr(55+h)
                              g+=str(h)
                        g=g[::-1]
                        print('\n',b,'( base',a,') =',g,'( base',c,')')
            else:
                  print('\nInvalid base entered.')
      except:
            print('\nInvalid base entered.')
      choice=input('\nPress "e" or "E" to exit: ')
      if choice in ('e','E'):
            break
print('\n\tThank You!!!')
