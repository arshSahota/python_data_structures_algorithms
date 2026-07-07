# Given an integer array nums, return True if any value appears at least twice.
# Return False if every element is distinct.

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

sol = Solution()
print(sol.containsDuplicate([1,2,3,4]))

# Time complexity: we go thru each element once so O(n)
# Space Complexity: O(n) we store each element in set except the duplicates
# why use set? because set does not contain duplicates and insertions and searches are faster!
# one line solution
# return len(nums) != len(set(nums))
