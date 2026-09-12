def solution(my_string, m, c):
    answer = []
    word = ''
    for i in range(0,len(my_string),m):
        answer.append(my_string[i:i+m])
    for w in answer:
        word += w[c-1]
    return word