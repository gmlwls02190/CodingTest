def solution(strArr):
    # answer = 0
    # for i in range(len(strArr)):
    #     count = 0
    #     for j in range(len(strArr)):
    #         if len(strArr[i])==len(strArr[j]):
    #             count += 1
    #     if answer < count:
    #         answer = count
    # return answer
    
    count_dict = {} # 각 문자길이 별로 몇개 있는지 카운트위해 딕셔러리 사용
    for word in strArr:
        length = len(word) # 리스트에서 가져온 문자열들의 길이 측정
        count_dict[length] = count_dict.get(length, 0) + 1
        # 딕셔너리에 length(len(word))라는 키의 밸류에 기본으로 1 값을 주고 이미 있다면 +1
        
    return max(count_dict.values()) # 저장된 밸류중 가장 큰 값을 반환