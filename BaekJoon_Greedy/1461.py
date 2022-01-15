"""
<그리디 알고리즘을 해결하는 그날까지....??>
GoldV 1461 도서관(https://www.acmicpc.net/problem/1461)
2022. 01. 15

<KeyPoint>
-> -39 -37 -29 -28 -6 2 11이 있다고 가정하면,
-> (-39 -37), (-29 -28), (-6), (2, 11) 로 묶어주고,
-> 맨 마지막에는 원점을 안찍어도 되므로, (-39 -37)그룹을 맨 마지막에 방문할 수 있도록 하는게 최선이다!
-> 답: 39 + 29*2 + 6*2 + 11*2 = 131

<구현 버벅인점>
-> 음수 그룹의 절댓값 최대 책과 양수 그룹 최대 거리 책의 값을 비교해서 절댓값이 더 큰 책을 맨 마지막에 방문해야 하므로, 일단 2배한 값을 전부 더해준 뒤 나중에 빼는 알고리즘을 만들었다.
-> 하지만 음수그룹을 나중에 뺄때 abs를 안해주면 오히려 거리값이 더해진다!
"""
N, M = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

book_left, book_right = [], []

for num in arr:
  if(num<0): book_left.append(num)
  else: book_right.append(num)

result, cnt = 0, 0
while(cnt<len(book_left)):
  result+=2*abs(book_left[cnt])
  cnt+=M

cnt = 0
if(book_right): book_right.sort(reverse=True)
while(cnt<len(book_right)):
  result+=2*book_right[cnt]
  cnt+=M

if(book_left and book_right):
  result -= max(abs(book_left[0]), book_right[0])
else:
  if(book_left): result -= abs(book_left[0]) #여기 abs 안한거 주의!!!!
  elif(book_right): result -= book_right[0]

print(result)

# -39 -37 -29 -28 -6 2 11