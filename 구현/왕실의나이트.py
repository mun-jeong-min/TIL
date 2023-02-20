def solution(scape):
    alpa = ["a", "b", "c", "d", "e", "f", "g", "h"]
    move = ["-2,1","-2,-1","-1,2","-1,-2","1,-2","1,2","2,-1","2,1"]

    a = list(scape)[0]
    b = int(list(scape)[1]) - 1

    cnt = -1
    for i in alpa:
        cnt += 1
        if a == i:
            break

    count = 0
    for i in move:
        na = cnt + int(i.split(",")[0])
        nb = b + int(i.split(",")[1])

        if na < 0 or nb < 0 or na >= 8 or nb >= 8:
            continue
        count += 1

    return count

print(solution("c2"))
print(solution("a1"))