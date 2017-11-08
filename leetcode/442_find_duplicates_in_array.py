class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # integers in array are between 1 and len(nums)
        # use input array as a hash 
        dupes = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                dupes.append(abs(num))
            else:
                nums[abs(num)-1] *= -1

        return dupes
