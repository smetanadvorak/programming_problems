# Disorderly Escape
# =================
#
# Oh no! You've managed to free the bunny prisoners and escape Commander Lambdas exploding space station, but her team of elite starfighters has flanked your ship. If you dont jump to hyperspace, and fast, youll be shot out of the sky!
#
# Problem is, to avoid detection by galactic law enforcement, Commander Lambda planted her space station in the middle of a quasar quantum flux field. In order to make the jump to hyperspace, you need to know the configuration of celestial bodies in the quadrant you plan to jump through. In order to do *that*, you need to figure out how many configurations each quadrant could possibly have, so that you can pick the optimal quadrant through which youll make your jump.
#
# There's something important to note about quasar quantum flux fields' configurations: when drawn on a star grid, configurations are considered equivalent by grouping rather than by order. That is, for a given set of configurations, if you exchange the position of any two columns or any two rows some number of times, youll find that all of those configurations are equivalent in that way - in grouping, rather than order.
#
# Write a function solution(w, h, s) that takes 3 integers and returns the number of unique, non-equivalent configurations that can be found on a star grid w blocks wide and h blocks tall where each celestial body has s possible states. Equivalency is defined as above: any two star grids with each celestial body in the same state where the actual order of the rows and columns do not matter (and can thus be freely swapped around). Star grid standardization means that the width and height of the grid will always be between 1 and 12, inclusive. And while there are a variety of celestial bodies in each grid, the number of states of those bodies is between 2 and 20, inclusive. The solution can be over 20 digits long, so return it as a decimal string.  The intermediate values can also be large, so you will likely need to use at least 64-bit integers.
#
# For example, consider w=2, h=2, s=2. We have a 2x2 grid where each celestial body is either in state 0 (for instance, silent) or state 1 (for instance, noisy).  We can examine which grids are equivalent by swapping rows and columns.
#
# 00
# 00
#
# In the above configuration, all celestial bodies are "silent" - that is, they have a state of 0 - so any swap of row or column would keep it in the same state.
#
# 00 00 01 10
# 01 10 00 00
#
# 1 celestial body is emitting noise - that is, has a state of 1 - so swapping rows and columns can put it in any of the 4 positions.  All four of the above configurations are equivalent.
#
# 00 11
# 11 00
#
# 2 celestial bodies are emitting noise side-by-side.  Swapping columns leaves them unchanged, and swapping rows simply moves them between the top and bottom.  In both, the *groupings* are the same: one row with two bodies in state 0, one row with two bodies in state 1, and two columns with one of each state.
#
# 01 10
# 01 10
#
# 2 noisy celestial bodies adjacent vertically. This is symmetric to the side-by-side case, but it is different because there's no way to transpose the grid.
#
# 01 10
# 10 01
#
# 2 noisy celestial bodies diagonally.  Both have 2 rows and 2 columns that have one of each state, so they are equivalent to each other.
#
# 01 10 11 11
# 11 11 01 10
#
# 3 noisy celestial bodies, similar to the case where only one of four is noisy.
#
# 11
# 11
#
# 4 noisy celestial bodies.
#
# There are 7 distinct, non-equivalent grids in total, so solution(2, 2, 2) would return 7.
#
# Languages
# =========
#
# To provide a Java solution, edit Solution.java
# To provide a Python solution, edit solution.py
#
# Test cases
# ==========
# Your code should pass the following test cases.
# Note that it may also be run against hidden test cases not shown here.
#
# -- Java cases --
# Input:
# Solution.solution(2, 3, 4)
# Output:
#     430
#
# Input:
# Solution.solution(2, 2, 2)
# Output:
#     7
#
# -- Python cases --
# Input:
# solution.solution(2, 3, 4)
# Output:
#     430
#
# Input:
# solution.solution(2, 2, 2)
# Output:
#     7


# def number_of_multinomial_coefficients(number, kinds):
#     return binomial_coefficient(kinds+number-1, kinds-1)
#
# def M(number, kinds):
#     return number_of_multinomial_coefficients(number, kinds)
#
# def half_solution(w,h,s):
#     res = M(h, M(w,s)) + B(s ** w - M(w,s), h-1)
#     return res
#
# from math import factorial
#
# def binomial_coefficient(n,k):
#     if n == k:
#         return 1
#     if k > n:
#         return 0
#     return factorial(n)/(factorial(k)*factorial(n-k))
#
# def B(n, k):
#     return binomial_coefficient(n,k)

# Solution is based on Burnside's Lemma and corresponding formula.
# To calculate the number of orbits of group G (combinations of hor and vert
# permutations) on X (integer matrices with values from 1 to S),
# we should calculate the number of matrices that are fixed by each of the
# w!h! permutations.
# To do that, we'll group the permutations, based on their cycle representation

from copy import copy

permutation_categories = []

def get_permutation_categories(n, k, composition=[]):
    if n == 0:
        permutation_categories.append(composition)
    else:
        for i in range(1, k+1):
            if n >= i:
                c = copy(composition)
                c.append(i)
                get_permutation_categories(n-i, k, c)


def gen_vars(n, lim):
    soln_set = [] # store the solution set in a list
    if n > 0: # breaks recursive loop when false and returns an empty list
        for x in range(lim, 0, -1): # work backwards from the limit
            if x == 1: # breaks recursive loop when true and returns a populated list
                soln_set.append([(1, n)])
            else: # otherwise, enter recursion based on how many x go into n
                for y in range(int(n / x), 0, -1):
                    # use recursion on the remainder across all values smaller than x
                    recurse = gen_vars(n - x * y, x - 1)
                    # if recursion comes up empty, add the value by itself to the solution set
                    if len(recurse) == 0:
                        soln_set.append([(x, y)])
                    # otherwise, append the current value to each solution and add that to the solution set
                    for soln in recurse:
                        soln_set.append([(x, y)] + soln)
    return soln_set # return the list of solutions


def solution(w, h, s):
    res = 0
    return str(int(res))

print(gen_vars(4,4))
get_permutation_categories(4, 4)
print(permutation_categories)

# print(solution(2,2,2))
#
# print(solution(2,3,4))
#
# print(solution(3,2,4))
#
# print(solution(11,3,2))
#
# print(solution(3,11,2))
#
# print(solution(1,10,2))
# print(solution(10,1,2))





















#blah
