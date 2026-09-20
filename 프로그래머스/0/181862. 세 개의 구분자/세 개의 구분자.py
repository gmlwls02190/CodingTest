def solution(myStr):
    answer = []
    temp = '' # 임시저장
    for word in myStr:
        if word == 'a' or word == 'b' or word == 'c':
            if temp: # 임시저장에 문자가 들어 있다면
                answer.append(temp) # 해당 문자 추가
                temp = '' # a, b, c를 만났기 때문에 초기화후 다시 반복
        else: # a, b, c가 아닌 문자들을 저장
            temp += word
    if temp: # 반복문이 끝나고 남아 있는 문자 추가
        answer.append(temp)
    if not answer:
        answer.append("EMPTY")
    return answer