from collections import Counter
t,n = map(int,input().split())
for test in range(t):
    s = input()
    c = Counter(s)
    valid = True
    for i in range(len(s)-1):
        if c[s[i]] == 1:
            if c[s[i+1]] == 1:
                valid = False
                break
        else:
            if c[s[i+1]] > 1:
                valid = False
                break
    if valid:
        print("T")
    else:
        print("F")