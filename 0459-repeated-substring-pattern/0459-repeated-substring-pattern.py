class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

# Testing kecil
sol = Solution()
print(sol.repeatedSubstringPattern("abab"))       # True
print(sol.repeatedSubstringPattern("aba"))        # False
print(sol.repeatedSubstringPattern("abcabcabcabc")) # True
