array = [7, 5, 9, 0, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
  for j in range(i, 0, -1):
    if array[j]<array[j-1]: #더 작은 숫자가 나올 때까지 자리 바꾸기 (삽입정렬은 앞의 데이터들은 모두 정렬되어 있다고 간주한다.)
      array[j], array[j-1] = array[j-1], array[j]
    else: break 

print(array)

# 시간 복잡도: O(n^2), 정렬하려는 배열이 거의 정렬되어 있는 경우(최선의 경우, O(N))
# 따라서, 거의 정렬된 배열을 정렬할때는 퀵소트나 sort()를 쓰는 것보다 삽입정렬을 쓰는 것이 나을 때도 있다. 
