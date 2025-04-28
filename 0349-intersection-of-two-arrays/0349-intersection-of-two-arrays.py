class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in range(len(nums1)):
            if nums1[i] not in result:
                for j in range(len(nums2)):
                    if nums1[i] == nums2[j]:
                         result.append(nums1[i])
                         break
        return result                 
