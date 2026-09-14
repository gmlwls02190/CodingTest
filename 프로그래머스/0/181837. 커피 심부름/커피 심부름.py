def solution(order):
    answer = 0
    for i in range(len(order)):
        if "americano" in order[i] or "anything" in order[i]:
            # print("check")
            answer += 4500
        elif "cafelatte" in order[i]:
            answer += 5000
    return answer