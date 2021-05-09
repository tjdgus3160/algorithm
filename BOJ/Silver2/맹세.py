# 3407번
from collections import deque
import sys
input=sys.stdin.readline

s1={ 'h', 'b', 'c', 'n', 'o', 'f', 'p', 's', 'k', 'v', 'y', 'i', 'w', 'u' }
s2={
	"ba", "ca" , "ga", "la", "na", "pa", "ra", "ta", "db", "nb", "pb", "rb", "sb", "tb", "yb", "ac",
	"sc", "tc", "cd", "gd", "md", "nd", "pd", "be", "ce", "fe", "ge", "he", "ne", "re", "se", "te",
	"xe", "cf", "hf", "rf", "ag", "hg", "mg", "rg", "sg", "bh", "rh", "th", "bi", "li", "ni", "si",
	"ti", "bk", "al", "cl", "fl", "tl", "am", "cm", "fm", "pm", "sm", "tm", "cn", "in", "mn", "rn",
	"sn", "zn", "co", "ho", "mo", "no", "po", "np", "ar", "br", "cr", "er", "fr", "ir", "kr", "lr",
	"pr", "sr", "zr", "as", "cs", "ds", "es", "hs", "os", "at", "mt", "pt", "au", "cu", "eu", "lu",
	"pu", "ru", "lv", "dy"
	}

for _ in range(int(input())):
    s=input().rstrip('\n')
    dq=deque([0])
    visit=[False]*len(s)
    flag=False
    while dq:
        idx=dq.popleft()
        if idx==len(s):
            flag=True
            break
        if s[idx] in s1 and not visit[idx]:
            visit[idx]=True
            dq.append(idx+1)
        if idx+1<len(s) and s[idx:idx+2] in s2 and not visit[idx+1]:
            visit[idx+1]=True
            dq.append(idx+2)
    print('YES' if flag else 'NO')