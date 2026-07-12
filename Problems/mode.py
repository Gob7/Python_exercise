#mode in a list
while True:
        try:
                a=list(eval(input('Enter a list: ')))
                d={}
                for i in range(0,len(a)):
                        d[a[i]]=a.count(a[i])
                z=d[a[0]]
                y=a[0]
                for j in d:
                        if d[j]>z:
                                z=d[j]
                                y=j
                for k in d:
                        if d[k]==z:
                                y=k
                                print(y,'is mode and present',z,'times.')
                choice=input('\nEnter "n" to end the programme: ')
                if choice=='n':
                        break
        except:
                print('You entered something wrong; SORRY.')
                choice=input('\nEnter "n" to end the programme: ')
                if choice=='n':
                        break
print('\nThank you!!!')
