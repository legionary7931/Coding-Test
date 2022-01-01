# 가장 간단한 다익스트라 알고리즘
# 시간 복잡도 : O(N^2)
# Why? 정점을 한바퀴 돌면서 최단 거리가 가장 짧은 노드를 선택해주어야 하고, 현재 노드와 연결된 도착 노드들을 일일히 확인해 주어야 하기 때문이다.

import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
N, M = map(int, input().split())
# 출발 노드 번호를 입력받기
start = int(input())
# 그래프 만들어 주기
graph = [[] for i in range(N+1)]
# 방문 확인하는 리스트 만들어주기
visit = [False] * (N+1)
# 최단 거리 리스트 초기화
distance = [INF] * (N+1)

for _ in range(M):
  a, b, c = map(int, input().split()) # a->b로 가는데 비용이 c라는 의미
  graph[a].append((b, c)) # (도착점, 간선 거리)

def get_smallest_node():
  min_dist = INF
  idx = 0

  for i in range(1, N+1):
    if(distance[i]<min_dist and not visit[i]):
      min_dist = distance[i]
      idx = i

  return idx

def dijkstra(start):
  distance[start] = 0 # 출발점에서 출발점까지의 최단 거리는 0
  visit[start] = True # 출발점 방문 처리
  for v in graph[start]:
    distance[v[0]] = v[1] # 출발점과 연결된 정점과의 거리를 초기화

  for i in range(N-1): # 출발점 제외한 n-1개의 노드에 대해 반복
    now = get_smallest_node()
    visit[now] = True

    for v in graph[now]:
      cost = distance[now] + v[1] 
      # distance[now] = 출발점부터 현재 정점까지의 거리, v[1] = 현재 정점부터 현재 정점과 연결된 다른 정점과의 거리 
      if(cost<distance[v[0]]):
        distance[v[0]] = cost

dijkstra(start)

print(distance)