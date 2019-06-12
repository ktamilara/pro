value11=int(input())
value12=list(map(int,input().split()))
res1=0
for i1 in range(len(value12)-2):
    for j1 in range(i1+1,len(value12)-1):
        for k1 in range(j1+1,len(value12)):
            if value12[i1]<value12[j1]<value12[k1] and i1<j1<k1:
                res1=res1+1
print(res1)
