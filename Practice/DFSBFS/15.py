"""
P339 특정 거리의 도시 찾기
15. 특정 거리의 도시 찾기 (BFS)
-> 1회차(O), 2022/01/26

TIP)
1. BFS로 거리 데이터 대입때 원리는 기억해둔다.
dist[vertex] = dist[d] + 1 <- 이런식으로 현재 출발점까지 온 거리에서 그 다음 vertex로 넘어갈때 거리를 더해주는 식이다.abs

2. sys.stdin.readline()은 input()대신 쓰는 함수로 생각해주면 된다.
(이거쓰면 input()쓰는 것 보다 거의 50%이상 빠르니 이걸 쓰는 걸 습관으로 들이자)
"""

import sys
from collections import deque

def bfs(arr, X): #X는 출발점
  dist = [99999999 for _ in range(N+1)]
  visit = [0 for _ in range(N+1)]
  queue = deque()

  dist[X] = 0
  visit[X] = 1
  queue.append(X) #출발점 데이터 초기화

  while(queue):
    d=queue.popleft()

    for vertex in arr[d]:
      if not visit[vertex]:
        visit[vertex]=1
        queue.append(vertex)
        dist[vertex] = dist[d] + 1

  return dist

N, M, K, X =  map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())
  arr[a].append(b)

dist = bfs(arr, X)
flag = -1

#print(dist)

for i in range(1, N+1):
  if(dist[i]==K): 
    flag = 1
    print(i)

if(flag==-1): print("-1")
