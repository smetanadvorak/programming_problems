from collections import deque

with open('input.txt', 'r') as f:
    n, m = map(int, f.readline().split())
    b = []
    for i in range(n):
        b.append(int(f.readline()))

print(b)

feed = []
i = 0
type = None
add_later = deque([])
while i < n:
    if b[i] != type:
        feed.append(i)
        type = b[i]
    else:
        for j in range(len(add_later)):
            if type != b[add_later[j]]:
                feed.append(add_later[j])
                del add_later[j]
                break
        add_later.append(i)
    i += 1

print(feed)

# def value(i, j):
#     return 2**(-i) * 2**(-j)
#
# def printknapSack(W, wt, n):
#     K = [[0 for w in range(W + 1)]
#             for i in range(n + 1)]
#
#     # Build table K[][] in bottom
#     # up manner
#     for i in range(n + 1):
#         for w in range(W + 1):
#             if i == 0 or w == 0:
#                 K[i][w] = 0
#             elif wt[i - 1] <= w:
#                 K[i][w] = max(value(i-1, w-1)
#                   + K[i - 1][w - wt[i - 1]],
#                                K[i - 1][w])
#             else:
#                 K[i][w] = K[i - 1][w]
#
#
#
#     res = K[n][W]
#     print(res)
#
#     w = W
#     for i in range(n, 0, -1):
#         if res <= 0:
#             break
#         # either the result comes from the
#         # top (K[i-1][w]) or from (val[i-1]
#         # + K[i-1] [w-wt[i-1]]) as in Knapsack
#         # table. If it comes from the latter
#         # one/ it means the item is included.
#         if res == K[i - 1][w]:
#             continue
#         else:
#
#             # This item is included.
#             print(w)
#
#             # Since this weight is included
#             # its value is deducted
#             res = res - value(i,w)
#             w = w - wt[i - 1]
#
# # Driver code
# wt = [ 1 for i in range(n) ]
# W = n
#
# printknapSack(W, wt, n)
