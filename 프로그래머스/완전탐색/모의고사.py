def solution(answers):
    case = [
        [1, 2, 3, 4, 5], 
        [2, 1, 2, 3, 2, 4, 2, 5], 
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]    
        ]
    answer = []
    cnt = [0] * 3

    for i, v in enumerate(answers):
        for idx, val in enumerate(case):
            if v == val[i % len(val)]:
                cnt[idx] += 1
    
    for i, v in enumerate(cnt):
        if v == max(cnt):
            answer.append(i+1)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))