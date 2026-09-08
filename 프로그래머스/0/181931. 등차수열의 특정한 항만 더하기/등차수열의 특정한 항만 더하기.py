def solution(a, d, included):
    total = 0
    for i in range(len(included)):
        if included[i] is True:
            total += a
        a += d
    return total