"""
<그리디 알고리즘을 해결하는 그날까지....??>
Gold V 센서 (https://www.acmicpc.net/problem/2212)
2022. 01. 16

<Idea>
1. 주어진 배열을 그대로 사용하는게 아니라, 주어진 배열에서 데이터를 추출하여 그 배열을 정렬해본다.
(여기선 센서간의 거리 배열 dist를 만들어내서 정렬했다.)
2. 난 처음에 K를 고려하지 않고 문제를 풀려 했었다..(의미 없이 주는 데이터는 없다)
3. 예를 들어, 각 수신소 사이의 거리가 2 3 0 1 2라면, 이를 내림차순으로 정렬 후(->3 2 2 1 0),
수신소가 2개일시 -> 하나 거리 포함은 면제 됨
(1-3 6-7-9를 선택하고, 3-6에 해당되는 거리 3은 제외)가 이문제의 메인 아이디어
"""
N = int(input())
K = int(input())
arr=sorted(list(map(int, input().split())))

dist = []
for i in range(len(arr)-1):
  dist.append(arr[i+1]-arr[i])

dist.sort(reverse=True)

answer = 0
for i in range(K-1, len(dist)):
  answer+=dist[i]
print(answer)


