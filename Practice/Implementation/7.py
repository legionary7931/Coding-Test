"""
P321 럭키 스트레이트
7. 럭키 스트레이트(Implementation)
-> 1회차(), 2021/12/30
<Keypoint> 
-> 어려운 거 없음..
-> 파이썬은 input을 str로 받는다는 걸 기억하고, 제발 자릿수로 끊어서 리스트 만드는 법 숙지해두자..

<중요> data = list(map(int, input()))

"""
data = list(map(int, input()))

left = data[0:len(data)//2]
right = data[len(data)//2 : len(data)]

if(sum(left)==sum(right)): print("LUCKY")
else: print("READY")

