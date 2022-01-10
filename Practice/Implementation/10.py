"""
P325 자물쇠와 열쇠
10. 자물쇠와 열쇠(Implementation)
-> 1회차(X/O), 2022/01/10
<Keypoint> 
-> M, N의 범위가 매우 작은 것으로 보아 브루트 포스 형식의 완전탐색이라는 것을 인지해주어야 한다.
-> 사실 아이디어는 그렇게 어렵지 않고, lock을 3배 정도로 늘려 key가 들어갈 자리를 맞추어 주는게 포인트!
-> 이차원 배열의 rotate 함수는 기억해두어서 나쁠것이 없을 것 같다.

<중요> data = list(map(int, input()))

def rotate(a):
  n = len(a) # 행 길이 계산
  m = len(a[0]) # 열 길이 계산

  result = [[0] * n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  
  return result

"""
"""
<디버그용 함수>
def debug_print(length, arr):
  for i in range(length):
    for j in range(length):
      print(arr[i][j], end=" ")
    print()
"""
def rotate(a):
  n = len(a) # 행 길이 계산
  m = len(a[0]) # 열 길이 계산

  result = [[0] * n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  
  return result
  

def check(lock):
  length = len(lock)//3

  for i in range(length, 2*length):
    for j in range(length, 2*length):
      if(lock[i][j]!=1): return False

  return True

def solution(key, lock):
  M = len(key)
  N = len(lock)

  new_lock = [[0] * (N*3) for _ in range(N*3)]

  for i in range(N, N*2):
    for j in range(N, N*2):
      new_lock[i][j] += lock[i-N][j-N]
  
  for rotation in range(4):
    key = rotate(key)

    for x in range(N*2):
      for y in range(N*2): # 이 반복문은 new_lock의 어느 지점부터 key를 갖다 놓을지를 결정함.

        for i in range(M): # 이 반복문은 key 범위만큼 new_lock에 key를 꽂는 반복문임.
          for j in range(M):
            new_lock[x+i][y+j] += key[i][j]

        #debug_print(N*3, new_lock)
        #print()

        if(check(new_lock) == True):
          return True

        for i in range(M): #만일 key가 맞지 않는다면 원상태로 원복되어야 함.
          for j in range(M):
            new_lock[x+i][y+j] -= key[i][j]

  return False 

      



















M = int(input()) #key
N = int(input()) #lock

key = [[] for _ in range(M)]
lock = [[] for _ in range(N)]

for i in range(M):
  key[i] = list(map(int, input().split()))

for i in range(N):
  lock[i] = list(map(int, input().split()))

print(solution(key, lock))

