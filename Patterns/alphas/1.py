#alpha pattern 1
while True:
    try:
        n=int(eval(input('\nEnter number of rows: ')))
        x='A'
        for i in range (n):
            for j in range (i+1):
                print(x,end='\t')
            print()
            x=chr(ord(x)+1)
    except:
        print('\nWrong number given.')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break
print('\nThank You!!!')   
