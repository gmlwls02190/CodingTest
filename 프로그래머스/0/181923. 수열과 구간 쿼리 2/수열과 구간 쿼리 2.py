def solution(arr, queries):
    answer = []
    for i in range(len(queries)):
        s,e,k = queries[i]
        min = 0 # 최소값 저장
        for j in range(s, e+1):
            if arr[j]>k:
                if min==0 or min>arr[j]: # min이 arr[j]보다 크다면 min에 arr[j] 저장
                    min = arr[j]
        if min != 0: # min이 0이 아니면 min을 추가
            answer.append(min)
        else: # 안쪽for문에서 min이 변경이 안됐다면 -1 추가
            answer.append(-1)
    return answer