# 거의 풀었는데 구현을 못했다....

N, M = map(int, input().split())

arr = [0] * N
for i in range(N):
  arr[i] = int(input())

dp = [10001] * (M+1)
dp[0] = 0

for i in range(N):
  for j in range(arr[i], M+1):
    dp[j] = min(dp[j], dp[j-arr[i]]+1)

print(dp)
if(dp[M] == 10001): print("-1")
else: print(dp[M])
  
