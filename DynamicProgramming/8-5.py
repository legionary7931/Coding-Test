# 217p 1로 만들기
x = int(input())

dp = [0] * 30001
# dp[1] => 1에서 1로 만들어졌으니 dp[1] = 0이다.

for i in range(2, x+1):
  dp[i] = dp[i-1]+1 #일단 1뺀거를 기준으로

  if(i%2==0):
    dp[i] = min(dp[i], dp[i//2]+1)
  elif(i%3==0):
    dp[i] = min(dp[i], dp[i//3]+1)
  elif(i%5==0):
    dp[i] = min(dp[i], dp[i//5]+1)
  
  # 1뺀거보다 어떤 연산을 취했을 때가 더 작은지를 본다.
print(dp[x])

#해당 코드는 작은 문제에서 큰 문제로 차근차근 올라가는 방식이므로 Bottom-up 방식에 해당한다.