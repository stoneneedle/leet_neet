n = 5
# n = 10

class Solution:
    def climbStairs(self, n):

        def fib_num(num):
            if num == 0:
                return 0
            elif num == 1:
                return 1
            elif num > 1:
                return fib_num(num - 1) + fib_num(num - 2)

        n = n + 1

        return fib_num(n)



s = Solution()
print(s.climbStairs(n))
