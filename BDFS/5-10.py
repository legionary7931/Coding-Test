from collections import deque

def bfs(arr, row, col):
  drow = [-1, 1, 0, 0] # 북 남 동 서
  dcol = [0, 0, 1, -1]


  queue = deque()
  queue.append([row, col])
  arr[row][col] = -1 # visit 처리

  while(queue):
    v = queue.popleft()

    for i in range(4):
      nrow = v[0]  + drow[i] #이거를 i대신 0으로 써서 헤맸다....
      ncol = v[1] + dcol[i]

      if(0<=nrow<M and 0<=ncol<N and [nrow, ncol] not in queue):
        if(arr[nrow][ncol]==0):
          arr[nrow][ncol] = - 1
          queue.append([nrow, ncol])
  return arr
        
N, M = map(int, input().split())
arr = []

for i in range(M):
  arr.append(list(map(int, input())))

ice_num = 0
for i in range(M):
  for j in range(N):
    if(arr[i][j] == 0):
      arr = bfs(arr, i, j)
      ice_num+=1



print(ice_num)