N, K = map(int, input().split())

arrA = list(map(int, input().split()))
arrB = list(map(int, input().split()))

arrA.sort()
arrB.sort(reverse=True)

answer = 0
for i in range(K):
  if(arrA[i] < arrB[i]):
    arrA[i], arrB[i] = arrB[i], arrA[i]
  else: break
  
for num in arrA:
  answer+=num

print(answer)