class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT_MAX = (1<<31)-1
        INT_MIN = -1<<31
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
        y*sign
        if y > INT_MAX or y < INT_MIN:
        	return 0
        return y
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
sample = [123, -123, 120, 1534236469, -2147483412]

for m in sample:
  print("%d => %d" % (m, my_test.reverse(m)))
