#alpha pattern 11
while True:
    try:
        n=int(input('\nEnter number of rows: '))
        for i in range (n,0,-1):
            y=65
            for j in range (i):
                print(chr(y),end='\t')
                y+=1
            print()
    except:
        print('\nWrong number given.')
    choice=input('\nEnter "n" to end the programme: ')
    if choice=='n':
        break        
print('\nThank You!!!')   
