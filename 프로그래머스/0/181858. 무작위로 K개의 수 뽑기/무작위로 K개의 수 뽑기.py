def solution(arr, k):
    answer = []
    for num in arr:
        if num in answer:
            continue
        elif len(answer)==k:
            break
        else:
            answer.append(num)
    if len(answer)<k:
        for i in range(k-len(answer)):
            answer.append(-1)
            
    return answer