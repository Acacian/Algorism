import sys
input = sys.stdin.readline
from collections import deque

all = list(map(int,input().split()))

N = all[0]
M = all[1]
K = all[2]
X = all[3]

road = []
for i in range(0,M):
    road.append(input().split())

def bfs(start_node, graph):
    queue = deque([start_node])
    visited = set([start_node])

    while queue:
        curr_node = queue.popleft()

        if curr_node == K:
            return

        for next_node in graph[curr_node]:
            if next_node not in visited:
                visited.add(next_node)
                queue.append(next_node)
    return -1