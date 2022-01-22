"""
P351
20. 감시 피하기 (DFSBFS)
-> 1회차(o), 2022/01/22

TIP) 

이 문제는 BFS DFS문제라 하기엔 좀....
애초에 책조차 BFS DFS로 풀질 않았다.

선생님들의 감시 범위는 상하좌우이지 바이러스 문제 마냥
퍼져 나가는게 아니기 때문에 bfs, dfs를 쓸 이유가 없으며
그냥 정석적으로 감시 되는지 안되는지 판단만 해주면 된다.

그냥 python의 combinations 사용 방법에 대해서만 숙지해두자.

"""

from itertools import combinations

def watch(direction, srow, scol):
  if direction==0: #북쪽으로 이동
    while(srow>0):
      srow-=1
      if(arr[srow][scol]=='S'): return False #이러면 들킴
      elif(arr[srow][scol]=='O'): break

  elif direction==1: #동쪽으로 이동
    while(scol<N-1):
      scol+=1
      if(arr[srow][scol]=='S'): return False #이러면 들킴
      elif(arr[srow][scol]=='O'): break

  elif direction==2: #남쪽으로 이동
    while(srow<N-1):
      srow+=1
      if(arr[srow][scol]=='S'): return False #이러면 들킴
      elif(arr[srow][scol]=='O'): break

  elif direction==3: #서쪽으로 이동
    while(scol>0):
      scol-=1
      if(arr[srow][scol]=='S'): return False #이러면 들킴
      elif(arr[srow][scol]=='O'): break

  return True

def solve():
  for datas in obstacle_locs: #data : 3개 장애물 좌표들 tuple
    for data in datas: #obstacle: 장애물 개별 좌표
      arr[data[0]][data[1]] = 'O'
    # 장애물 세움

    for teacher in teacher_locs:
      for i in range(4):
        re = watch(i, teacher[0], teacher[1])
        if(re==False): break #만약 들키는 경우가 있다면 해당 장애물 case에 대해선 더이상 볼 필요가 없음.
      if(re==False): break

    if(re==True):
      return "YES"

    for data in datas: #obstacle: 장애물 개별 좌표
      arr[data[0]][data[1]] = 'X' #다시 원상복구

  return "NO"

N = int(input())

arr = []
for i in range(N):
  arr.append(list(map(str, input().split())))

teacher_locs = []
blank_locs = []
for i in range(N):
  for j in range(N):
    if(arr[i][j]=='X'): blank_locs.append([i, j])
    if(arr[i][j]=='T'): teacher_locs.append([i, j])

obstacle_locs = list(combinations(blank_locs, 3))

print(solve())