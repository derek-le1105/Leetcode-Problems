class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = s.lower()
        l = 0
        r = len(newStr) - 1
        while l <= r:
            if newStr[l] == newStr[r]:
                l += 1
                r -= 1
            elif not newStr[l].isalnum():
                l += 1
            elif not newStr[r].isalnum():
                r -= 1
            else:
                return False
        return True
                