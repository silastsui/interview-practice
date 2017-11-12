class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            n = num
            num = 0
            while n > 0:
                num += n%10
                n = n//10

        return num

    def addDigitsNoLoop(self, num):
        if num == 0:
            return 0
        return 1 + ((num-1)%9)
