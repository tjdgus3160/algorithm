import math
a,b,c=input().split()
a,b,c=int(a),int(b),int(c)
i=(-1*b)/(2*a)
j=(b**2)-(4*a*c)
if j==0:
    print("%.2f"%(i))
elif j>0:
    k=math.sqrt(j)/(2*a)
    print("%.2f"%(i+k))
    print("%.2f" % (i-k))
else:
    k =abs(math.sqrt(abs(j))/(2*a))
    print("%.2f+%.2fi"%(i,k))
    print("%.2f-%.2fi" % (i,k))
