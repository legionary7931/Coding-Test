array = [7, 5, 9, 0, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min = i
  for j in range(i+1, len(array)):
    if(array[min]>array[j]):
      min = j
  array[min], array[i] = array[i], array[min]

print(array)

# Selection sort(선택 정렬)은 그자체로는 코딩테스트에선 쓰기 힘들지만, list에서 최솟값을 찾을 때 저런 방식으로 찾는다는 구조만 이해하고 넘어가면 될것 같다.