    class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        sorted_people = []
        for person in sorted(people, key=lambda x: x[0], reverse=True):
            sorted_people.insert(person[1], person)

        return sorted_people
