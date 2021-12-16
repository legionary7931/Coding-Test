location = input()
direction = [[-2, -1], [-2, 1], [-1, 2], [1, 2], [2, -1], [2, 1], [1, -2], [-1, -2]]

col = ord(location[0]) - 96
row = int(location[1])

answer = 0

for way in direction:
  if(1<=col+way[0]<=8 and 1<=row+way[1]<=8):
    print(col+way[0], row+way[1])
    answer+=1

print(answer)

