x11,x21=input().split()
temp1=0
if len(x11)>len(x21):
  x11,x21=x21,x11
i1=0
while i1<len(x11):
  temp+=(ord(x21[i1])-ord(x11[i1]))
  i1+=1
for i1 in range(i1,len(x21)):
  temp1+=ord(x21[i1])-ord('a1')+1
print(temp1)
