class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def find_degree(x, y):
            degree = 0
            if x != 0:
                degree += grid[y][x-1]
            if x != len(grid[0])-1:
                degree += grid[y][x+1]
            if y != 0:
                degree += grid[y-1][x]
            if y != len(grid)-1:
                degree += grid[y+1][x]

            return 4 - degree

        perim = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 1:
                    perim += find_degree(x, y)


        return perim
