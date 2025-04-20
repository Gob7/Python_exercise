import random
def next(Index,previous):
        if Index==1: possible=[2,4]
        elif Index==2: possible=[1,5,3]
        elif Index==3: possible=[2,6]
        elif Index==4: possible=[1,5,7]
        elif Index==5: possible=[2,4,6,8]
        elif Index==6: possible=[3,5,9]
        elif Index==7: possible=[4,8]
        elif Index==8: possible=[5,7,9]
        elif Index==9: possible=[6,8]
        for i in range(len(possible)-1,-1,-1):
                if str(possible[i]) in previous: possible.pop(i)
        if possible==[]: return -1
        return possible[random.randint(0,len(possible)-1)]
def solve(code,number):
        answer=number[int(code[0])]
        for i in range (1,len(code),2):
                if int(code[i]) in (2,8): answer+=number[int(code[i+1])]
                elif int(code[i]) in (4,6): answer-=number[int(code[i+1])]
        return answer

print('Format:\n1\t2\t3\n4\t5\t6\n7\t8\t9')
while True:
        number=[]
        while len(number)!=5:
                x=random.randint(1,9)
                if x not in number: number.append(x)
        number={1:number[0],2:'+',3:number[1],4:'-',5:number[2],6:'-',7:number[3],8:'+',9:number[4]}
        print('\n',number[1],'\t',number[2],'\t',number[3],'\n',number[4],'\t',number[5],
              '\t',number[6],'\n',number[7],'\t',number[8],'\t',number[9])
        answer,previous='',''
        Index=random.randint(0,4)*2+1
        previous+=str(Index)
        answer+=str(number[Index])
        y=random.randint(1,5)
        while len(previous)==1 or answer<1:
                answer=str(answer)
                for i in range(y*2):
                        Index=next(Index,previous)
                        if Index==-1: break
                        previous+=str(Index)
                        answer+=str(number[Index])
                if len(answer)%2==0: answer=answer[:-1]
                answer=eval(answer)
        print('\nGet:\t',answer)
        code=input('\nEnter your answer: ')
        if len(code)%2 and solve(code,number)==answer: print('Suckces')
        else: print('fail, you got',solve(code,number))
