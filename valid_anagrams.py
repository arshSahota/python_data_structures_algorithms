# Given two strings s and t, return True if t is an anagram of s, and False otherwise.
# An anagram contains the same characters with the same frequencies.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        for char in s:
            count[char] = count.get(char, 0)+1
        
        for char in t:
            count[char] = count.get(char, 0)-1
        
        return all(v == 0 for v in count.values())

    
sol = Solution()
print(sol.isAnagram("rat", "car"))
print(sol.isAnagram("anagram", "nagaram"))

# Time complexity => O(n)+O(n) = O(n) because we go over both strings
# Space Complexity: O(k) where k is the # of unique characters
# Worst Case - O(n) where every character is unique
# Hash map vs sorting approach idk sorting takes O(nlogn) time complexity and O(n) space complexity