class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        nsum = [left + right]

        for i in range(len(nums)):
            if nums[i] == 0:
                left+=1
            if nums[i] == 1:
                right -=1
            nsum.append(left + right)
            vmax = max(nsum)
        return( [i for i, v in enumerate(nsum) if v==vmax])