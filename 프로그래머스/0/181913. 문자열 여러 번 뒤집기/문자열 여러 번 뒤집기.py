def solution(my_string, queries):
    answer = ''
    for query in queries:
        a = query[0]
        b = query[1]
        my_string = my_string[:a] + my_string[a:b+1][::-1] + my_string[b+1:]
    return my_string