#197p 부품 찾기 - 계수 정렬을 이용해서 풀어봄.

N = int(input())
arr = list(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

data = [0]*1000001
for i in arr:
  data[i]+=1

for target in targets:
  if(data[target]==1): print("yes", end = " ")
  else: print("no", end = " ")

  