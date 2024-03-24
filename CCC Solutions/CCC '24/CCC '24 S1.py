import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for i in range(n)]
t = 0
for i in range(n//2):
    if arr[i] == arr[n//2 + i]:
        t += 2
print(t)