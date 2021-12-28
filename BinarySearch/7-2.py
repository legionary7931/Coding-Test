# 이진탐색을 재귀로 구현한 사례 (반복무으로 구현해도 별거 없다...)
def binary_search(array, target, start, end):
  if(start>end):
    return None
  
  mid = (start+end)//2

  if(array[mid]==target):
    return mid

  elif(target<array[mid]):
    return binary_search(array, target, start, mid-1)
  
  elif(target>array[mid]):
    return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if(result==None):
  print("존재 안 함")
else:
  print(result+1)
