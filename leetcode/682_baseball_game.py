class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        valid_ops = []
        score = 0
        for item in ops:
            if item == '+':
                valid_ops.append(valid_ops[-1] + valid_ops[-2])
            elif item == 'D':
                valid_ops.append(2 * valid_ops[-1])
            elif item == 'C':
                valid_ops.pop()
            else:
                valid_ops.append(int(item))

        return sum(score)
