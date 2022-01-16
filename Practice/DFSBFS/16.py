"""
옛날에 풀었던 거네.... (2022.01.16 한 번더품)
"""

from itertools import combinations
from copy import deepcopy
from collections import deque

def bfs(arr, scenario, v_pos):
  tmp_arr = deepcopy(arr)
  
  dcol = [1, -1, 0, 0] #동 서 남 북
  drow = [0, 0, 1, -1] #동 서 남 북


  for case in scenario:
    tmp_arr[case[0]][case[1]]=1 # 벽을 세워준다.

  for start in v_pos:
    queue = deque([start])

    while(queue):
      v = queue.popleft()
      now_r, now_c = v[0], v[1]

      for i in range(4):
        next_r = now_r + drow[i]
        next_c = now_c + dcol[i]

        if(next_r<0 or next_c<0 or next_r>=N or next_c>=M): continue
        else:
          if(tmp_arr[next_r][next_c]==0):
            tmp_arr[next_r][next_c] = 2
            queue.append([next_r, next_c])

  area_result = 0
  for i in range(N):
    for j in range(M):
      if(tmp_arr[i][j]==0): area_result+=1

  """
  for i in range(N):
    for j in range(M):
      print(tmp_arr[i][j], end = " ")
    print()
  print()
  """
  return area_result
          
N, M = map(int, input().split()) #N=세로, M=가로
arr = []

for i in range(N):
  arr.append(list(map(int, input().split())))

v_pos = [] # 바이러스 좌표
b_pos = [] # 빈칸 좌표

for i in range(N):
  for j in range(M):
    if(arr[i][j]==2): v_pos.append([i, j])
    elif(arr[i][j]==0): b_pos.append([i, j])

wall_scenarios = list(combinations(b_pos, 3))
area = []

for scenario in wall_scenarios:
  area.append(bfs(arr, scenario, v_pos))

print(max(area))