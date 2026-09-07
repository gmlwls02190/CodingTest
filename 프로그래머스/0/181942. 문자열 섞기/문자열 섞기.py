def solution(str1, str2):
    str3 = ""
    for i in range(len(str1)):
        str3 += str1[i] + str2[i]
    answer = str3
    return answer