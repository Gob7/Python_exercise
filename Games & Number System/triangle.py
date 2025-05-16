#area and perimeter of a triangle
while True:
    try:
        s1_b=float(eval(input('\nEnter (base/first side) of the triangle (in cm): ')))
        s2_h=float(eval(input('Enter second side of the triangle (in cm): ')))
        s3_0=float(eval(input('Enter third side of the triangle (in cm): ')))
        if s1_b<=0 or s2_h<=0 or s3_0<=0 or s1_b+s2_h<=s3_0 or s3_0+s2_h<=s1_b or s1_b+s3_0<=s2_h:
            print('Invalid input.')
        else:
                sp=(s1_b+s2_h+s3_0)/2
                area=(sp*(sp-s1_b)*(sp-s2_h)*(sp-s3_0))**0.5
                perimeter=s1_b+s2_h+s3_0
                print('\nArea and perimeter of the given triangle is',area,'cm square and',perimeter,'cm respectively.')
        choice=input('\nEnter "n" to end the programme: ')
        if choice=='n':
                break
    except:
            print('\nYou entered something wrong; SORRY.')
            choice=input('\nEnter "n" to end the programme: ')
            if choice=='n':
                break
print('\nThank you!!!')

    
