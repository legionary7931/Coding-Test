from collections import deque

def bfs(arr, N, M):
  answer = 0
  drow = [-1, 1, 0, 0] # 북 남 동 서
  dcol = [0, 0, 1, -1]
  
  queue = deque()
  queue.append([0, 0])
  arr[0][0] = -1 #시작점 방문 처리

  while(queue):
    v = queue.popleft()

    for i in range(4):
      nrow = v[0] + drow[i]
      ncol = v[1] + dcol[i]

      if(0<=nrow<N and 0<=ncol<M and arr[nrow][ncol] == 1):
        queue.append([nrow, ncol])
        arr[nrow][ncol] = -1

      if(nrow==N-1 and ncol==M-1):
        print(arr)
        return answer
    answer+=1
  
  return answer
        
N, M = map(int, input().split())
arr = []

for i in range(N):
  arr.append(list(map(int, input())))

print(bfs(arr, N, M))
