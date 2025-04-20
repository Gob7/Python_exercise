#even vs. odd
while True:
        try:
                a=list(eval(input('\nEnter a list: ')))
                even,odd,s_even,s_odd=0,0,0,0
                for i in a:
                        if type(i)==type(0):
                                if i%2==0:
                                        s_even,even=s_even+i,even+1
                                else:
                                        s_odd,odd=s_odd+i,odd+1
                print('\nThere are total:')
                print(even,'even number(s), whose sum is',s_even,'and',odd,'odd number(s), whose sum is',s_odd)
        except:
                print('\nYou entered something wrong; SORRY.')
        choice=input('\nEnter "n" to end the programme: ')
        if choice=='n':
                break
print('\nThank you!!!')
