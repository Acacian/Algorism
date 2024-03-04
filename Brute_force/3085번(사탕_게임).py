import sys
input = sys.stdin.readline

N = int(input())
Candybox = [0 for _ in range(N)]

for i in range(0,N):
    Candybox[i] = list(map(str,input().strip()))

Maxright = 0
Maxup = 0
Max = 0

def checkMax():
    for i in range(0,N):
        for j in range(0,N):
            