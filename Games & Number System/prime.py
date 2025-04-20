def prime(x):
    if x<2: return False
    flag = True
    for i in range(2, int(x**0.5)+1):
        if x%i == 0:
            flag = False
            break
    return flag

def count_list(l):
    d = {}
    for i in l:
        d.setdefault(i, 0)
        d[i] += 1
    return d

x = prime(7)
print(x)
d = count_list([0,5,2,2,3,2,3,0,1,0,0,0])
print(d)