def solution(l, r):
    answer = []
    for i in range(1,65): # 제한사항의 최대값을 이진수로 생각해서 해당 값을 십진수로 표현하면 64
        bi_num = int(bin(i)[2:].replace("1","5")) # i를 이진수로 바꾸고 1을 5로 변환후 int로 다시 타입변환
        
        if bi_num > r:
            break
        if bi_num >= l:
            answer.append(bi_num)
    
    if not answer:
        answer.append(-1)
    return answer