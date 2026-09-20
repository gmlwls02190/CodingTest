def solution(picture, k):
    answer = []
    temp = []
    for list in picture:
        for _ in range(k):
            for word in list:
                temp.append(word*k)
            answer.append("".join(temp))
            temp = []
    return answer