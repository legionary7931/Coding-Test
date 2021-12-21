#2021.12.09 백준 GoldV 로봇청소기(14503, https://www.acmicpc.net/problem/14503)

def turn_left(direction):
  if(direction==0): direction = 3
  else: direction -= 1

  return direction

arr = []
N, M = map(int, input().split())
r, c, d = map(int, input().split())

drow = [-1, 0, 1, 0] # 북 동 남 서
dcol = [0, 1, 0, -1] # 북 동 남 서


for i in range(N):
  arr.append(list(map(int, input().split())))

answer = 1
arr[r][c] = -1 #시작점 방문처리
turn_num = 0

while True:
  d = turn_left(d)

  nrow = r + drow[d]
  ncol = c + dcol[d]

  if(0<=nrow<N and 0<=ncol<M): #범위 처리!!!!!!
    if(arr[nrow][ncol] == 0): #0이 빈칸
      arr[nrow][ncol] = -1
      turn_num=0
      answer+=1
      r = nrow
      c = ncol
      continue
    else: turn_num += 1
  else: turn_num += 1

  if(turn_num == 4):
    turn_num = 0

    nrow = r - drow[d]
    ncol = c - dcol[d]
    
    if(0<=nrow<N and 0<=ncol<M):
      if(arr[nrow][ncol] != 1):
        r = nrow
        c = ncol

      else: break
    else: break

print(answer)

