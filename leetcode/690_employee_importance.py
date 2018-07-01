
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emp = {}

        for employee in employees:
            emp[employee.id] = employee

        total = 0
        queue = [emp[id]]
        while queue:
            total += queue[0].importance
            for x in queue[0].subordinates:
                queue.append(emp[x])
            queue.pop(0)

        return total
