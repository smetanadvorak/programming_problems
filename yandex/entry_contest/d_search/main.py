from collections import Counter
from sys import getsizeof
C = Counter()
memory_limit = 500

n_unique = 0
kept_from_last_chunk = 0

with open('input2.txt', 'r') as f:
    n = int(f.readline())
    for i in range(n):
        search = f.readline()
        C.update([search])
        if getsizeof(C)/1024 > memory_limit - 1:
            n_unique += len(C) - kept_from_last_chunk
            C = Counter(C.most_common(int(len(C)*3/4)))
            C.subtract(C)
            kept_from_last_chunk = len(C)
            print(i, 'Chunk!', C.__sizeof__()/1024)

n_unique += len(C) - kept_from_last_chunk

print(n_unique)











# C = Counter()
# memory_limit = 9000
#
#
# n = int(input())
# for i in range(n):
#     search = input()
#     C.update([search])
#     if C.__sizeof__()/1024 > memory_limit - 1:
#         break
#
# print(len(C) * (i+1) / n)
