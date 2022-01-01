"""
P312 곱하기 혹은 더하기
2. 곱하기 혹은 더하기(Greedy Algorithm)
-> 1회차(O), 2021/12/28
<Keypoint> 
-> 0, 1이면 더하는게 무조건 이득이고, 그 이상이면 무조건 곱해야지만 최대값을 만들어 낼 수 있다.
"""

data = input()
result = 0

for idx, num in enumerate(data):
  if(idx==0): result = int(num) #처음에는 연산할게 없다.
  else:
    if(result<=1 or int(num)<=1): #0,1은 무조건 더해주는게 이득이다.
      result+=int(num)
    else: #그 외에는 무조건 곱해주는게 이득이다.
      result*=int(num)

print(result)
