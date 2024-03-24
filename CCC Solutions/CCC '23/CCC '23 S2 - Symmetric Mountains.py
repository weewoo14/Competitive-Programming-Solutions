n = int(input())
mountains = list(map(int,input().split()))
final = [0]
for _ in range(n-1):
    final.append(float('inf'))
for i in range(n-1):
    fidx = False
    el,er = i,i+1
    ol,odr = i-1,i+1
    ort,ert = 0,0
    while True:
        if i != 0:
            ort+=abs(mountains[ol]-mountains[odr])
        if i != 0:
            if ort < final[odr-ol]:
                final[odr-ol] = ort
        ol -= 1
        odr += 1
        if ol < 0 or odr >= n:
            break
    while True:
        if i == 0:
            final[1] = abs(mountains[0]-mountains[1])
            fidx = True
        else:
            ert += abs(mountains[el]-mountains[er])
        if ert < final[er-el] and not fidx:
            final[er-el] = ert
        el -= 1
        er += 1
        if el < 0 or er >= n:
            break
print(*final)