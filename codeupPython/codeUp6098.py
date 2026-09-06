# 6098
"""미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지
오른쪽 또는 아래쪽으로만 움직였다.

미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다."""

d = []
for i in range(11):
    d.append([])
    for j in range(11):
        d[i].append(0)

for i in range(1, 11):
    m = list(map(int, input().split()))
    for j in range(1, 11):
        d[i][j] = m[j-1]

x = 2
y = 2
while True:
    if d[x][y] == 2:
        d[x][y] = 9
        break
    elif d[x][y] ==  1:
        y -= 1
        x += 1
        if d[x][y] == 1:
            break
        continue
    elif d[x][y] == 0:
        d[x][y] = 9
        y += 1

for i in range(1, 11):
    for j in range(1, 11):
        print(d[i][j], end= ' ')
    print()