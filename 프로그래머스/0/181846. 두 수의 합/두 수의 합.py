def solution(a, b):
    answer = []
    carry = 0 # 올림수를 저장할 변수
    
    # 두 문자열의 맨 뒤부터 계산을 하기 위한 인덱스 계산
    i = len(a)-1
    j = len(b)-1
    
    # 올림수도 없을때 까지 반복
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            num_a = int(a[i])
        else:
            num_a = 0
        if j >= 0:
            num_b = int(b[j])
        else:
            num_b = 0
    
        sum = num_a + num_b + carry # 올림수와 같이 계산
        carry = sum//10 # 10으로 나눈 몫을 올림수에 저장
        res = sum%10 # 10으로 나눈 나머지 값을 저장
        answer.append(str(res))
        i -= 1
        j -= 1
    return "".join(answer[::-1]) # 뒤에서 부터 계산했기 때문에 다시 역순으로 출력