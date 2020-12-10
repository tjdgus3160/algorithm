# 최대공약소 구하는 함수

def finding_gcd(a, b):
	while(b != 0):
		result = b
		a, b = b, a % b
	return result

def gcd_sub(a, b):
	while a != 0 and b != 0:
		if a < b:
			b = b - a
		else:
			a = a - b
	return a + b
	
def gcd_mod(a, b):
	mod = a % b
	while mod > 0:
		a = b
		b = mod
		mod = a % b
	return b
	
def gcd_rec(a, b):
	if a == b:
		return a
	if a > b:
		return gcd_rec(a - b, b)
	else:
		return gcd_rec(a, b - a)
	
# a, b를 입력받는다
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다

a, b = input().split()
a=int(a)
b=int(b)

x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)

print(x, y, z)