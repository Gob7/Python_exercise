import random
x=100
print(x)
for i in range(x):
    n,m=random.randint(1,100),random.randint(1,100)
    print(n,end=' ')
    for i in range(n):
        print(chr(random.randint(97,122)),end='')
    print()
    print(m,end=' ')
    for i in range(m):
        print(chr(random.randint(97,122)),end='')
    print()
