n = int(input())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))
total = 0
for i in range(n):
    if arr1[i] == 1:
        total += 3
    if arr2[i] == 1:
        total += 3
    if (i+1) <= n-1:
        if arr1[i+1] == 1 and arr1[i] == 1:
            total -= 2
        if arr2[i+1] == 1 and arr2[i] == 1:
            total -= 2
    if arr2[i] == 1 and i % 2 == 0 and arr1[i] == 1:
        total -= 2
print(total)