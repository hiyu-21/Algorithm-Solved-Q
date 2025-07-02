class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        t = 0
        s =0
        d = 0
        for i in nums:
            t+=i
            if i < 10:
                s+=i
            else:
                d+=i
        if s > t-s or d > t-d:
            return True
        else: 
            return False

        