"""
<Top-down, Bottom-up 방식>
1. Top-down: 큰 문제를 작은 문제로 나누어 해결
(현재 이 소스코드가 Top-down방식으로 피보나치 문제를 해결한 것이다.)
2. Bottom-up: 작은 문제부터 차근차근 위로 답을 도출하는 형태
"""

# Bottom-up에선 memoization이라 안하고 보통 dp 테이블이라는 말을 사용함.
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1):
  d[i] = d[i-2] + d[i-1]

print(d[n])