for _ in range(int(input())):
    s=input()
    x='Yes'
    j=-1
    for i in range(3):
        if x[i]==s[0]:
            j=i
            break
    else:
        print('NO')
        continue
    for i in range (1,len(s)):
        j+=1
        if j==3: j=0
        if s[i]!=x[j]:
            print('NO')
            break 
    else:
        print('YES')
