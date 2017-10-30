class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        # We can also use array[i] = array[i/2] + i%2

        power = 0
        array = [0]

        for i in range(1,num+1):
            if i == 2**power:
                power += 1
                array.append(1)
            else:
                array.append(1 + array[i - 2**power])

        return arrays
