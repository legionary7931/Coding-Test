#이진탐색을 반복문으로 구현한 사례
def binary_search(array, target, start, end):
  while(start<=end):
    mid = (start+end)//2

    if(array[mid] == target): return mid
    elif(array[mid] > target):
      end = mid-1
    else: start = mid+1
  
  return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if(result==None):
  print("존재 안 함")
else:
  print(result+1)

# 보통은 순차탐색으로 풀리겠지만(시간복잡도 : O(N)), 그렇지 않은 경우에는(입력 데이터가 1000억 이상이라던가... 처럼 입력데이터가 너무 많을 경우)
# sys 라이브러리의 readline 함수를 사용하면 된다.

"""
<readline 함수 사용하는 예시>
import sys
input = sys.stdin.readline().rstrip()

print(input)
"""