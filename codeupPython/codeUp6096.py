# 6096.
"""19 x 19 바둑판에서 십(+)자 뒤집기를 수행한다.

좌표 (x, y)를 선택하면 다음 두 작업을 순서대로 한다.
1. x번째 가로줄의 모든 돌을 뒤집는다.
2. y번째 세로줄의 모든 돌을 뒤집는다.

돌은 0과 1 중 하나이므로 XOR 연산(^= 1)을 사용하면
0은 1로, 1은 0으로 간단하게 바꿀 수 있다.
"""
d = [] # 바둑판 제작을 위해 빈리스트 생성
for i in range(20): # 20 X 20 바둑판을 위해 반복 실행
    d.append([]) # 바둑판에 y 열 생성
    for j in range(20): # y 열 20칸 생성
        d[i].append(0) # y 열에 0 추가

for i in range(1, 20): # 바둑판 전체를 입력 받기 위해 반복 실행
    row = list(map(int, input().split())) # 입력받는 값을 정수로 바꾸면서 입력 받는 한 줄을 리스트 형태로 row에 저장
    for j in range(1, 20): 
        d[i][j] = row[j - 1] # d라는 바둑판을 row로 변경 row[j-1]에서 -1을 하는 이유는 d 바둑판의 첫 행 열은 0, 0 이여서 위치를 맞추기 위해 사용

n = int(input())

for _ in range(n):
    x, y = map(int, input().split()) # 뒤집을 x, y 좌표 입력
    for j in range(1, 20):
        d[x][j] = 1 - d[x][j] # 0이면 1 - 0 = 1, 1이면 1 - 1 = 0이 된다
        d[j][y] = 1 - d[j][y]

        # XOR 연산을 사용해 x행의 모든 칸을 뒤집는다
        # d[x][j] ^= 1 
        # d[j][y] ^= 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=" ")
    print()