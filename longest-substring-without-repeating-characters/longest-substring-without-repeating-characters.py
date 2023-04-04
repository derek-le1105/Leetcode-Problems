class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        currWindow = []
        maxLen = 0
        for char in s:
            if char not in currWindow:
                currWindow.append(char)
            else:
                if currWindow[0] == char:
                    currWindow.pop(0)
                    currWindow.append(char)
                else:
                    idx = currWindow.index(char)
                    currWindow = currWindow[idx+1:]
                    currWindow.append(char)
            if maxLen < len(currWindow):
                maxLen = len(currWindow)
        return maxLen