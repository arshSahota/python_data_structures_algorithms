from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen = {}
        for i, x in enumerate(nums):
            need = target-x
            if need in seen:
                return [seen[need], i]
            seen[x] = i

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))