"""
P313 문자열 뒤집기 (https://www.acmicpc.net/problem/1439)
3. 문자열 뒤집기(Greedy Algorithm)
-> 1회차(), 2021/12/28
<Keypoint> 
-> 1과 0의 덩어리를 찾아주는게 핵심이다.
"""


S = input()
cur_num = int(S[0])
data = [0, 0]
for idx, num in enumerate(S):
  if(idx==0): #처음에는
    cur_num = int(num)
    data[cur_num]+=1

  else:
    if(cur_num!=int(num)):
      cur_num = int(num)
      data[cur_num]+=1
    else: continue

print(min(data))



  
