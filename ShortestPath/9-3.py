"""
< 플로이드-워셜 알고리즘 > 
시간 복잡도 :  O(N^3))
-> 기존 다익스트라 알고리즘은 특정 한 지점에서 다른 한지점까지의 최단 거리를 구할 때 사용하는 알고리즘이라면,
-> 플로이드-워셜 알고리즘은 모든 지점에서 다른 모든 지점까지의 최단 거리를 구할 때 사용하는 알고리즘이다.
-> 시간 복잡도가 꽤 크기 때문에 input크기가 작을때만 사용하는게 좋을 것 같다.
"""

import sys

input = sys.stdin.readline
V, E = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (V+1) for _ in range(V+1)]

for a in range(V+1):
  for b in range(V+1):
    if(a==b): graph[a][b] = 0

for _ in range(E):
  a, b, c = map(int, input().split())
  graph[a][b] = c

for k in range(V+1):
  for a in range(V+1):
    for b in range(V+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)
