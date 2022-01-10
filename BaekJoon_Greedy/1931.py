"""
<그리디 알고리즘을 해결하는 그날까지....??>
Silver II 회의실배정 (https://www.acmicpc.net/problem/1931)
2021. 12. 30

이 문제의 핵심은 "끝나는 시간이 작은 순서대로 정렬한다는 것이 핵심이다."

1. 끝나는 시간이 가장 작은 회의를 첫번째 가능한 회의로 가져가고,
2. 그 뒤에 정렬되어있는 회의를 하나하나 보면서 그 전 회의의 end시간과 회의의 시작시간(v[1])과 겹치지 않는지 확인한다.
3. 만일 v[1]<end, 회의의 시작시간이 end시간보다 앞이라면 회의 진행 불가
4. 그렇지 않다면 end를 v[0]로 최신화하고 result 하나씩 올려준다.
"""


import heapq

N=int(input())
q = []

for _ in range(N):
  start, end = map(int, input().split())

  heapq.heappush(q, [end, start])

# 끝나는 시간이 작은 순서대로 정렬!

end = heapq.heappop(q)[0]
result=1

data = []
while(q):
  v = heapq.heappop(q)
 

  if(v[1]<end): continue
  else:
    data.append(v)
    end = v[0]
    result+=1    

#print(data)
print(result)







