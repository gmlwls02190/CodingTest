def solution(num_list):
    even_sum = 0
    odd_sum = 0
    for i in range(len(num_list)):
        if i%2==0:
            odd_sum += num_list[i]
        else:
            even_sum += num_list[i]
            
    if odd_sum > even_sum:
        return odd_sum
    elif odd_sum < even_sum:
        return even_sum
    else:
        return even_sum