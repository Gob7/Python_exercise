def lcs(x,n,y,m):
    z=[0]*(m+1)
    res=[]
    for i in range(n+1):
        res.append(list(z))
    for i in range(n):
        for j in range (m):
            if x[i]==y[j]: res[i+1][j+1]=res[i][j]+1
            else: res[i+1][j+1]=max(res[i][j+1],res[i+1][j])
    return res[n][m]
for _ in range(int(input())):
    x=input().split()
    y=input().split()
    n=int(x[0])
    m=int(y[0])
    x=x[1]
    y=y[1]
    print(lcs(x,n,y,m))
