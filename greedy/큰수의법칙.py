def solution(a, b, c, values):

    check = 0
    result = 0
    values.sort()

    for i in range(b):
        if check == c:
            result += values[a-2]
            check = 0
        else:
            result += values[a-1]
        check += 1

    return result

print(solution(5, 8, 3, [2, 4, 2, 5, 6]))