class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        if r*c != len(nums) * len(nums[0]):
            return nums
        concat_nums = []
        for row in nums:
            concat_nums += row
        new_nums = []
        for column in range(r):
            temp_row = []
            for row in range(c):
                temp_row.append(concat_nums.pop(0))
            new_nums.append(temp_row)
        return new_nums


a = Solution()
print(a.matrixReshape([[1,2], [3,4]], 2, 4))
