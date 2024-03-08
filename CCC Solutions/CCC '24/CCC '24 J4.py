from collections import Counter
import sys
s1 = input()
s2 = input()
c1,c2 = Counter(s1),Counter(s2)
cf1,cf2 = Counter(),Counter()
poss = []
for key,val in c1.items():
    if key not in c2:
        poss.append(key)
    cf1[val] += 1
for key,val in c2.items():
    cf2[val] += 1
if len(poss) == 1:
    for key,val in c2.items():
        if key not in c1:
            print(poss[0],key)
            print('-')
else:
    quiet = poss[0]
    silent = poss[1]
    s3 = s1.replace(quiet,'')
    if len(s3) < len(s2) or len(s3) > len(s2):
        quiet = poss[1]
        silent = poss[0]
    else:
        for i in range(len(s3)):
            if s3[i] != s2[i] and s3[i] not in poss:
                quiet = poss[1]
                silent = poss[0]
                break
    for key,val in c2.items():
        if key not in c1:
            print(silent,key)
            print(quiet)