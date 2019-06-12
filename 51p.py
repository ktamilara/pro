number11=int(input())
l1=list(map(int,input().split()))
number12=[]
number13=1
for i1 in range(number11):
	val1=l1[i1:]
	ans1=len1(val1)
	for j1 in range(ans1-1):
		if val1[j1]>0 and val1[j1+1]<0:
			number13=number13+1
		elif val1[j1]<0 and val1[j1+1]>0:
			number13=number13+1
		else:
			break
	number12.append(str(number13))
	number13=1
print(" ".join(number12))
