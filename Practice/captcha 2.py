# Captcha 2
import random
while True:
      a,b,c=random.randint(0,9),random.randint(0,9),random.randint(0,2)
      l=['+','-','*']
      if c==0:
            d=a+b
      elif c==1:
            d=a-b
      else:
            d=a*b
      print('Solve the captcha (only integers are allowed ):',end='\n\t')
      print(a,l[c],b)
      try:
            e=int(input('Enter your answer: '))
            if d==e:
                  print("\nVerified, you're welcome!")
            else:
                  print('\nNo entry, wrong captcha entered.')
      except:
            print('\nNo entry, wrong captcha entered.')
      choice=input('\nEnter "n" to end the programme: ')
      if choice=='n':
            break
print('\nThank you!!!')
