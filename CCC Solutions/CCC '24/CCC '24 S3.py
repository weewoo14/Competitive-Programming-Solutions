import sys
from collections import defaultdict,deque
from bisect import bisect_left,bisect_right
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

def findclosest(dq,p):
    while dq:
        if dq[0] > p:
            return dq[0]
        dq.popleft()
    return -1

if a == b:
    print("YES")
    print(0)
else:
    lcmd,rcmd = [],[]
    gb = [[b[0],0,0]]
    d = defaultdict(deque)
    for i in range(1,n):
        if b[i] == gb[-1][0]:
            gb[-1][2] += 1
        else:
            gb.append([b[i],i,i])
    for i in range(n):
        d[a[i]].append(i)
    prev = -1
    for i in range(len(gb)):
        curseg = gb[i]
        neednum = curseg[0]
        l,r = curseg[1],curseg[2]
        if neednum not in d:
            print("NO")
            sys.exit()
        else:
            cpos = findclosest(d[neednum],prev)
            if cpos == -1:
                print("NO")
                sys.exit()
            else:
                prev = cpos
                if l < cpos:
                    lcmd.append(["L",l,cpos])
                if r > cpos:
                    rcmd.append(["R",cpos,r])
    print("YES")
    print(len(lcmd)+len(rcmd))
    for cmd,l,r in lcmd:
        print(cmd,l,r)
    for i in range(len(rcmd)-1,-1,-1):
        print(*rcmd[i])
