def solution(myString, pat):
    
    return 1 if pat in "".join([word.replace("A", "B") if word=="A" else word.replace("B","A") for word in myString]) else 0