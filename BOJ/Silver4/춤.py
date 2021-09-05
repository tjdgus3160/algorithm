import sys
input=sys.stdin.readline

while True:
    s=input().rstrip()
    if not s:
        break
    arr=s.split()
    error=[]
    role1=[]
    role5=False
    role3=set()
    for idx,v in enumerate(arr):
        if v == 'dip' and not((idx>=1 and arr[idx-1]=='jiggle') or(idx<len(arr)-1 and arr[idx+1]=='twirl') or(idx>=2 and arr[idx-2]=='jiggle')):
            error.append(1)
            role1.append(idx)
        if idx==0 and v=='jiggle':
            error.append(4)
        if v=='dip':
            role5=True
        if v=='twirl' or v=='hop':
            role3.add(v)
    if not(arr[-1] == 'clap' and arr[-2]=='stomp' and arr[-3]=='clap'):
        error.append(2)
    if not role5:
        error.append(5)
    if len(role3)==1 and role3.pop()=='twirl':
        error.append(3)
    if not error:
        print(f'form ok: {s}')
    elif len(error)==1:
        if error[0]==1:
            for idx in role1:
                arr[idx]='DIP'
            tmp=' '.join(arr)
            print(f'form error {error[0]}: {tmp}')
        else:
            print(f'form error {error[0]}: {s}')
    else:
        res='form errors '
        for idx,v in enumerate(sorted(error)):
            if idx==0:
                res+=str(v)
            elif idx==len(error)-1:
                if 1 in error:
                    for idx in role1:
                        arr[idx] = 'DIP'
                    s = ' '.join(arr)
                res+=f' and {v}: {s}'
            else:
                res+=f', {v}'
        print(res)