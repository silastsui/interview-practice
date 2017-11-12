class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """

        while n:
            if n % 2 == n / 2 % 2:
                return False
            n = n / 2

        return True
