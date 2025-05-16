#interest and amount
while True:
    try:
        p=float(eval(input('Enter principle amount (in ₹): ')))
        r=float(eval(input('Enter rate of interest (in %age): ')))
        t=float(eval(input('Enter time period (in years): ')))
        ty=input('Enter "SI" for simple interest, "CI" for compound interest and (press enter) for both: ')
        si=round(p*r*t/100,2)
        asi=p+si
        t1=t//1
        t2=t-t1
        aci=round(p*(1+r/100)**t1+p*r*t2/100,2)
        ci=round(aci-p,2)
        if ty=='SI':
            print('\nYour simple interest is ₹',si,'/- with amount of ₹',asi,'/-')
        elif ty=='CI':
            print('\nYour compound interest is ₹',ci,'/- with amount of ₹',aci,'/-')
        else:
            print('\nYour simple interest is ₹',si,'/- with amount of ₹',asi,'/-  and',end=' ')
            print('your compound interest is ₹',ci,'/- with amount of ₹',aci,'/-')
        choice=input('\nEnter "n" to end the programme: ')
        if choice=='n':
            break
    except:
                print('You entered something wrong; SORRY.')
                break
print('\nThankyou!!!')
