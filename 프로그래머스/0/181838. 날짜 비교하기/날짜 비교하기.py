def solution(date1, date2):
    answer = 0
    for i in range(3):
        if date1[i] > date2[i]:
            answer = 0
            break
        elif date1[i] == date2[i]:
            answer = 0
        else:
            answer = 1
            break
    return answer