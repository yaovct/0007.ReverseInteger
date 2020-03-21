class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
        	sign = -1
        	x *= -1
        y = 0
        while x > 10:
        	if y > 0:
        		y *= 10
        	y += x % 10
        	x = x / 10
        y *= 10
        y += x % 10
        if y > pow(2, 31) - 1 or y < pow(2, 31) * -1:
        	return 0
        return y*sign
#        z = []
#        sign = 1
#        if x < 0:
#        	sign = -1
#        	x *= -1
#        y = str(x) [::-1]
#        t = int(y) * sign
#        if t > pow(2, 31) - 1 or t < pow(2, 31) * -1:
#        	return 0
#        return t

my_test = Solution()
sample = [123, -123, 120, 1534236469]

for m in sample:
  print("%d => %d" % (m, my_test.reverse(m)))
