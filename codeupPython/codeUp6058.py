# 6058.
a, b = input().split()
c = bool(int(a))
d = bool(int(b))
print(not(c or d))
print("===========")
print(not c and not d)