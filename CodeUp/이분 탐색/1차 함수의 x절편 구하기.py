def find(a,b):
	return -b/a

a,b=input().split()
c=find(float(a), float(b))
round(c,4)
print('%0.4f'%(c))
