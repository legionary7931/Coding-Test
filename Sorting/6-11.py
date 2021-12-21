N = int(input())
arr = []

for i in range(N):
  data = input().split()
  arr.append((data[0], int(data[1])))

arr = sorted(arr, key = lambda student: student[1])

for student in arr:
  print(student[0], end = " ")