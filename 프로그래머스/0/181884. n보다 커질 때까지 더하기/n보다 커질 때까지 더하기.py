def solution(numbers, n):
    sum = 0
    for num in numbers:
        if n >= sum:
            sum += num
        
    return sum