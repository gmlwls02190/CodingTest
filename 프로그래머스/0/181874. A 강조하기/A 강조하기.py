def solution(myString):
    answer = ""
    for str in myString.lower():
        if "a" == str:
            answer += str.upper()
        else:
            answer += str
    return answer