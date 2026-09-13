def solution(my_string, s, e):
    answer = ''
    
    for word in reversed(my_string[s:e+1]):
        answer += word
    
    answer = my_string[:s] + answer + my_string[e+1:]
    
    return answer