class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def check_array(arr):
            for x in range(len(arr)):
                if arr[x] == 0:
                    continue
                if arr[x] % x != 0 and x % arr[x] != 0:
                    return False
            return True
