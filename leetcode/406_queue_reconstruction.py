class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        before = {}
        for x in people:
            if x[0] not in before:
                before[x[0]] = 0

        l_bound = min(before.keys())
        r_bound = max(before.keys())

        ordered = False
        while not ordered:
            ordered = True
            for x in range(len(people)):
                if people[x][1] == before[people[x][0]]:
                    before[people[x][0]] += 1
                # too many tall people in front of them
                elif people[x][1] < before[people[x][0]]:
                    ordered = False
                    # find how many people taller than them are in front of them
                    taller = sum([before[k] for k in range(people[x][1], r_bound+1)])

                # not enough tall people in front of them
                elif people[x][1] < before[people[x][0]]:
                    ordered = False


        return before



a = Solution()
print(a.reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))
