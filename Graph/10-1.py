"""
2022-01-06 서로소 집합 알고리즘

-> union: 서로 다른 집합들끼리 합침.
-> find: 어떤 특정 노드의 루트노드를 찾기 위함.


일단 

"""


def find_parent(parent, x):
  if(parent[x]!=x):
    return find_parent(parent, parent[x])
  return x

def union_parent(parent, a, b):
  a = find_parent(parent, a) #, a, b의 root_node를 찾아준다.
  b = find_parent(parent, b)

  if(a<b):
    parent[b] = a 
  else:
    parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

print("각 원소가 속한 집합: ", end=" ")
for i in range(1, v+1):
  print(find_parent(parent, i), end=" ")

print()

print(parent)