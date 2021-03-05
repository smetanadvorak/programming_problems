# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.
from collections import deque

def check_perfectness(num):
    return sum(map(int, str(num))) == 10

def find_nth_perfect_number(n):
    d = deque()
    for i in range(1,10):
        d.append(i)

    while n > 0:
        num = d.popleft()
        if check_perfectness(num):
            n -= 1

        for i in range(10):
            d.append(int(str(num) + str(i)))

    return num


for i in range(1,100):
    print(find_nth_perfect_number(i))
    
