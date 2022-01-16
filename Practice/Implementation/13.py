"""
P332 치킨 배달
13. 치킨 배달(Implementation)
-> 1회차(O)), 2022/01/16
<Keypoint>
1. 옛날에 풀었던 치킨 배달 문제임.
2. 딱히 어려울 것 없고, 삼중 반복문 쓸때 어떤걸 기준으로 반복문을 돌릴것이냐 구현할 때 유의해야 함.
"""

from itertools import combinations

N, M = map(int, input().split())
arr = []

for i in range(N):
  arr.append(list(map(int, input().split())))

d_home, d_store = [], []

for i in range(N):
  for j in range(N):
    if(arr[i][j]==1): d_home.append([i, j])
    elif(arr[i][j]==2): d_store.append([i, j])

cnt = 0
dist_arr = []

while(cnt<M):
  cnt+=1

  stores_lists = list(combinations(d_store, cnt))
  #print(stores_lists)

  for stores_list in stores_lists:
    dist = 0
    for home in d_home:
      h_dist = 999999999
      for store in stores_list:
        if(h_dist>abs(home[0]-store[0]) + abs(home[1]-store[1])):
          h_dist = abs(home[0]-store[0]) + abs(home[1]-store[1])
      dist+=h_dist 
    dist_arr.append(dist)

#print(dist_arr)
print(min(dist_arr))



