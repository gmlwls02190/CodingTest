def solution(ineq, eq, n, m):
    
    if eq == '=':
        if eval(f"{n} {ineq}{eq} {m}"):
            answer = 1
        else:
            answer = 0
    else:
        if eval(f"{n} {ineq} {m}"):
            answer = 1
        else:
            answer = 0
    return answer