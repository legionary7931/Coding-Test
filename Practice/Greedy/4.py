"""
P314 만들 수 없는 금액 (https://www.acmicpc.net/problem/2437)
4. 만들 수 없는 금액(Greedy Algorithm)
-> 1회차(X), 2021/12/28
<Keypoint> 
-> 그리디 알고리즘의 "누적합" 개념을 알아야만 해결 할 수 있는 문제이다.
<원리>
-> 누적합이 360인 n개의 수가 있다고 가정할 때 (이 말은 1~360까진 수의 합으로 나타낼 수 있음.)
1. n+1번째 수가 200이라면, 1+200 ~ 360+200 (201~560) 까지 합을 나타낼 수 있지만,
2. n+1번째 수가 400이라면, 1+400 ~ 360+400 (401~760) 까지 합을 나타낼 수 있다. 따라서 이말은 361~400까지는 정수의 합으로 만들어 낼 수 없음을 의미한다!!
"""
N = int(input())
arr = list(map(int, input().split()))

arr.sort()

target=1
for x in arr:
  if target<x:
    break
  target+=x

print(target)

"""
<실패 코드 - 메모리 초과>
combinations를 구한 리스트가 메모리를 너무 많이 잡아먹어서 그런 것 같다.

from itertools import combinations

N = int(input())
arr = list(map(int, input().split()))

arr.sort()

if(arr[0]!=1): print("1") #최솟값이 1이 아니라면 1은 죽었다 깨어나도 만들 수 없다.
else:
  able_cost = set()
  for i in range(1, N+1):
      v = list(combinations(arr, i))
      for data in v:
        able_cost.add(sum(data))

  target = 2
  while True:
    if(target not in able_cost):
      print(target)
      break
    else: target+=1

"""

