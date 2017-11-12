class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        opt = 0
        i = 1
        for j in range(2,len(A)):
            if A[j]-A[j-1] == A[j-1]-A[j-2]:
                opt += i
                i += 1
            else:
                i = 1
        return opt
