"""
<그리디 알고리즘을 해결하는 그날까지....??>
Gold V(https://www.acmicpc.net/problem/12904)
2022. 01. 12

<Keypoint>
-> 그리디에서 볼 수 있는 흔한 유형 "거꾸로 생각하기"
-> S에서 T를 만드는 과정 대신 T에서 S를 만들 수 있는지를 생각해본다!!!!
-> 어떻게 보면 11501(주식) 문제와 비슷한 문제라고도 볼 수 있다. (첫날부터 보는게 아니라 마지막 날부터 for문 순회)
"""
def solve(S, T):
  while(len(S)<len(T)):
    if(T[-1] == 'A'): 
      T = T[:-1]
    elif(T[-1]=='B'):
      T = T[::-1]
      T = T[1:]
  
  if(S==T): return 1
  else: return 0

S = input()
T = input()

print(solve(S,T))

