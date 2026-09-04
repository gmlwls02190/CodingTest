# 6064.
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
# a if a < b else b a가 b 보다 작다면 a를 아니면 b
# if(a if a < b else b) < c else c ()안에서 나온 값이 c보다 작다면 ()안의 값이 아니면 c
print((a if a < b else b) if(a if a < b else b) < c else c)