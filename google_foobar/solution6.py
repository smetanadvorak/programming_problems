# Fuel Injection Perfection
# =========================
#
# Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.
#
# Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.
#
# The fuel control mechanisms have three operations:
#
# 1) Add one fuel pellet
# 2) Remove one fuel pellet
# 3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)
#
# Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.
#
# For example:
# solution(4) returns 2: 4 -> 2 -> 1
# solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

from collections import deque
#import matplotlib.pyplot as plt

def solution3(n):
    n = int(n)

    # Get the upper limit in the search
    # (helps to limit graph growth caused by + operation)
    up_degree = 1
    while n > pow(2, up_degree):
        up_degree += 1
    up_border = pow(2, up_degree)

    # Do BFS from 'n' to '1'
    d_nodes = deque([n])
    d_dists = deque([0])
    visited = []
    while d_nodes:
        node = d_nodes.popleft()
        dist = d_dists.popleft()
        visited.append(node)

        # Check if finished
        if node == 1:
            return dist

        # Add /2 number to the deque:
        if not node % 2:
            next_node = node/2
            if not (next_node in visited):
                d_nodes += [next_node]
                d_dists += [dist + 1]
                continue

        # Add +1 number to the deque if it's not unnecesarily big
        next_node = node + 1
        if not (next_node in visited) and (next_node <= up_border):
            d_nodes += [next_node]
            d_dists += [dist + 1]

        # Add -1 number to the deque
        next_node = node - 1
        if not (next_node in visited):
            d_nodes += [next_node]
            d_dists += [dist + 1]


# def solution2(n):
    # n = format(int(n), 'b')[::-1]
    # res = 0
    # i = 0
    # while len(n) != 1:
    #     if n[0] == '1':
    #         if len(n) >= 3 and n[:3] == '111':
    #             n = int(n[::-1],2) + 1
    #             n = format(int(n), 'b')[::-1]
    #             res += 1
    #         else:
    #             res += 2
    #             n = n[1:]
    #     else:
    #         res += 1
    #         n = n[1:]
    # return res

from collections import deque

def solution(n):
    # This algorithm always divides by 2 when possible.
    # When it is not, it decides whether do +1 or -1 based on how it
    # changes the binary representation of the number.
    # It seeks to minimize the number of '1's and the number of '01' and '10'
    # subsequences in the binary representation of the number.
    # The idea behind it is to maximize the number of '0's (because they always
    # require one single division operation to get rid of) and, if '1' are present,
    # maximize the lenght of '11...11' sequences because they require one +1 operation
    # to become '100...00'.
    ndecimal = int(n)
    nbinary  = format(ndecimal, 'b') # Get binary representation of the number

    res = 0
    while len(nbinary) != 1:
        if nbinary[-1] == '1':
            nplus = format(ndecimal+1, 'b') # Get binary of '+1' decision
            p = map(int, nplus)             # Represent as a list of 0s and 1s
            pd = [abs(f - s) for (f,s) in zip(p, p[1:])]  # Calculate its 'oddity'

            nminus = format(ndecimal-1, 'b') # Same for '-1' decision
            m = map(int, nminus)
            md = [abs(f - s) for (f,s) in zip(m, m[1:])]

            if sum(md)+sum(m) <= sum(pd)+sum(p): # Compare the costs of the two decisionss
                nbinary = nminus
                ndecimal -= 1
            else:
                nbinary  = nplus
                ndecimal += 1
            res += 1

        # Now it is guaranteed that there is zero in LSB,
        # so diivide by two (discard the LSB):
        res += 1
        nbinary  = nbinary[:-1]
        ndecimal /= 2
    return res



res = []
res2 = []
inputs = range(1,10000)
for input in inputs:
    s  = solution(str(input))
    s2 = solution3(str(input))
    res.append(s)
    res2.append(s2)
    print('%d: %d, %s, %d' % (input, s, bin(input), s2))
#    print('%d: %s, %d' % (input, bin(input), s2))

# plt.plot(res)
# plt.plot(res2)
# plt.show()

if res == res2:
    print('Same!')

for i in range(len(inputs)):
    if res[i] != res2[i]:
        print(inputs[i], bin(inputs[i]))


# print(solution('1'))
# print(solution('2'))
# print(solution('3'))
# print(solution('4'))
# print(solution('15'))
# print(solution('30'))
# print(solution('31'))
# print(solution('33'))
# print(solution('100'))
# print(solution('001000'))
#print(solution('2371'))
#print(solution('65536'))
#print(str_mult( map(int, '99') ))
#print(str_plus( map(int, '99') ))
#print(str_minus( map(int, '1') ))

# print(str_mult( map(int, '1') ))
# print(str_plus( map(int, '1') ))
# print(str_minus( map(int, '1') ))



# def str_mult(s):
#     carry = 0
#     for i in range(len(s)-1, -1, -1):
#         res = s[i] * 2 + carry
#         if res >= 10:
#             res -= 10
#             carry = 1
#         else:
#             carry = 0
#         s[i] = res
#     if carry:
#         s.insert(0,carry)
#     return s
#
# def str_plus(s):
#     carry = 0
#     res = s[-1] + 1
#     if res == 10:
#         s[-1] = 0
#         carry = 1
#         for i in range(len(s)-2,-1,-1): #while carry
#             res = s[i] + carry
#             if res == 10:
#                 res = 0
#                 carry = 1
#             else:
#                 carry = 0
#             s[i] = res
#     else:
#         s[-1] = res
#
#     if carry:
#         s.insert(0,carry)
#     return s
#
# def str_minus(s):
#     res = s[-1] - 1
#     carry = 0
#     if res == -1:
#         s[-1] = 9
#         carry = -1
#         for i in range(len(s)-2,-1,-1): #while carry
#             res = s[i] + carry
#             if res == -1:
#                 res = 9
#                 carry = -1
#             else:
#                 carry = 0
#             s[i] = res
#     else:
#         s[-1] = res
#
#     if carry == -1:
#         return [-1]
#     if len(s) > 1 and s[0] == 0:
#         del s[0]
#     return s
#
#
#
#
# def solution(n):
#     print('Solution for', n)
#     # Delete any preceding zeros, if there are
#     n_list = map(int, n)
#     i = 0
#     while n_list[i] == 0:
#         i += 1
#     del n_list[0:i]
#     n = ''.join(map(str, n_list))
#
#     d_nodes = deque('1')
#     d_dists = deque([0])
#     visited = []
#     while d_nodes:
#         node = d_nodes.popleft()
#         dist = d_dists.popleft()
#         #print('Node', node)
#         visited.append(node)
#         # Check if finished
#         if node == n:
#             return dist
#
#         # Add *2 number to the deque
#         node = map(int, node)
#         next_node = ''.join(map(str, str_mult(node[:])))
#         if not (next_node in visited) and not (len(next_node) > len(n) + 1):
#             #print('*', next_node)
#             d_nodes.append(next_node)
#             d_dists.append(dist + 1)
#
#         # Add +1 number to the deque of it's not unnecesarily big
#         next_node = ''.join(map(str, str_plus(node[:])))
#         if not (next_node in visited) and not (len(next_node) > len(n) + 1):
#             #print('+',next_node)
#             d_nodes.append(next_node)
#             d_dists.append(dist + 1)
#
#         # Add -1 number to the deque
#         next_node = ''.join(map(str, str_minus(node[:])))
#         if not (next_node in visited) and not (next_node == '0'):
#             #print('-',next_node)
#             d_nodes.append(next_node)
#             d_dists.append(dist + 1)
#
#     return None
