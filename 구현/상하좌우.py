def solution(n, values):
    width = 0
    length = 0

    x = [-1,1,0,0]
    y = [0,0,-1,1]
    move = ["L","R","U","D"]

    for i in values:
        for j in range(len(move)):
            if i == move[j]:
                nx = width + x[j]
                ny = length + y[j]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        width = nx
        length = ny

    return length+1, width+1

print(solution(5, ["R","R","R","U","D","D"]))