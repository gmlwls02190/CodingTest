def solution(arr):
    answer = arr
    length = len(arr)
    i = 1
    while i < length:
        i *= 2
        
    for _ in range(i-length):
        answer.append(0)
        
    return answer