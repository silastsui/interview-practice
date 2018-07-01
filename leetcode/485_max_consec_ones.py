class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        count = 0
        for x in nums:
            if x == 0:
                if count > max_num:
                    max_num = count
                count = 0
            else:
                count += 1

        if count > max_num:
            max_num = count

        return max_num
