"""
P345 괄호 변환
18. 괄호 변환 (DFSBFS)
-> 1회차(O), 2022/01/22

TIP)
1. <올바른 문자열 판단하는 알고리즘>
-> Line 을 보면
def chk_proper(p):
  cnt = 0

  for i in range(len(p)):
    if(p[i]=="("): cnt+=1
    else:
      if(cnt == 0): return False
      # cnt==0인 상태에서 p가 올바른 괄호 문자열이려면 ( 가 나와서 짝을 맞추어주어야 한다.
      # 그러나, cnt==0인 상태에서 else조건에 걸렸다는건 )가 나왔다는 의미고, 이는 곧 괄호쌍개수가 절대 맞지 않음을 의미한다.
      cnt-=1

  return True

2. python에서 str형은 item assignment가 안된다.

ex) 
string = "good"
string[2] = i <- 이렇게 할 수 없다.

이런 동작을 하려면 list로 변환후 list를 str로 바꿔주는 join을 사용해야 한다.

3. 이건 문제에 나와있는대로 구현만 했으면 별로 어려울 게 없었다. 재귀문제라고 겁먹지 말자!
"""
def balanced_index(p):
  cnt, index = 0, 0

  for i in range(len(p)):
    if(p[i]=="("): cnt+=1
    elif(p[i]==")"): cnt-=1

    if(cnt==0):
      index = i
      break
  
  return index

# 왜 이게 올바른 문자열을 판단할 수 있는지....?
def chk_proper(p):
  cnt = 0

  for i in range(len(p)):
    if(p[i]=="("): cnt+=1
    else:
      if(cnt == 0): return False
      # cnt==0인 상태에서 p가 올바른 괄호 문자열이려면 ( 가 나와서 짝을 맞추어주어야 한다.
      # 그러나, cnt==0인 상태에서 else조건에 걸렸다는건 )가 나왔다는 의미고, 이는 곧 괄호쌍개수가 절대 맞지 않음을 의미한다.
      cnt-=1

  return True

def solution(p):
  answer = ""
  if(p == ""): return answer

  index = balanced_index(p)

  u = p[:index+1]
  v = p[index+1:]

  if(chk_proper(u)):
    answer = u + solution(v)
  else:
    answer = "("
    answer += solution(v)
    answer += ")"

    u = list(u[1:-1]) # 첫 번째와 마지막 문자 제거

    for i in range(len(u)):
      if(u[i]=="("): u[i]=")"
      elif(u[i]==")"): u[i]="("
    
    answer+="".join(u)

  return answer

p = input()
print(solution(p))