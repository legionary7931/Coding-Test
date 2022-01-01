"""
P311 그리디 문제
1. 모험가 길드 (Greedy Algorithm)
-> 1회차(X), 2021/12/28
TIP) 엄밀한 그룹 구성원까지 파악해 놓으란 것이 아니다.

KeyPoint) 만들고 있는 그룹원 수가 현재 모험가의 공포도 이상이라면 (ex) 공포도 3인데 그룹에는 3명의 모험가가 존재), 다른 그룹을 형성해준다.

"""

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

result = 0 #전체 그룹 수
count = 0 #현재 그룹에 포함된 모험가 수

for i in arr:
  count+=1
  if(count>=i):
    result+=1
    count=0

print(result)
