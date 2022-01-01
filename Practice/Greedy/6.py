"""
P316 무지의 먹방 라이브 
6. 무지의 먹방 라이브 (Greedy Algorithm)
-> 1회차(?), 2021/12/29 
<Keypoint> 

"""
def solution(food_times, k):
  sec, idx = -1, -1

  while(sec<=k):
    sec+=1
    idx+=1

    if(idx==len(food_times)): idx=0
    if(food_times[idx]==0):
      continue
    else:
      food_times[idx]-=1

    print(sec, idx, food_times)
    
  return idx+1





food_times = list(map(int, input().split()))
k = int(input())

print(solution(food_times, k))

