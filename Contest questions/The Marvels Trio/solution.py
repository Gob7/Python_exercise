def solve(a,b,c,n):
    if n==1: return a
    if n==2: return b
    if n==3: return c
    for i in range(3,n):
        a,b,c=b,c,a+b+c
    return c
for _ in range(int(input())):
    a,b,c,n=map(int,input().split())
    print(solve(a,b,c,n))
