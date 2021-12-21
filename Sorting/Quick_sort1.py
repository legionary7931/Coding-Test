# 퀵 소트의 구현
# 1. 리스트의 첫 번째 데이터를 피벗으로 정한다.
# 2. 왼쪽부터는 피벗보다 큰 값을, 오른쪽부터는 피벗보다 작은 값을 선택하고, 두 값의 위치를 서로 바꿔준다.
# 3. 이 과정을 반복하며, 정렬하려는 리스트의 len값이 1이 될 때(피벗밖에 값이 없을 때) 해당 정렬을 종료한다. 

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if(start>=end): return
    # quick_sort의 종료조건(피벗값밖에 값이 없을 때)

  pivot = start
  left = start+1
  right = end
  
  while(left<=right):
    while(left<=end and array[left]<=array[pivot]): # left와 right를 결정...
      left+=1
    while(right>start and array[right]>=array[pivot]):
      right-=1

    if(left>right): array[right], array[pivot] = array[pivot], array[right] 
    # left, right 엇갈릴 경우(left right 모두 array끝까지 갔을 것이다. p 166참조)) pivot과 작은 값을 바꾸어 준다. (해당 pivot에 대해선 분할 완료)
    else: array[left], array[right] = array[right], array[left] # 분할 진행중

  quick_sort(array, start, right-1)
  quick_sort(array, right+1, end)

    




quick_sort(array, 0, len(array)-1)
print(array)
