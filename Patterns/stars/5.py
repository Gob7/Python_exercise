#Star pattern 5
while True:
    try:
        a=int(eval(input('\nEnter a natural number: ')))
        for m in range(a):
              if m<a/2:
                      for n in range(m+1):
                            if n==0 or n==m:
                                print('*',end='\t')
                            else:
                                  print('',end='\t')
                      print()
              else:
                    z=a-m
                    for o in range(z,0,-1):
                          for p in range(o):
                            if p==0 or p==o-1:
                                print('*',end='\t')
                            else:
                                  print('',end='\t')
                          print()
                    break
    except:
        print('\nWrong input given!')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
                break
print('\nThank You!!!')
                
        
