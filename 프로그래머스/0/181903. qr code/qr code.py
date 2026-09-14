def solution(q, r, code):
    answer = ''
    word_list = []
    for i in range(0,len(code),q):
        word_list.append(code[i:i+q])
    
    for word in word_list:
        if len(word)<=r:
            continue
        else:
            answer += word[r]
        
    print(word_list)
    return answer