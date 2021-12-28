"""
Dynamic Programming의 기초

<사용 조건>
1. 큰 문제를 작은 문제로 나누는 것이 가능하다.
2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

-> 피보나치 수열을 통해 알아 보자.

<Top-down, Bottom-up 방식>
1. Top-down: 큰 문제를 작은 문제로 나누어 해결
(현재 이 소스코드가 Top-down방식으로 피보나치 문제를 해결한 것이다.)
2. Bottom-up: 작은 문제부터 차근차근 위로 답을 도출하는 형태

"""

d = [0]*100
# Memoization 기법을 활용 (이미 구한 값에 대해서 저장해 두고 그 뒤에 이 값이 필요할 때 저장해둔 데이터를 사용)

def fibo(x):
  if(x==1 or x==2): return 1

  if(d[x]!=0): return d[x]

  d[x] = fibo(x-1)+fibo(x-2)
  return d[x]

print(fibo(500))