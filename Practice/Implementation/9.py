"""
P323
9. 문자열 압축
(Implementation)
-> 1회차(O), 2022/01/05
<Keypoint> 
1. s의 길이 1000밖에 안되므로 일일히 하나씩 다 해봐도 통과가 가능하다는 것을 인지해준다.
2. token의 길이는 문자열의 s의 절반 이상을 넘을 수 없다. (token의 길이가 그 이상이 된다면 압축 자체가 불가능하다.)

<중요> 

s = "ssibal"
s = s[6:]
if(s==""): print("ok")
else: print("No")

해당 코드는 s의 길이보다 큰 index 6에서부터 split을 하려고 하지만, 정상적으로 ok를 출력한다.

(파이썬에선 스플릿 할때 끝의 범위 체크 해줄 필요 없다. 알아서 빈문자열로 만들어줌 ㅎㅎ)
"""
def solution(s):
  unit = 0
  result_len = 999999999

  while(unit<=len(s)//2):
    new_str = ""
    tmp_str = s

    unit+=1
    while(tmp_str):
      st = tmp_str[0:unit]
      cnt = 1

      for j in range(unit, len(tmp_str)+1, unit): #token을 0~unit-1까지 잘랐으므로 unit부터 비교해준다.
        if(st==tmp_str[j:j+unit]):
          cnt+=1
        else: break
      tmp_str = tmp_str[j:] #break된 곳이 잘리고 남은 곳에 해당한다.

      if(cnt==1): new_str += st #반복되는 문자가 없다면 token하나만 새로운 문자열에 추가한다.
      else: new_str += (str(cnt)+st)

    if(len(new_str)<result_len):
      result_len = len(new_str)

  return result_len
  
s = input()

print(solution(s))