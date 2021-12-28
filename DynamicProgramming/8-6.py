# 220p 개미 전사
# Dynamic Programming, 시간 지나고 다시 풀어보기....

N = int(input())
arr = list(map(int, input().split()))

dp = [0]*100

dp[0] = arr[0]
dp[1] = max(arr[0], arr[1])

for i in range(2, N):
  dp[i] = max(dp[i-1], dp[i-2]+arr[i])

print(dp[N-1])
