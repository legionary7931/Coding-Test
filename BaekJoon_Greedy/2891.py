"""
<그리디 알고리즘을 해결하는 그날까지....??>
Silver V 카약과 강풍 (https://www.acmicpc.net/problem/2891)
2022. 01. 10

<Idea>
1. 아이디어는 사실 별거 없고, 가질 수 있는 카약의 수를 배열로 저장한다는 점
2. 범위 처리 힘드니까, 쓰레기 값을 하나씩 추가해준것?(cayak 배열의 길이를 (N+2)로 설정하여 맨끝 팀도 손쉽게 처리 할 수 있도록 함))
3. 내가 카약을 2개 가지고 있는데 양 옆에 없다면 카약을 준다! <- main idea
"""


N, S, R = map(int, input().split())
#N = 팀의 수, S = 손상된 팀 수, R = 하나 더 있는 팀 수

cayak = [1 for _ in range(N+2)]

damage_team = list(map(int, input().split()))
bonus_team = list(map(int, input().split()))

for t in damage_team:
  cayak[t]-=1

for b in bonus_team:
  cayak[b]+=1

for i in range(1, len(cayak)):
  if(cayak[i]==2 and cayak[i-1]==0):
    cayak[i-1]+=1
    cayak[i]-=1 
  
  if(cayak[i]==2 and cayak[i+1]==0):
    cayak[i+1]+=1
    cayak[i]-=1

cnt = 0
for i in range(1, len(cayak)):
  if(cayak[i]==0): cnt+=1

print(cnt)
  