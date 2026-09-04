# 6079.
"""1, 2, 3 ... 을 계속 더해 나갈 때,
그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
계속 더하는 프로그램을 작성해보자.

즉, 1부터 n까지 정수를 계속 더해 나간다고 할 때,
어디까지 더해야 입력한 수보다 같거나 커지는 지를 알아보고자하는 문제이다."""

# ex1)
n = int(input())
sum = 0
for i in range(1, n+1, 1):
    if sum <= n:
        sum += i
        if sum >= n:
            print(i)
            break

# ex2)
n = int(input()) # 입력값
s = 0 # 합을 알기 위한 변수
t = 0 # 횟수를 
while s<n :
  t = t+1
  s = s+t
print(t)

# ex3)
n=int(input())
s=0
while True:
    s+=1
    n-=s
    if n<=0:
        print(s)
        break