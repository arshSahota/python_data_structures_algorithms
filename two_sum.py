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

#space complexity: O(n)
# dictionary stores values that we have seen

# why use a dictionary
# because I need fast lookups. For every number, I can calculate its complement and check whether I've already seen it in O(1) time. This reduces 
# the overall runtime from O(n^2) to O(n)