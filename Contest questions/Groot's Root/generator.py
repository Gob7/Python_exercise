import random
x=30
print(x)
for i in range(x):
    x=random.randint(15,30)
    print(x)
    for i in range(x):
        print(random.randint(1,3),end=' ')
    print()
