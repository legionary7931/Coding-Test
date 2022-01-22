"""
P345 괄호 변환
19. 연산자 끼워넣기 (DFSBFS)
-> 1회차(X), 2022/01/22

TIP)
1. 사실 이거도 dfs의 느낌보다는 재귀 문제의 느낌이 강한 문제였다.
2. 재귀를 보면 머리가 굳는 문제가 있는거 같은데 빨리 한문제를 풀 수 있길.....
"""

import sys

def dfs(i, now):
  global max_val, min_val, add, sub, mul, div

  if i==N:
    max_val = max(max_val, now)
    min_val = min(min_val, now)

  if add>0:
    add-=1
    dfs(i+1, now+nums[i]) # i는 1부터 시작하기 때문에 nums[i]로 연산해주어야 한다.
    add+=1

  if sub>0:
    sub-=1
    dfs(i+1, now-nums[i])
    sub+=1
  
  if mul>0:
    mul-=1
    dfs(i+1, now*nums[i])
    mul+=1
  
  if div>0:
    div-=1
    dfs(i+1, int(now/nums[i]))
    div+=1

N = int(input())
nums = list(map(int, sys.stdin.readline().split()))
add, sub, mul, div = map(int, sys.stdin.readline().split())

max_val = -int(1e9)
min_val = int(1e9)

dfs(1, nums[0])

print(max_val)
print(min_val)