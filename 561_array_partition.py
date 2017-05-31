class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sum = 0
        nums = sorted(nums, reverse=True)
        for num in range(0, len(nums), 2):
            sum += min(nums[num], nums[num+1])

        return sum
