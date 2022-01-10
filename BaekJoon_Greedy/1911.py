"""
<그리디 알고리즘을 해결하는 그날까지....??>
Silver I 1911(https://www.acmicpc.net/problem/1911)
2022. 01. 02

그저 간단한 구현 문제에 불과....
1. 그리디 문제 풀 때 sort 생각해주는건 기본이다.
2. 그리디는 아이디어를 요구 할 수도 있지만, 정말 간단하게 문제에서 요구하는 그대로 구현해도 된다.
"""
import math
N, L = map(int, input().split())
road = []

for _ in range(N):
  a, b = map(int, input().split())
  road.append((a, b))
road.sort(key = lambda x : x[0])

maxPlankIndex = 0
plankCount = 0
for start, end in road:
  if start<=maxPlankIndex:
    # 만일 start<=maxPlankIndex라면 웅덩이 중간까지만 채우고 말았다는 걸 의미한다. 그렇다면 start = max+1로 업데이트
    start=maxPlankIndex+1

  curPlankCount = math.ceil((end-start)/L)
  # 웅덩이의 시작과 끝을 받아서, 웅덩이의 길이를 판자 길이로 나눈 값이 판자 필요 값이 된다.
  plankCount += curPlankCount
  maxPlankIndex = start+curPlankCount*L-1
  # -> 그 후 판자가 채워진 가장 최대의 idx를 시작점+판자개수*판자 길이 -1로 업데이트 한다.

print(plankCount)


# 아이디어가 떠오르지 않는다면 정직하게 구현해보는 것도 방법이다......