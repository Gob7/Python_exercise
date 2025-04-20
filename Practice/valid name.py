# Valid name
while True:
      while True:
            a=input('\nEnter your salutations from "MR", "MRS" and "MISS": ')
            a=a.upper()
            if a in ("MR", "MRS", "MISS"):
                  break
            else:
                  print('\tInvalid entry, try again.')
      while True:
            b=input('\nEnter your first name: ')
            b=b.upper()
            if len(b)>0 and len(b)<50:
                  for i in b:
                        if ord(i) not in range(65,91):
                              print('\tInvalid entry, try again.')
                              break
                  else:
                        break
            else:
                  print('\tInvalid entry, try again.')
      while True:
            c=input('\nEnter your middle name (press ENTER, if you have no middle name): ')
            c=c.upper()
            for j in c:
                  if ord(j) not in range(65,91) or len(c)>49:
                        print('\tInvalid entry, try again.')
                        break
            else:
                  break
      while True:
            d=input('\nEnter your last name: ')
            d=d.upper()
            if len(d)>0 and len(d)<50:
                  for k in d:
                        if ord(k) not in range(65,91):
                              print('\tInvalid entry, try again.')
                              break
                  else:
                        break
            else:
                  print('\tInvalid entry, try again.')
      if len(c)==0:
            name=a+' '+b+' '+d
      else:
            name=a+' '+b+' '+c+' '+d
      print('\nWelcome',name)
      choice=input('\nEnter "n" to end the programme: ')
      if choice=='n':
            break
print('\nThank You!!!')
            
