from itertools import permutations

def solution(numbers):
    answer = []
    nums = [n for n in numbers]
    per = []
    for i in range(1, len(numbers)+1):
        per += list(permutations(nums, i))
    int_num = [int(("").join(p)) for p in per]
    for n in int_num:
        if n < 2:
            continue
        sosu = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                sosu = False
                break
        if sosu:
            answer.append(n)
    
    return len(set(answer))

print(solution("17"))