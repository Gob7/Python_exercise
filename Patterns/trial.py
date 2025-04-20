
def lov(a):
        for i in range(a*3):
                for j in range(a*4-3):
                        if i<a:
                                if j+1 in (a-i,a+i,3*a-2-i,3*a-2+i): print('*',end='')
                                else: print(' ',end=' ')
                        elif i>=2*a:
                                if j in (i-2*a+1, 6*a-5-i): print('*',end='')
                                elif i==a*3-1 and j in range(i-2*a+4, 6*a-6-i):
                                        if j%2==0: print('*',end='')
                                        else: print(' ',end=' ')
                                else: print(' ',end=' ')
                        else:
                                if j in (0,4*a-4): print('*',end='')
                                else: print(' ',end=' ')
                print() 
lov(5)