class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = 0
        seen = set()
        longest = 0

        for b in range(len(s)):
            while s[b] in seen:
                seen.remove(s[a])
                a += 1
            seen.add(s[b])
            longest = max(longest, b - a + 1)

        return longest