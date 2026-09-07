def solution(n):
    sum = 0
    mul = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            mul += i**2
        else:
            sum += i 
    return mul if n % 2 == 0 else sum