def solution(brown, yellow):
    answer = []
    
    x_y = int(brown / 2) + 2 # 가로+세로
    xy = brown + yellow # 가로x세로
    
    for x in range(1, x_y):
        for y in range(1, x_y):
            if (x + y == x_y) and (x*y == xy):
                if x >= y:
                    return [x, y]
        
    return answer