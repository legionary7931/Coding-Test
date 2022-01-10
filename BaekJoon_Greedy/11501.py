"""
<그리디 알고리즘을 해결하는 그날까지....??>
Silver II 주식 (https://www.acmicpc.net/problem/11501)
2022. 01. 02
1. sort도 해보는게 좋을 수 있지만,
2. 뒤에서부터 배열을 볼 수 있는데 이건 왜 안 해봤는가? 
(물론 sort로 해보는건 좋은 시도이긴 했지만, 영 안된다 싶으면 다른 쪽으로 시도해봤어야 됐다....)
"""

T = int(input())

for _ in range(T):
  N = int(input())
  data = list(map(int, input().split()))

  profit = 0

  max_val = -1
  for i in range(len(data)-1, -1, -1):
    if(data[i]>max_val):
      max_val = data[i]
    else:
      profit+=(max_val-data[i])

  print(profit)
