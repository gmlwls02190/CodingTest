def solution(num_list):
    mul = 1
    total = 0
    for num in num_list:
        mul *= num
        total += num
    total **= 2
    if mul < total:
        return 1
    else:
        return 0