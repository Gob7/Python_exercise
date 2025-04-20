for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    x=y=0
    for i in range(7):
        x+=a[i]
        y+=b[i]
        if x>24 and y>24:
            print('BOTH')
            break
        elif x>24:
            print('WIDOW')
            break
        elif y>24:
            print('HAWKEYE')
            break
    else: print('NONE')
