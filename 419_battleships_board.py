class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        # NOT YET COMPELTE

        checked_board = list(board)
        count = 0

        #Returns which spaces to check
        def check_space(row, column):
            if (row, column) == (0, 0):
                spaces = [(row+1, column), (row, column+1)]
            elif (row, column) == (0, len(board[row])-1):
                spaces = [(row+1, column), (row, column-1)]
            elif (row, column) == (len(board)-1, 0):
                spaces = [(row-1, column), (row, column+1)]
            elif (row, column) == (len(board)-1, len(board[row])-1):
                spaces = [(row-1, column), (row, column-1)]
            elif row == 0:
                spaces = [(row+1, column), (row, column-1), (row, column+1)]
            elif row == len(board)-1:
                spaces = [(row-1, column), (row, column-1), (row, column+1)]
            elif column == 0:
                spaces = [(row-1, column), (row+1, column), (row, column+1)]
            elif column == len(board[row]) - 1:
                spaces = [(row-1, column), (row+1, column), (row, column-1)]
            else:
                spaces = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
            return spaces

        for row in range(len(board)):
            for column in range(len(board[row])):
                beside_known_battleship = False
                for check_row, check_column in check_space(row, column):
                    #if checked_board and board are the same, it hasn't been checked yet
                    if checked_board[check_row][check_column] == 'X' and board[check_row][check_column] == '.':
                        beside_known_battleship = True
                        continue
                if beside_known_battleship == False:
                    count += 1
                checked_board[row][column] == '.'
        return count

a = Solution()
print a.countBattleships([['X', '.', '.', 'X'], ['.', '.', '.', 'X'], ['.', '.', '.', 'X']])
