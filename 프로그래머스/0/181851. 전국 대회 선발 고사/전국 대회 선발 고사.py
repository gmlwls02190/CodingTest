def solution(rank, attendance):
    answer = 0
    is_true = {}
    for i in range(len(attendance)):
        if attendance[i]:
            is_true[rank[i]] = i
            
    sorted_dict=dict(sorted(is_true.items()))
    top3 = []
    for i, (key, value) in enumerate(sorted_dict.items()):
        if i == 3:
            break
        top3.append(value)
    answer = 10000 * top3[0] + 100 * top3[1] + top3[2]
    return answer