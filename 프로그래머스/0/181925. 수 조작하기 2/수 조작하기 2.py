def solution(numLog):
    n = len(numLog)
    answer = ''
    num_dict = {'w':1, 's':-1, 'd':10, 'a':-10}
    for i in range(n-1):
        for key in num_dict:
            if numLog[i+1] - numLog[i] == num_dict[key]:
                answer += key
    return answer