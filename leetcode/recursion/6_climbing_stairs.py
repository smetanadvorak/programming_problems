# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if not n in self.memo:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

S = Solution()

for n in range(1,50):
    print('%d-th Result: %d' % (n, S.climbStairs(n)))
