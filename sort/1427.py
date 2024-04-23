from collections import deque

ls = list(map(str,input().strip()))
lsl = []

for i in range(len(ls)):
    lsl.append(int(ls[i]))

c = 0
while c != len(ls):
    c += 1
    for i in range(1,len(ls)):
        if lsl[i] >= lsl[i-1]:
            lsl[i] , lsl[i-1] = lsl[i-1] , lsl[i]

lso = 0
for i in range(len(lsl)):
    lso += int(lsl[i]) * 10**(len(lsl)-1-i)

print(lso)

# sorted(ls)
