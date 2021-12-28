"""
#2021.12.26 226p 효율적인 화폐 구성
N, M = map(int, input().split())

arr = []
for i in range(N):
  arr.append(int(input()))
print(arr)


dp = [10001] * (M+1)
dp[0] = 0

for i in range(N): #coin을 기준으로 
  for j in range(arr[i], M+1): #전체 dp를 싹 돌린다.
    dp[j] = min(dp[j], dp[j-arr[i]]+1)
#그 후 coin 바꿔가면서 기존에 다른 코인보다 적은 개수로 금액을 만들수 있는지 확인해준다.
print(dp)

if(dp[M] == 10001): print("-1")
else: print(dp[M])
"""

"""
#2021.12.26 223p 바닥 공사 rewind
N = int(input())
dp = [0] * (N+1)

dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
  dp[i] = dp[i-1] + 2*dp[i-2]

print(dp)
print(dp[N])
"""

"""
2021.12.26 220p 개미 전사 rewind
N = int(input())
arr = list(map(int, input().split()))

dp = [0] * (N+1)

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, N):
  dp[i] = max(dp[i-1], dp[i-2]+arr[i])

print(dp)
print(dp[N-1])
"""
"""
2021.12.26 217p 1로 만들기 rewind
X = int(input())

dp = [0] * (X+1)

for i in range(2, X+1):
  dp[i] = dp[i-1]+1

  if(i%5==0): dp[i] = min(dp[i], dp[i//5]+1)
  if(i%3==0): dp[i] = min(dp[i], dp[i//3]+1)
  if(i%2==0): dp[i] = min(dp[i], dp[i//2]+1)

print(dp)
print(dp[X])


"""



