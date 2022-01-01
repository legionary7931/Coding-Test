import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
N, M, C = map(int, input().split())

distance = [INF] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
  a, b, c = map(int, input().split())
  graph[a].append((b, c)) #도착점, 거리

def dijkstra(start):
  q = []

  distance[start] = 0
  heapq.heappush(q, (0, start)) #거리, 시작점

  while q:
    dist, now = heapq.heappop(q)

    if(distance[now]<dist):
      continue
    
    for v in graph[now]:
      cost = dist + v[1]
      
      if(cost<distance[v[0]]):
        distance[v[0]] = cost
        heapq.heappush(q, (cost, v[0]))

dijkstra(C)

city_num = 0
max_val = -1

for i in range(1, len(distance)-1):
  if(max_val<distance[i] and distance[i]!=INF):
    max_val = distance[i]
  
  if(distance[i]!=INF): city_num+=1

print(city_num, max_val)
  