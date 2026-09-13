def solution(arr):
    answer = [-1]
    flag = False
    for i in range(len(arr)):
        if arr[i]==2:
            for j in range(-1,-len(arr)-1,-1):
                if arr[j]==2 and j+1!=0:
                    answer = arr[i:j+1]
                    flag = True
                    break
                elif arr[j]==2 and j+1==0:
                    answer = arr[i:]
                    flag = True
                    break
        if flag:
            break
    
    return answer