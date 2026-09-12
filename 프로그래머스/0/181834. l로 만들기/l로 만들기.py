def solution(myString):
    answer = ''
    for i in range(len(myString)):
        if ord(myString[i]) <= ord("l"):
            answer += myString[i].replace(myString[i],"l")
        else:
            answer += myString[i]
    return answer