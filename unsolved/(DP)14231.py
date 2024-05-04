import sys
input = sys.stdin.readline

n = int(input())
Lst = list(map(int,input().split()))

count = 0
nb = 0

for i in range(n):
    for j in range(i):
        if (n > 0 and Lst[i] > Lst[i-1] and Lst[i] > Lst[j] and j >= nb):
            count += i - j
            nb = i

else:
    print(count + 1)