class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diff = {}
        for x in range(len(nums)):
            if nums[x] in diff.keys():
                return [diff[nums[x]], x]
            diff[target - nums[x]] = x
