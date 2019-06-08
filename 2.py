from itertools import combinations
u21,v1=map(int,input().split())
w1=len(str(u21))
x1=list(combinations(str(u21),w1-v1))
x1=(sorted(x1))
y1="".join(x1[0])
print(y1)
