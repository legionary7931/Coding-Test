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
arr[r][c] = -1 #시작점 방문처리 => 시작점에 대해서 처리를 해주는 습관을 항상 들이자.
turn_num = 0

while True:
  d = turn_left(d)

  nrow = r + drow[d]
  ncol = c + dcol[d]

  if(0<=nrow<N and 0<=ncol<M): # 범위 처리!!!!!!
    if(arr[nrow][ncol] == 0): # 0이 빈칸
      arr[nrow][ncol] = -1
      turn_num=0
      answer+=1
      r = nrow
      c = ncol
      continue
    else: turn_num += 1 # 빈칸이 아니고 벽이거나 이미 간 지점이면 회전 횟수를 더해주어야 한다.
  else: turn_num += 1 # 범위가 안맞아도 갈 수 없는 지점이므로 회전 횟수를 더해주어야 한다.

  if(turn_num == 4):
    turn_num = 0 # 회전횟수는 일단 초기화 되어야 한다.

    nrow = r - drow[d] # 발상: 뒤로 가는 것은 어떻게 구현할 것인가?
    ncol = c - dcol[d]
    
    if(0<=nrow<N and 0<=ncol<M): #범위 처리는 언제나 중요
      if(arr[nrow][ncol] != 1): #벽만 아니라면 이미 지나간 곳이라도 상관없다.
        r = nrow
        c = ncol 
      else: break
    else: break

print(answer)
