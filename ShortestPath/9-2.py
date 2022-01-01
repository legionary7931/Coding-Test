"""
< 개선된 다익스트라 알고리즘 > 
시간 복잡도 :  O(ElogV)
-> 기존 다익스트라 알고리즘은 최단 거리가 짧은 노드를 찾기 위해 선형탐색을 진행했고, 이 때문에
시간 복잡도가 O(V^2) 가 나왔다.
-> 개선된 다익스트라 알고리즘은 최단거리를 찾는 과정을 우선순위 큐(힙 자료구조로 운용)로 구현함. (Priority Queue, 혹은 Heapq를 사용하나, Heapq가 쓰기에는 좋다.)
-> 파이썬에서의 heap은 최소 힙 기준이다.
-> Heap의 데이터 삽입/삭제 시간 복잡도는 O(logN)이다.

-> 쉽게 말해서 9-1.py의 get_smallest_path 동작을 heap으로 대체했다는 것으로 보면 된다.
"""

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
start = int(input())
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)


for _ in range(M):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q = []
  heapq.heappush(q, (0, start)) # (거리, 노드)
  distance[start] = 0

  while q:
    # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼냄.
    dist, now = heapq.heappop(q)
    # 현재 노드가 이미 처리된 적이 있다면, 무시....
    if distance[now] < dist:
      continue

    for i in graph[now]: #그래프는 (노드, 거리의 형식.....)
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(distance)

