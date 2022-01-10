"""
P327 뱀
11. 뱀(Implementation)
-> 1회차(O), 2022/01/10
<Keypoint> 
-> 방향 전환을 어떻게 효율적으로 짤 것인가?
  -> 동 남 서 북의 순서 잘 기억하고 왼쪽으로 꺾냐, 오른쪽으로 꺽냐에 따라 나머지 연산 진행해준다.
-> 뱀의 몸 충돌은 어떻게 처리 할 것인가?
  -> 처음에는 snake의 좌표를 정리한 큐에서 중복 좌표를 계산해서 할 생각이었지만, 그렇게는 시간복잡도가 너무 높을 것 같다.
  -> 그냥 뱀의 위치를 보드 상에 표시하고, board[new_row][new_col]값이 뱀 몸통값(2)랑 같은지만 판단해주면 효율적으로 구현이 가능했다.
"""




from collections import deque

def change_dir(row_dir, col_dir, new_dir): # 방향 전환 구현함수 잘 알아두기
  drow = [0, 1, 0, -1] # 동 남 서 북
  dcol = [1, 0, -1, 0] # 동 남 서 북

  for i in range(4):
    if(row_dir==drow[i] and col_dir==dcol[i]):
      direction = i

  if(new_dir=='L'):
    direction = (direction-1) % 4
  elif(new_dir=='D'):
    direction = (direction+1) % 4

  return drow[direction], dcol[direction]

N = int(input()) # 보드의 크기
K = int(input()) # 사과의 크기

board = [[0] * (N+1) for _ in range(N+1)]
for _ in range(K):
  a, b = map(int, input().split())
  board[a][b] = 1

L = int(input()) #뱀의 방향 전환 횟수
dir_data = []
for _ in range(L):
  a, b = map(str, input().split())
  dir_data.append([int(a), b])

snake = deque([[1, 1]]) #머리는 idx=0 (popleft), 꼬리는 idx=len(snake)-1(pop)
board[1][1] = 2 #2는 뱀의 몸통
row_dir, col_dir = 0, 1 #뱀은 오른쪽을 향한다.

sec = 0

while True:
  sec+=1
  cur_row = snake[0][0] #현재 머리 좌표 저장
  cur_col = snake[0][1]

  new_row = cur_row + row_dir
  new_col = cur_col + col_dir
  
  # 범위 처리 
  if(new_row<1 or new_col<1 or new_row>N or new_col>N): # 범위 처리
    print(sec)
    break
  
  # 뱀 몸통 충돌 처리 (큐에 저장된 걸로 판단하려면 시간복잡도 너무 높다..)
  if(board[new_row][new_col]==2):
    print(sec)
    break
  
  if(board[new_row][new_col]==1): #사과를 먹었을 때
    snake.appendleft([new_row, new_col]) #머리 늘려주고
    board[new_row][new_col] = 2 #사과 먹음 처리하고 보드 상에서 뱀의 머리로 처리

  elif(board[new_row][new_col]==0): #사과가 아니라면
    snake.appendleft([new_row, new_col]) # 머리 늘려주고
    board[new_row][new_col] = 2 # 보드에서 머리 처리
    last = snake.pop() # 꼬리가 삭제.
    board[last[0]][last[1]] = 0 # 꼬리 삭제 보드 상에서 최신화

  # 뱀 이동 완료, 이제 뱀 방향 
  if(len(dir_data)!= 0 and sec==dir_data[0][0]): #뱀의 방향전환이 식별 될 시
    row_dir, col_dir = change_dir(row_dir, col_dir, dir_data[0][1])
    dir_data.pop(0) #처리한 데이터는 삭제
