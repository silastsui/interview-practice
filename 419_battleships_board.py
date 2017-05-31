class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        board_copy = board
        # iterate over rows, then iterate over columns
        count = 0
        for row in board:
