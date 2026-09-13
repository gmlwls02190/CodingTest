def solution(myString, pat):
    idx = myString.rfind(pat)
    
    if idx != -1:
        end_idx = idx + len(pat)
        
    answer = myString[:end_idx]
    return answer