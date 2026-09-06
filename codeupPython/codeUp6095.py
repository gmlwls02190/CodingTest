# 95.
"""기숙사 생활을 하는 학교에서 어떤 금요일(전원 귀가일)에는 모두 집으로 귀가를 한다.

오랜만에 집에 간 영일이는 아버지와 함께 두던 매우 큰 오목에 대해서 생각해 보다가
"바둑판에 돌을 올린 것을 프로그래밍 할 수 있을까?"하고 생각하였다.

바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자."""

n = int(input())

d = []
for i in range(20): # 20x20 리스트 생성
    d.append([]) # d라는 리스트안에 20개의 빈 리스트 생성
    for j in range(20):
        d[i].append("O") # d[i][j]에 0을 생성

for i in range(n):
    x, y = map(int, input().split())
    d[x][y] = "X"

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ') # 바둑판에 돌이 놓인 위치 출력
    print() # 줄 바꿈