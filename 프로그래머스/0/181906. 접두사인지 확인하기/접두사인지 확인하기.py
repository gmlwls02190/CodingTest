def solution(my_string, is_prefix):
    if is_prefix in my_string and my_string[:len(is_prefix)]==is_prefix:
        answer = 1
    else:
        answer = 0
    return answer