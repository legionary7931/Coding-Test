"""
P345 경쟁적 전염
17. 경쟁적 전염 (DFSBFS)
-> 1회차(O), 2022/01/18

TIP)
1. BFS로 거리 데이터 대입때 원리는 기억해둔다.
dist[vertex] = dist[d] + 1 <- 이런식으로 현재 출발점까지 온 거리에서 그 다음 vertex로 넘어갈때 거리를 더해주는 식이다.abs

2. sys.stdin.readline()은 input()대신 쓰는 함수로 생각해주면 된다.
(이거쓰면 input()쓰는 것 보다 거의 50%이상 빠르니 이걸 쓰는 걸 습관으로 들이자 

-> 15번에서 나온 TIP들인데, 이 TIP들은 이 문제에서도 유용했으니 잘 기억해두자.

3. 이 문제는 queue의 FILO를 활용하는 문제였다. 예제 case에서 1번 바이러스가 먼저 퍼져나가지만, 우리가 확인해야 할 그다음은 2번 바이러스와 3번 바이러스의 확산 위치이다. 이걸 queue를 통해 구현하면 매우 쉽게 구현할 수 있다ㅏㅏㅏ
"""
from collections import deque
import sys

def bfs(arr, S):
  queue = deque()
  
  start = [] #시작 포인트를 바이러스 순서에 맞게 queue에 넣기 위한 임시 list
  for i in range(N):
    for j in range(N):
      if(arr[i][j]!=0): 
        start.append([i, j, arr[i][j]])

  start.sort(key=lambda x : x[2])

  for p_start in start:
    p_start.pop(2) # 맨 마지막 필요없는 바이러스 정보 제외
    queue.append(p_start + [0]) # 초의 정보까지 저장 (해당 점들은 0초일때 추가된 point임을 의미)

  drow = [0, 0, 1, -1] # 동 서 남 북
  dcol = [1, -1, 0, 0] # 동 서 남 북  
  while(queue):
    d = queue.popleft()
    c_row, c_col, c_vir, c_sec = d[0], d[1], arr[d[0]][d[1]], d[2]

    if(c_sec==S): break

    for i in range(4):
      n_row = c_row + drow[i]
      n_col = c_col + dcol[i]
      n_sec = c_sec+1

      if(n_row<0 or n_col<0 or n_row>=N or n_col>=N): continue

      if(arr[n_row][n_col]==0):
        arr[n_row][n_col] = c_vir
        queue.append([n_row, n_col, n_sec])
  
  return arr

# N은 맵의 크기, K는 바이러스 종류
N, K = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
  arr.append(list(map(int, sys.stdin.readline().split())))

S, X, Y = map(int, sys.stdin.readline().split())

arr = bfs(arr, S)

print(arr[X-1][Y-1]) #문제는 1행 1열부터 시작하기 때문에 좌표 1씩 빼서 답 형식이랑 맞춰줌


