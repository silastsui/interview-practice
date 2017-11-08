class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor = x^y
        count = 0
        while xor > 0:
            if xor%2 == 1:
                count += 1
            xor /= 2
        return count
