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
  for i in range(len(data)-1, -1, -1): #뒤부터 탐색하면서
    if(data[i]>max_val): #만일 현재가보다 그 전날들 값이 높았다면 이때 걸로 팔아야 이득
      max_val = data[i]
    else: #그 전날들 값이 낮았다면 갖고 있다가 max 찍을때 파는게 이득 
      profit+=(max_val-data[i])

  print(profit)
