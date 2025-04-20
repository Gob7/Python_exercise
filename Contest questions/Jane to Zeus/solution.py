for _ in range(int(input())):
    n=int(input())
    c='I','V','X','L','C','D','M'
    s=''
    i=1
    while n:
        d=n%10
        if d<4: s=d*c[(i-1)*2]+s
        elif d==4: s=c[(i-1)*2]+c[(i-1)*2+1]+s
        elif d<9: s=c[(i-1)*2+1]+(d-5)*c[(i-1)*2]+s
        elif d==9: s=c[(i-1)*2]+c[(i-1)*2+2]+s
        i+=1
        n//=10
    print(s)
