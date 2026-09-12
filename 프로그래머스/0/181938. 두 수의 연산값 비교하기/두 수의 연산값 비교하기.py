def solution(a, b):
    str1 = str(a) + str(b)
    res = 2 * a * b
    str1 = int(str1)
    if str1 >= res:
        answer = str1
    else:
        answer = res
    return answer