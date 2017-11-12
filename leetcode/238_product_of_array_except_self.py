class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = []
        p = 1
        for x in range(len(nums)):
            product.append(p)
            p = p * nums[x]

        p = 1
        for x in range(len(nums)-1, -1, -1):
            product[x] = product[x] * p
            p = p * nums[x]

        return product

a = Solution()
print(a.productExceptSelf([1, 2, 3, 4]))
