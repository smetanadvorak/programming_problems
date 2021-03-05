def solution(x, y):
    if len(x) > len(y):
        x, y = y, x

    z = [False for i in range(2001)]

    for elem in x:
        z[elem] = True

    for elem in y:
        if not z[elem]:
            return elem

print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))
