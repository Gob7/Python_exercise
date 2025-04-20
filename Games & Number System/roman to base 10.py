#roman number to base 10
while True:
      a=input('\nEnter your valid roman number : ')
      a=a.upper()
      b='I','V','X','L','C','D','M'
      c=1,5,10,50,100,500,1000
      l=[]
      for i in range(len(a)):
            if a[i] in b:
                  j=0
                  while a[i]!=b[j]:
                        j+=1
                  l.append(c[j])
            else:
                  print('\nInvalid input.')
                  break
      else:
            for k in range(len(a)-1):
                  if l[k]==l[k+1] :
                        if l[k] not in (1,10,100,1000):
                              print('\nInvalid input.')
                              break
                  if len(l[k:k+4])==4:
                        if l[k]==l[k+1]==l[k+2]==l[k+3]:
                              print('\nInvalid input.')
                              break
                  if l[k]<l[k+1]:
                        if l[k]==1:
                              if l[k+1] not in (5,10):
                                    print('\nInvalid input.')
                                    break
                        elif l[k]==10:
                              if l[k+1] not in (50,100):
                                    print('\nInvalid input.')
                                    break
                        elif l[k]==100:
                              if l[k+1] not in (500,1000):
                                    print('\nInvalid input.')
                                    break
                        else:
                              print('\nInvalid input.')
                              break
                        if k>0:
                              if l[k]==1:
                                    if l[k-1] not in (10,50,100,500,1000):
                                          print('\nInvalid input.')
                                          break
                              elif l[k]==10:
                                    if l[k-1] not in (100,500,1000):
                                          print('\nInvalid input.')
                                          break
                              elif l[k]==100:
                                    if l[k-1] not in (1000,):
                                          print('\nInvalid input.')
                                          break
                        if len(l[k:k+3])==3:
                              if l[k]==1:
                                    print('\nInvalid input.')
                                    break
                              elif l[k]==10:
                                    if l[k+2] not in (1,5):
                                          print('\nInvalid input.')
                                          break
                              elif l[k]==100:
                                    if l[k+2] not in (1,5,10,50):
                                          print('\nInvalid input.')
                                          break
            else:
                  e,m=0,0
                  while m<len(l):
                        if len(l[m:m+2])==2:
                              if l[m]<l[m+1]:
                                    e+=l[m+1]-l[m]
                                    m+=2
                              else:
                                    e+=l[m]
                                    m+=1
                        else:
                              e+=l[m]
                              m+=1
                  print('\n\t',a,'=',e)
      choice=input('\nEnter "n" to end the programme: ')
      if choice=='n':
                  break
print('\nThank You!!!')
                              
