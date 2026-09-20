def solution(my_string):
    answer = []
    for _ in range(52):
        answer.append(0)
        
    word_dict = {}
    count = 0
    for i in range(ord('A'),ord('Z')+1):
        word_dict[chr(i)] = count
        count += 1
    for i in range(ord('a'),ord('z')+1):
        word_dict[chr(i)] = count
        count += 1
    
    for word in my_string:
        answer[word_dict[word]] += 1
    return answer