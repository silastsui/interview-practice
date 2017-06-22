class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        next_element = {}
        for num in nums:
            while 
            if num+1 in nums:
                next_element[num] = num+1
            else:
                next_element[num] = -1

        next_nums = []
        for num in range(len(findNums)):
            next_nums.append(next_element[findNums[num]])

        return next_nums
