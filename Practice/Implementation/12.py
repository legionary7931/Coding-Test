"""
P329 기둥과 보 설치
12. 기둥과 보 설치(Implementation)
-> 1회차(X)), 2022/01/11
<Keypoint>
1. frame=[1, 2, 3, 4] 일때
x, y, stuff, operate = frame하면 순서대로 대입 가능하다. 
2. 시간 제한 5초이므로 구조물 전체 순회하면서 봐도 상관이 없다. <- O(n^3)이 되네...

"""
def possible(answer):
  for x, y, stuff in answer: #구조물 하나씩 일일히 파악
    if(stuff==0): #설치된게 기둥일 때
      if y==0 or [x-1, y, 1] in answer or [x, y, 1] in answer or [x, y-1, 0] in answer:
        """
        1. y==0: 바닥에 설치되어 있을 때
        2. [x-1, y, 1]: 보의 오른쪽 끝에 기둥이 설치됨.
        3. [x, y, 1]: 보의 왼쪽 끝에 기둥이 설치됨.
        4. [x, y-1, 0]: 다른 기둥의 위에 설치됨.
        """
        continue
      return False #기둥이 불가능하다면 False 리턴
    
    elif(stuff==1): #설치된게 보일 때
      if [x, y-1, 0] in answer or [x+1, y-1, 0] in answer or([x-1, y, 1] in answer and [x+1, y, 1] in answer):
        """
          1. [x, y-1, 0]: 보 왼쪽 밑에 기둥이 있을 때
          2. [x+1, y-1, 0]: 보의 오른쪽 끝에 기둥이 설치됨.
          3. [x, y, 1] and [x, y-1, 0]: 보 양끝에 다른 보들이 양쪽으로 존재 
        """
        continue
      return False
  
  return True


def solution(n, build_frame):
  answer = []

  for frame in build_frame:
    x, y, stuff, operate = frame #요렇게도 대입된다 기억

    if operate==0: # 만일 행동이 삭제일때
      answer.remove([x, y, stuff]) # 일단 삭제해보고
      if not possible(answer): # 나올 수 없는 구조물이다?
        answer.append([x, y, stuff]) # 그럼 원복

    if operate==1:
      answer.append([x, y, stuff]) # 만일 행동이 build일때
      if not possible(answer): # 나올 수 없는 구조물이다?
        answer.remove([x, y, stuff]) # 그럼 다시 원복

  return sorted(answer)

n = int(input())
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

print(solution(n, build_frame))