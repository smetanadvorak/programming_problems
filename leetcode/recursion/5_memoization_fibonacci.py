# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
#
# F(0) = 0, F(1) = 1
# F(n) = F(n - 1) + F(n - 2), for n > 1.

class Solution:
    memo = {0: 0, 1: 1} # Memoization cache, start with two first numbers

    def fib(self, n: int) -> int:
        if n >= len(self.memo): # comparing n to len(memo) is enough since
                                # for m if exists memo[m], then exists memo[<m]
            self.memo[n] = self.fib(n-1) + self.fib(n-2)
        return self.memo[n]

S = Solution()

for n in range(51,1,-1):
    print('%d-th Fibonacci number: %d' % (n, S.fib(n)))
