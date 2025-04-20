#roman numerical convertor
while True:
      try:
            print('\nEnter a natural number less than 4000')
            a=int(eval(input('to convert into roman numerical: ')))
            if 0<a<4000:
                  c='I','V','X','L','C','D','M'
                  s,n,i='',a,1
                  while n:
                        d=n%10
                        if d<4:
                              s=d*c[(i-1)*2]+s
                        elif d==4:
                              s=c[(i-1)*2]+c[(i-1)*2+1]+s
                        elif d<9:
                              s=c[(i-1)*2+1]+(d-5)*c[(i-1)*2]+s
                        elif d==9:
                              s=c[(i-1)*2]+c[(i-1)*2+2]+s
                        i+=1
                        n//=10
                  print('\n\t',a,'=',s)
            else:
                  print('\nInvalid input.')
      except:
            print('\nYou entered something wrong; SORRY.')
      choice=input('\nEnter "n" to end the programme: ')
      if choice=='n':
                  break
print('\nThank You!!!')
