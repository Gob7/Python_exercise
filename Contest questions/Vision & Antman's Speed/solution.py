for _ in range(int(input())):
    x,x1,x2,v1,v2=map(int,input().split())
    x1=abs(x-x1)
    x2=abs(x-x2)
    t1=x1/v1
    t2=x2/v2
    if t1<t2: print('VISION')
    elif t1>t2: print('ANTMAN')
    else: print('BOTH')
