class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        x = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                print(nums)
                nums[x], nums[j] = nums[j], nums[x]
                x += 1

        return nums
