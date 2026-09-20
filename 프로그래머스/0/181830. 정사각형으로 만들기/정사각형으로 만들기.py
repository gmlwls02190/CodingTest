def solution(arr):
    x = len(arr)
    y = len(arr[0])
    if x > y:
        for i in range(x):
            arr[i] += [0] * (x - y)
    elif y > x:
        for _ in range(y - x):
            arr.append([0] * y)
    return arr