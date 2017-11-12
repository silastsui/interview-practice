class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        high = n/2
        low = 0

        while (low < high):
            idx = (low + high) /2
            if (nums[2*idx] != nums[2*idx + 1]):
                high = idx
            else:
                low = idx + 1

        return nums[2*low]
