"""
별거 없다.... 그냥 플로이드 워셜 알고리즘 쓰면 바로 풀림
"""

INF = int(1e9)
V, E = map(int, input().split())

graph =[[INF]*(V+1) for _ in range(V+1)]

for i in range(1, V+1):
  for j in range(1, V+1):
    if(i==j): graph[i][j] = 0

for _ in range(E):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1 # 양방향이라 둘다 해주어야 한다.

X, K = map(int, input().split())
# K: 중간에 방문, X: 최종 목표지점

for k in range(1, V+1):
  for a in range(1, V+1):
    for b in range(1, V+1):
      graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])


if(graph[1][K] != INF and graph[K][X] != INF): 
  print(graph[1][K] + graph[K][X])
else: print("-1")