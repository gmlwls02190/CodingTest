def solution(arr, intervals):
    answer = []
    for num in intervals:
        for i in range(num[0],num[1]+1):
            answer.append(arr[i])
    return answer