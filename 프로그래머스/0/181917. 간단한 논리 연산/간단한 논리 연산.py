def solution(x1, x2, x3, x4):
    answer = True
    if x1 or x2:
        x = True
    else:
        x = False
    if x3 or x4:
        y = True
    else:
        y = False
    if x and y:
        answer = True
    else:
        answer = False
    return answer