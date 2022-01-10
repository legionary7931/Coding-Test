N = int(input())
data = []

for i in range(N):
  num = int(input())
  data.append(num)
  
data.sort()

result, standard = 0, 1
for rank in data:
  result += abs(rank-standard)
  standard+=1

print(result)


