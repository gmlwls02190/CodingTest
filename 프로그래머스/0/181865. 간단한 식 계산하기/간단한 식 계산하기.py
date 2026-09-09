def solution(binomial):
    bi_list = binomial.split()
    res = 0
    for i in range(len(bi_list)):
        if bi_list[i] == "+":
            res = int(bi_list[0]) + int(bi_list[-1])
        elif bi_list[i] == "-":
            res = int(bi_list[0]) - int(bi_list[-1])
        else:
            res = int(bi_list[0]) * int(bi_list[-1])
            
        
    return eval(binomial)