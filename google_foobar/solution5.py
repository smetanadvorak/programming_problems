# In order to destroy Commander Lambda's LAMBCHOP doomsday device, you'll need access to it. But the only door leading to the LAMBCHOP chamber is secured with a unique lock system whose number of passcodes changes daily. Commander Lambda gets a report every day that includes the locks' access codes, but only she knows how to figure out which of several lists contains the access codes. You need to find a way to determine which list contains the access codes once you're ready to go in.
#
# Fortunately, now that you're Commander Lambda's personal assistant, she's confided to you that she made all the access codes "lucky triples" in order to help her better find them in the lists. A "lucky triple" is a tuple (x, y, z) where x divides y and y divides z, such as (1, 2, 4). With that information, you can figure out which list contains the number of access codes that matches the number of locks on the door when you're ready to go in (for example, if there's 5 passcodes, you'd need to find a list with 5 "lucky triple" access codes).
#
# Write a function solution(l) that takes a list of positive integers l and counts the number of "lucky triples" of (li, lj, lk) where the list indices meet the requirement i < j < k.  The length of l is between 2 and 2000 inclusive.  The elements of l are between 1 and 999999 inclusive.  The answer fits within a signed 32-bit integer. Some of the lists are purposely generated without any access codes to throw off spies, so if no triples are found, return 0.
#
# For example, [1, 2, 3, 4, 5, 6] has the triples: [1, 2, 4], [1, 2, 6], [1, 3, 6], making the answer 3 total.

from collections import deque
from random import randint
from random import seed
seed(1)


# class Node:
#     def __init__(self , value, parent = [], children = []):
#         self.parent = parent
#         self.children = children
#         self.value = value
#
# def add_node(root, new):
#     new = Node(new)
#     d = deque([root])
#     while d:
#         node = d.pop()
#         print(len(d))
#         for ch in node.children:
#             d.append(ch)
#
#         if not new.value % node.value:
#             new.parent.append(node)
#             node.children.append(new)
#
# def print_graph(root):
#     print(root.value)
#     for ch in root.children:
#         print_graph(ch)

#def build_graph(list):
#    list.sort()
#    graph = [Node(list[0])]
#    for elem in list[1:]:

#            if not elem % leaf.value:
#                n.parent += leaf





def solution(l):
#     list.sort()
#     graph = Node(1)
#     for elem in list:
#         print('Element: ', elem)
#         add_node(graph, elem)
#
#     return graph
    #list.sort()
    print('Solution for', l)
    N = 0
    for i in range(len(l)-2):
        for j in range(i+1, len(l)-1):
            if not (l[j] % l[i]):
                for k in range(j+1,len(l)):
                    if not (l[k] % l[j]):
                        print('%d %d %d' % (l[i],l[j],l[k]))
                        N += 1

    return N

print(solution([1, 2]))
print(solution([1, 2, 3]))
print(solution([1, 1, 1]))
print(solution([1, 1, 1, 1]))
print(solution([1, 2, 3, 4, 5, 6]))
# N = 1
# for i in [1, 3, 5, 7, 11, 13, 17, 23, 31]:
#     N *= i
print(solution([1, 3, 5, 7, 11, 13, 17, 23, 31]))
# input()
# print(solution([randint(1,2000) for i in range(1, 2000)]))
