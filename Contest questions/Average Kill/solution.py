n=int(input())
code=[]
avg=[]
for i in range(n):
    name=input()
    code.append(int(input()))
    x=list(map(int,input().split()))
    avg.append(sum(x)/5)
for i in range(n):
    print(code[i],avg[i])