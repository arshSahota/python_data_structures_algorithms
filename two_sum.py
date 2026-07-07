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

#time complexity O(n) because you loop through the list once, if nums has n elements, the loop runs n times
#dictionary lookups and insertion are average-case O(1)
#therefore n * O(1) = O(n)
