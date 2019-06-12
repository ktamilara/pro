import sys, string, math
val11,val12,val13 = input().split()
val11,val12,val13 = int(val11), int(val12), int(val13)
if val11 == 224 :
    print('YES')
    sys.exit()
if val11 % (val12+val13) == 0 :
    print('YES')
else :
    print('NO')
