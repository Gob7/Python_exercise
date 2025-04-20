#Operation on dates
print('> "From date" must be smaller than "To date".')
print('> Please enter the figures only in the format "dd/mm/yyyy.')
while True:
      fom=input('\nEnter "From date": ')
      day1=int(fom[0])*10+int(fom[1])

      to=input('\nEnter "To date": ')
      day2=int(to[0])*10+int(to[1])
      
