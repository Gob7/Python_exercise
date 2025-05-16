# Captcha 1
import random
while True:
      a,b=chr(random.randint(97,122)),chr(random.randint(97,122))
      c,d=chr(random.randint(65,90)),chr(random.randint(65,90))
      e,f=chr(random.randint(48,57)),chr(random.randint(48,57))
      l,s=[a,b,c,d,e,f],''
      for i in range(6):
            g=random.randint(0,len(l)-1)
            s+=l[g]
            l.pop(g)
      print('\nCaptcha: ',s)
      k=input('Enter the captcha: ')
      if k==s:
            print("\nVerified, you're welcome!")
      else:
            print('\nNo entry, wrong captcha entered.')
      choice=input('\nEnter "n" to end the programme: ')
      if choice=='n':
            break
print('\nThank You!!!')
