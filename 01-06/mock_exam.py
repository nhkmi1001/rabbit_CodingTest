def solution(answer):
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,1,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    c1, c2, c3 = 0, 0, 0
    
    for i in range(len(answer)):
        b1 = i%5
        b2 = i%8
        b3 = i%10

        if a1[b1] == answer[i]:
            c1 += 1
        if a2[b2] == answer[i]:
            c2 += 1
        if a3[b3] == answer[i]:
            c3 += 1
    k = max(c1, c2, c3)
    answer = []
    
    if k == c1:
        answer.append(1)
    if k == c2:
        answer.append(2)
    if k == c3:
        answer.append(3)
    
    return answer