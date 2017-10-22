#linear time with linear space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for num in nums:
            if num not in dict:
                dict[num] = True
            elif num in dict:
                del dict[num]
        return dict.keys()[0]


#linear time without extra space
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for num in nums:
            result ^= num
        return result
