location = input()
direction = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1], [1, -2], [-1, -2]]
# 이렇게 미리 정해둔 방향을 리스트로 만들어 두는 형식은 굉장히 많이 사용하는 형식이므로 참고하자


col = ord(location[0]) - 96
row = int(location[1])

answer = 0

for way in direction:
  if(1<=col+way[0]<=8 and 1<=row+way[1]<=8):
    print(col+way[0], row+way[1])
    answer+=1

print(answer)
