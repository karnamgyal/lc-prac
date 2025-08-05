class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = { "(" : ")", "[" : "]", "{" : "}" }

        for c in s:
            if c in brackets.keys():
                stack.append(c)
            elif c in brackets.values():
                if not stack:
                    return False
                last = stack[-1]
                if c == brackets[last]:
                    stack.pop()
                else: 
                    return False
            else:
                return False
        return not stack