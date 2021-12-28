#197p 부품 찾기 - set 자료형을 사용함
# set 자료형은 특정 데이터가 존재하는지 검사할 때 효과적으로 사용 가능.


N = int(input())
arr = set(map(int, input().split()))

M = int(input())
targets = list(map(int, input().split()))

for target in targets:
  if target in arr:
    print("yes", end=" ")
  else:
    print("no", end = " ")
