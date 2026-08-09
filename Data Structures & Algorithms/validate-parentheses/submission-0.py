class Solution:
    def isValid(self, s: str) -> bool:
        matches = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket in "({[":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                recent = stack.pop()
                if matches[bracket] != recent:
                    return False
        return not stack
        
