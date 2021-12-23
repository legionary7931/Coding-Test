#2021.12.09 백준 GoldV 연구소(14502, https://www.acmicpc.net/problem/14502)
# Idea
# 벽을 세우는 것이 case의 기준
# combinations 사용하여 벽을 세우고, virus 위치에 대해 bfs 돌려서 바이러스 퍼지는 것 판단하여 총 개수 더함.d


from itertools import combinations
from collections import deque
import copy

def bfs(c, arr, virus):
  case = copy.deepcopy(arr)

  for x, y in c:
    case[x][y] = 1 # 해당 벽을 세우는 case를 만들어냄

  drows = [0, 0, 1, -1] # 동 서 남 북
  dcols = [1, -1, 0, 0]

  for vir in virus:
    queue = deque()
    vir_row, vir_col = vir[0], vir[1]

    queue.append([vir_row, vir_col]) # 바이러스가 있는 곳이 곧 start 지점

    while(queue):
      v = queue.popleft()

      cur_row, cur_col = v[0], v[1]

      for i in range(4):
        nrow = cur_row + drows[i]
        ncol = cur_col + dcols[i]

        if(0<=nrow<N and 0<=ncol<M):
          if(case[nrow][ncol] == 0):
            queue.append([nrow, ncol])
            case[nrow][ncol] = 2
  
  answer = 0
  for i in range(N):
    for j in range(M):
      if(case[i][j] == 0): answer+=1
  
  return answer

N, M = map(int, input().split()) #N은 세로 / M은 가로
arr = []

for i in range(N):
  arr.append(list(map(int, input().split())))

virus = [] #바이러스가 있는 위치 저장.
blank = [] #벽을 세울 수 있는 위치 저장.

for i in range(N):
  for j in range(M):
    if(arr[i][j] == 2): virus.append([i, j])
    elif(arr[i][j] == 0): blank.append([i, j])

answer = -1
safe_area = 0
for c in combinations(blank, 3):
  safe_area = bfs(c, arr, virus)
  if(safe_area>answer): answer = safe_area

print(answer)



   
