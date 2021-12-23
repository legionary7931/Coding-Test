# 사실상 답보고 끼워 맞춘 문제.... 구현력을 좀 더 높일 필요가 있겠다...

# <Data>
# 서로 맞닿은 톱니의 극이 다르다면, B는 A가 회전한 방향과 반대방향으로 회전하게 된다.
# 맞닿은 극이 같거나, 회전하지 않는다면 회전하지 않는다.
# 1은 시계방향, -1은 반시계 방향

# <Idea>
# (wheels[0][2] : wheels[1][6]), (wheels[1][2] : wheel[2][6]), (wheels[2][2] : wheels[3][6]) -> 맞닿아 있는 톱니바퀴들

def rotate(wheel, dir):
  if(dir==-1): return wheel[1:]+[wheel[0]] #반시계
  elif(dir==1): return [wheel[-1]] + wheel[0:-1] #시계

def check_left(turn, dir): #turn은 돌린 톱니바퀴의 왼쪽... 따라서 오른쪽 톱니바퀴랑 비교해주어야 한다.
  #print("left turn: {} dir: {}".format(turn, dir))
  if(turn<0 or wheels[turn][2] == wheels[turn+1][6]):
    return
  
  if(wheels[turn][2] != wheels[turn+1][6]):
    check_left(turn-1, -dir)
    wheels[turn] = rotate(wheels[turn], dir)

def check_right(turn, dir):#turn은 돌린 톱니바퀴의 오른쪽... 따라서 왼쪽 톱니바퀴랑 비교해주어야 한다.
  if(turn>3 or wheels[turn-1][2] == wheels[turn][6]):
    return
  
  if(wheels[turn-1][2] != wheels[turn][6]):
    check_right(turn+1, -dir)
    wheels[turn] = rotate(wheels[turn], dir)

def get_score(wheels):
  answer = 0
  if(wheels[0][0] == 1): answer+=1
  if(wheels[1][0] == 1): answer+=2
  if(wheels[2][0] == 1): answer+=4
  if(wheels[3][0] == 1): answer+=8

  return answer

wheels = []
for _ in range(4):
  wheels.append([int(a) for a in input()])

K = int(input())
for i in range(K):
  turn, direction = map(int, input().split())
  turn-=1 #arr의 idx로 맞춰주기 위함.
  
  check_left(turn-1, -direction)
  check_right(turn+1, -direction)
  
  wheels[turn] = rotate(wheels[turn], direction)

print(get_score(wheels))
















