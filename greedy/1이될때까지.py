def solution(m, k):
    result = 0

    while m > 1:
        if m % k == 0:
            m = m/k
            result += 1
        else:
            m -= 1
            result += 1

    return result

print(solution(25, 3))