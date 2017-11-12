class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x > 2147483647 or x < -2147483647:
            return 0

        x = str(x)[::-1]

        if x[-1] == '-':
            x = x[-1] + x[:-1]
            
        return int(x)
