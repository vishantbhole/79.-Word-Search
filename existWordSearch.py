
#79. Word Search
from typing import List

class Solution:
    def existWordSearch(self, board: List[List[str]], word: str) -> bool:
        # O(n * m * 4^k) where k is len of word
