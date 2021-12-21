array = [7, 5, 9, 0, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j]<array[j-1]: #더 작은 숫자가 나올 때까지 자리 바꾸기
      array[j], array[j-1] = array[j-1], array[j]
    else: break 

print(array)