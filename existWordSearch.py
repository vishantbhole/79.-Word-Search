
#79. Word Search
from typing import List

class Solution:
    def existWordSearch(self, board: List[List[str]], word: str) -> bool:
        # O(n * m * 4^k) where k is len of word
        ROWS = len(board)
        COLS = len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
                    r >= ROWS or c >= COLS or
                    word[i] != board[r][c] or
                    (r, c) in path):
                return False
