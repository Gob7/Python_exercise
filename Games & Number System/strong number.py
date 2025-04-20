#strong number
def Strong(n):
      b=str(n)
      c=0
      for i in b:
            d=1
            for j in range(2,int(i)+1):
                  d*=j
            c+=d
      return c
while True:
      try:
            c=input('Press "p" or "P" to print Strong numbers: ')
            if c in ('P','p'):
                  a=int(eval(input('\nEnter the last number till you want(inclusive): '))) 
                  for i in range(a+1):
                        if i==Strong(i):
                              print(i)
            else:
                  a=int(eval(input('\nEnter a natural number: ')))
                  if Strong(a)==a:
                        print(a,'is a strong number.')
                  else:
                        print(a,'is not a strong number.')
            choice=input('\nEnter "n" or "N" to end the programme: ')
            if choice in ('n','N'):
                    break
      except:
            print('You entered something wrong; SORRY.')
            break
print('\n\tThank You!!!')
