from collections import deque

Y = input().split()
N = int(Y[0])
K = int(Y[1])

# N = 7, K = 3
Q = deque()

for i in range(N):
    Q.append(K)
    
    if (K > N):
        K = N % K

print(Q)