"""
P315 볼링공 고르기 
5. 볼링공 고르기(Greedy Algorithm)
-> 1회차(?), 2021/12/29 -> 풀긴 했는데 그리디로 푼건 아닌거 같다.
<Keypoint> 
-> 그냥 간단한 확통 수학이다...
-> ex) 1 2 2 3 3 으로 볼링공이 있다고 가정하면,
-> 1(A가 1을 선택했을 때) * 4(B가 2또는 3을 선택했을 때) = 4
-> 2(A가 2를 선택했을 때) * 2(B가 3을 선택했을 때) = 4
-> 3(A가 3을 선택했을 때)) * 0(B는 선택할 것이 없음(이미 앞에서 다 고름))) = 0
따라서 4+4 = 8

"""
weight_num = [0] * 11

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for weight in arr:
  weight_num[weight]+=1

result = 0
for i in range(1, M+1):
  N -= weight_num[i]
  result += weight_num[i] * N

print(result)

"""
from itertools import combinations

N, M = map(int, input().split())
weights = list(map(int, input().split()))

data = []
for idx, weight in enumerate(weights):
  data.append([idx+1, weight])

result = list(combinations(data, 2))

for v in result:
  if(v[0][1] == v[1][1]): result.remove(v)

print(len(result))
"""

