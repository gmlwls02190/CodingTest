def solution(a, b, c, d):
    answer = 0
    n_list = [a,b,c,d]
    n_list.sort()
    
    z,x,c,v = n_list[0], n_list[1], n_list[2], n_list[3]
    
    answer = z
    if z==v:
        answer = 1111*z  
    elif z==c and c!=v:
        answer = (10*z+v)**2
    elif x==v and z!=x:
        answer = (10*x+z)**2
    elif z==x and c==v:
        answer = (z+c)*abs(z-c)
    elif z==x:
        answer = c*v
    elif x==c:
        answer = z*v
    elif c==v:
        answer = z*x
        
    return answer