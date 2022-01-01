"""
P322 문자열 재정렬
8. 문자열 재정렬
(Implementation)
-> 1회차(O), 2021/12/30
<Keypoint> 
딱히....

<중요> 
1. isalpha, isdigit의 사용법 알아두기
2. join의 사용법 알아두기(리스트 문자열 변환시 사용)

"""
data = list(input())

strings = []
total = 0

for ch in data:
  if(ch.isalpha()):
    strings+=ch
  elif(ch.isdigit()):
    total+=int(ch)

strings.sort()

print("".join(_ for _ in strings)+str(total))