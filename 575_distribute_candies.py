class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candy_list = {}
        for kind in candies:
            if kind not in candy_list:
                candy_list[kind] = True
        if len(candy_list) <= len(candies)/2:
            return len(candy_list)
        return len(candies)/2
