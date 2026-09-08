def solution(a, b, c):
    if a != b and a != c and b != c:
        answer = a + b + c
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        # (a == b) + (b == c) + (c == a) == 1
        # True=1 False=0을 이용해서 셋중 하나가 True일 경우 세 숫자중 두 숫자만 같은 경우
        answer = (a + b + c)*(a**2 + b**2 + c**2)
    elif a == b == c:
        answer = (a + b + c)*(a**2 + b**2 + c**2)*(a**3 + b**3 + c**3)
    return answer