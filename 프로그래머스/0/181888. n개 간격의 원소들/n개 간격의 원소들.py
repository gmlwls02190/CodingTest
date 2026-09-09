def solution(num_list, n):
    return [num_list[i] for i in range(len(num_list)) if i%n==0]