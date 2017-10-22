class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        greater = {}
        greater_nums = []
        for num in findNums:
            index = nums.index(num)
            greater_num = -1
            for comp_num in range(index + 1, len(nums)):
                if nums[comp_num] > num:
                    greater_num = nums[comp_num]
                    break
            greater_nums.append(greater_num)

        return greater_nums


    def linearNextGreaterElement(self, findNums, nums):
        cache, stack = {}, []
        for x in nums:
            if len(stack) == 0:
                stack.append(x)
            elif x <= stack[-1]:
                stack.append(x)
            else:
                while stack and stack[-1] < x:
                    cache[stack.pop()] = x
                stack.append(x)
        result = []
        for x in findNums:
            if x in cache:
                result.append(cache[x])
            else:
                result.append(-1)
        return result
