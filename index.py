class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        z = []
        sign = 1
        if x < 0:
        	sign = -1
        	x *= -1
        y = str(x) [::-1]
        t = int(y) * sign
        if t > pow(2, 31) - 1 or t < pow(2, 31) * -1:
        	return 0
        return t

my_test = Solution()
sample = [123, -123, 120, 1534236469]

for m in sample:
  print("%d => %d" % (m, my_test.reverse(m)))
