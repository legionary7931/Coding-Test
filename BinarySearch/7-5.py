#197p 부품 찾기 - 이진 탐색 알고리즘을 사용하여 문제를 품.
def binary_search(arr, target, start, end):
  if(start>end):
    print("no", end=" ")
    return 
  
  mid = (start+end)//2

  if arr[mid] == target:
    print("yes", end=" ")
    return
  
  elif arr[mid]>target:
    return binary_search(arr, target, start, mid-1)
  else:
    return binary_search(arr, target, mid+1, end)

#부품 array
N = int(input())
arr = list(map(int, input().split()))
arr.sort()

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
  binary_search(arr, target, 0, len(arr)-1)

