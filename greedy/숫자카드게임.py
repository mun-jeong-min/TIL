#1
def solution(value):
    rst = []

    for i in value:
        rst.append(min(i))

    return max(rst)
#2
def main():
    minus = []
    n, m = map(int, input().split())

    for i in range(n):
        values = list(map(int, input().split()))

        minus.append(min(values))

    return max(minus)

print(main())
print(solution([[3,1,2],[4,1,4],[2,2,2]]))