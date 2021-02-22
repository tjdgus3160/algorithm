# 9242번
import sys
input=sys.stdin.readline

dic={
    '**** ** ** ****':'0',
    '  *  *  *  *  *':'1',
    '***  *****  ***':'2',
    '***  ****  ****':'3',
    '* ** ****  *  *':'4',
    '****  ***  ****':'5',
    '****  **** ****':'6',
    '***  *  *  *  *':'7',
    '**** ***** ****':'8',
    '**** ****  ****':'9'
}
arr=[]
for _ in range(5):
    arr.append(input().rstrip('\n'))
n=(len(arr[0])+1)//4
tmp=[[] for _ in range(n)]
for i in range(5):
    k=0
    for j in range(0,len(arr[0]),4):
        try:
            tmp[k].append(arr[i][j:j+3])
            k+=1
        except:
            print('BOOM!!')
            exit()
res=''
for i in tmp:
    try:
        res+=dic[''.join(i)]
    except:
        print('BOOM!!')
        exit()
if int(res)%6==0:
    print('BEER!!')
else:
    print('BOOM!!')
