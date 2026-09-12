def solution(a, b):
    res1 = str(a) + str(b)
    res2 = str(b) + str(a)
    # res1 = int(res1)
    # res2 = int(res2)
    res1, res2 = map(int, [res1, res2])
    if res1 >= res2:
        answer = res1
    else:
        answer = res2
    return answer