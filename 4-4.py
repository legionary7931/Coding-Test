# P118 실전 문제 게임 개발
# 시간 제한 1초 / 풀이 시간 40분

# 솔직히 쉽다... 다시 풀어보자....
def turn_left():
  global direction
  direction -= 1
  if(direction == -1):
    direction = 3



n, m = map(int, input().split())

visit = [[0] * m for _ in range(n)] # 방문 체크
col, row, direction = map(int, input().split()) # x : 열 y : 행
visit[row][col] = 1

arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

answer = 1
turn = 0
while True:
  turn_left()
  nrow = row + drow[direction]
  ncol = col + dcol[direction]

  if(arr[nrow][ncol] == 0 and visit[nrow][ncol] == 0):
    visit[nrow][ncol] = 1
    answer += 1
    row = nrow
    col = ncol
    turn = 0
    continue
  else: turn += 1

  if turn==4:
    nrow = row - drow[direction]
    ncol = col - dcol[direction]

    if(arr[nrow][ncol] == 0):
      row = nrow
      col = ncol
    else: break
    turn = 0

print(visit)
print(answer)


  
