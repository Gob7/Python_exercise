for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    d={}
    for i in a:
        d.setdefault(i,0)
        d[i]+=1
        if d[i]>2:
            print(0)
            break
    else: print(1)
