#Armstrong numbers
while True:
      try:
            z=input('\nEnter "p" to print Armstrong numbers, or any other key* to check: ')
            if z=='p' or 'P':
                  for i in range(int(input('\nEnter the last number till you want: '))+1):
                        a=str(i)
                        c=0
                        for j in a:
                              c+=int(j)**len(a)
                        if i==c:
                              print(i)
            else:
                  a=int(eval(input('\nEnter a natural number: ')))
                  b=str(a)
                  c=0
                  for i in b:
                        c+=int(i)**len(b)
                  if c==a:
                        print(a,'is an Armstrong number.')
                  else:
                        print(a,'is not an Armstrong number.')
      except:
            print('\nYou entered something wrong; SORRY.')
      choice=input('\nEnter "n" to end the programme: ')
      if choice=='n':
            break
print('\nThank You!!!')

            
