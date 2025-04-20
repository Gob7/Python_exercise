def reproduce(age,day):
    if day==1: return 1
    day-=1
    if age>=3: return 0
    age+=1
    return reproduce(age,day)+2*reproduce(1,day)
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    for i in a:
        ans+=reproduce(i,7)
    print(ans)
