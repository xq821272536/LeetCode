class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        t = 10
        temp = 2
        while n > 5:
            while n // (t*10) > 0:
                t *= 10
                res += temp*10+2

            pres = n // 10
            if pres >= 5:


            n = n % t
        if n >= 5:
            res += 1
        return res


n = 54
print(Solution().trailingZeroes(n))

import math
value = math.factorial(n)
print(value)
