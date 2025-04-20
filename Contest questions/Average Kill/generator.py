import random
x=50
print(x)
for i in range(x):
    print('a')
    print(random.randint(10000,99999))
    for j in range(5):
        print(random.randint(0,1000),end=' ')
    print()
    
