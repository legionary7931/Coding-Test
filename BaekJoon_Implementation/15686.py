# 2021.12.21 백준 GoldV 치킨배달(15686)
# <ideas>
# 1. 치킨집의 좌표를 x, y로 묶어서 저장
# 2. combination 사용, 하나하나씩 빼서 해야 될 듯..
def get_distance(p1, p2):
  return abs(p1[0]-p2[0]) + abs(p1[1] - p2[1])


from itertools import combinations

arr = []
N, M = map(int, input().split())

for i in range(N):
  arr.append(list(map(int, input().split())))

house = []
chicken = []

#집과 치킨집의 좌표를 먼저 데이터화 해놓은 것은 아주 좋은 시도...
for i in range(N):
  for j in range(N):
    if(arr[i][j] == 1): house.append([i, j])
    if(arr[i][j] == 2): chicken.append([i, j]) #r, c가 1부터 시작하긴 하나 별 의미는 없다. 어차피 치킨 거리는 두 좌표 빼서 구하기 때문....

result = 999999999
distance = 0

for i in range(1, M+1):
  combination = list(combinations(chicken, i)) #일단 combination을 통해 남아있을 치킨집의 개수를 정해놓는다. (남아 있을 수 있는 치킨집은 최소 1개부터 M개 까지)

  for c in combination: # 남아 있는 치킨집의 case중에서
    city_dist = 0
    for home in house: # 남아 있는 치킨집들과, 집들 사이의 치킨 거리를 구한다.
      distance = min([get_distance(home, chicken_data) for chicken_data in c]) #그런데 치킨거리는 남아있는 모든 치킨집들과 집의 거리중 가장 최소가 되는 거리임.
      city_dist += distance #나온 치킨 거리 값을 해당 도시의 치킨 거리로 판정(해당 case에 대해)
    if(result>city_dist): result = city_dist #최소 치킨 거리를 찾기 위함.

# 솔직히 각잡고 했으면 했을텐데... 너무 어렵게 생각해서 망해버린 것 같다. while로 안하고 for문 써도 됐는데...
# distance = min([get_distance(home, chicken_data) for chicken_data in c]) 이런 pythonic한 문장 쓸 수 있도록 체화해두자.
# 문제 잘 읽자! 치킨 거리는 집과 모든 치킨집들의 거리의 합들이 아닌 모든 치킨집과의 거리중 가장 최소 거리가 해당 집의 치킨거리가 되는 것이었다.



print(result)





