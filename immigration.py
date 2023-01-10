def solution(n, times):
    answer = 0
    a = 1
    max_time = max(times) * n
    
    while a < max_time:
        mid = (a + max_time) // 2
        b = 0
        for t in times:
            b += mid // t 
        if b >= n:
            max_time = mid
        else:
            a = mid + 1
    answer = a    
    return answer
