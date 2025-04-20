import random
x=100
print(x)
for i in range(x):
    x=random.randint(1,50)
    print(x)
    for i in range(2*x):
        print(random.randint(1,100),end=' ')
    print()
