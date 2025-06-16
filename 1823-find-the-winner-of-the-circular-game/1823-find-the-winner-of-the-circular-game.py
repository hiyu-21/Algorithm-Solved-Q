class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        for j in range (1, n + 1):
            i = (i + k) % j
        return i + 1