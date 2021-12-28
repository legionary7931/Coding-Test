#201p 떡볶이 떡 만들기 문제

#이진 탐색이 문제로서 활용될 수 있는 Parametric Search 유형의 문제에 해당된다.

#절단기 높이를 순차탐색을 통해서 차근차근히 높이다 보면 떡의 길이 2000000000까지 가는데 하루 종일 걸린다.
#그러나 이진탐색을 통해 절단기 높이를 높이다 보면 31번의 탐색을 통해 절단기 높이를 찾아낼 수 있다.

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
#M = 필요한 떡의 길이

start = 0
end = max(arr)


answer = -1
while(start<=end):
  mid = (start+end)//2
  remain = 0
  for i in arr:
    if i>mid:
      remain+=(i-mid)

  if(remain>M):
    start = mid+1
    answer = mid
  else:
    end = mid-1


print(answer+1)

#parametric search 유형의 문제의 경우는 재귀적인 구현보다는 반복문으로 구현하는 것이 구현하기에는 훨씬 좋다......
