def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        s,e,k = queries[i]
        min = 0
        for j in range(s, e+1):
            if arr[j]>k:
                if min==0 or min>arr[j]:
                    min = arr[j]
        if min != 0:
            answer.append(min)
        else:
            answer.append(-1)
    return answer