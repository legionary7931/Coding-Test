"""
<그리디 알고리즘을 해결하는 그날까지....??>
Silver IV 1543(https://www.acmicpc.net/problem/1543)
2022. 01. 03

1. 솔직히 왜 그리디인지는 모르겠다...?
2. 간단한 문자열 탐색 브루트포스로서, word길이만큼 비교해주고 같으면 그 word만큼 잘라주고,
3. 아니라면 첫번째 글자부터 다시 탐색한다.
"""

document = input()
word = input()

result = 0

while(len(word)<=len(document)):
  if(document[0]==word[0]):
    if(document[0:len(word)] == word):
    # 첫 글자가 서로 일치한다면 맞는지 비교해준다.
      result+=1
      document = document[len(word):]
    # 첫 글자만 일치하면 첫글자 하나만 잘라준다.
    else: document = document[1:]
  else: 
    # 아예 첫글자조차 일치하지 않아도 첫글자 하나만 잘라준다.
    document = document[1:]
  
print(result)